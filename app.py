from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from contextlib import asynccontextmanager
import math
import logging
import MetaTrader5 as mt5

logger = logging.getLogger("uvicorn.error")

@asynccontextmanager
async def lifespan(app: FastAPI):
    if not mt5.initialize():
        logger.critical("Failed to connect to MT5")
    else:
        logger.info("MT5 connection established")
    yield
    mt5.shutdown()
    logger.info("MT5 connection closed")

app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="frontend/dist"), name="static")

@app.get("/")
async def main_index():
    return FileResponse("frontend/dist/index.html")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            if type(data) == list:
                await websocket.send_json(get_symbols_info(data))
            else:
                await websocket.send_json({"message": "error"})

    except WebSocketDisconnect:
        pass
        

def get_symbols_info(symbols_list: list[str]):
    symbol_data_list: list[dict[str: str, str: float | None, str: float | None, str: float | None]] = []
    for symbol in symbols_list:
        new_symbol_dict = {}
        new_symbol_dict["symbol"] = symbol
        new_symbol_dict["decimal_points"] = None
        point = None
        
        symbol_info = mt5.symbol_info(symbol)
        if symbol_info is not None:
            info_dict = symbol_info._asdict()
            new_symbol_dict["trade_tick_value"] = info_dict.get("trade_tick_value")
            new_symbol_dict["volume_min"] = info_dict.get("volume_min")
            point = info_dict.get("point")
        else:
            new_symbol_dict["trade_tick_value"] = None
            new_symbol_dict["volume_min"] = None

        symbol_info_tick = mt5.symbol_info_tick(symbol)
        if symbol_info_tick is not None:
            info_tick_dict = symbol_info_tick._asdict()
            ask = info_tick_dict.get("ask")
            if type(ask) == float and point is not None:
                decimal_places = get_decimal_places(point)
                formatted_ask = truncate(ask, decimal_places)
                new_symbol_dict["ask"] = formatted_ask
                new_symbol_dict["decimal_points"] = decimal_places
            else:
                new_symbol_dict["ask"] = ask
        else:
            new_symbol_dict["ask"] = None
        
        symbol_data_list.append(new_symbol_dict)

    return symbol_data_list
        

def get_decimal_places(num: float) -> int:
    num_str = str(num)
    decimal_places = 0
    if ("e-" in num_str):
        decimal_places = int(num_str.split("e-")[1])
    else:
        decimal_places = len(num_str.split(".")[1]) if "." in num_str else 0

    return decimal_places


def truncate(num: float, digits: int) -> float:
    num_decimals = len(str(num).split(".")[1])
    if num_decimals <= digits:
        return num

    multiplier = 10.0 ** digits

    return math.trunc(multiplier*num) / multiplier


        
     