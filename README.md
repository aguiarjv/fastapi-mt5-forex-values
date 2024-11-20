# FastAPI - Meta Trader 5 point-to-dollar conversion web app

This project is the backend for a real-time financial data streaming system and a utility for Forex point-to-dollar conversion. It integrates with Meta Trader 5 (MT5) to fetch live data and calculate the value (in USD) of a specified number of points for any Forex symbol for a given number of lots. <br>
The backend also serves a precompiled React-based frontend, making it accessible immediately upon starting the server. The details of the frontend project can be checked [here](https://github.com/aguiarjv/react-mt5-forex-values).

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation and Setup](#installation-and-setup)
- [Frontend Integration](#frontend-integration)
- [Technologies Used](#technologies-used)
- [Screenshots](#screenshots)

---

## Features
- **Real-Time Data Fetching**: Fetches live trading data directly from Meta Trader 5.
- **Forex Point-to-Dollar Conversion**: Converts a given number of points to USD value for a specified Forex symbol for a given number of lots.
- **WebSocket Integration**: Streams live data to the frontend for real-time updates.
- **Built-in Frontend**: Automatically serves a React-based frontend from the root URL (```/```).


## Prerequisites
### Meta Trader 5
- Install Meta Trader 5.
- Ensure it is running before you start the application.
- Ensure you have an account connected to a trading server.

### Python Environment
- Python 3.8+
- Git
- Virtualenv

## Installation and Setup
1. Clone this repository:
    ```bash
    git clone https://github.com/aguiarjv/fastapi-mt5-forex-values
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Run the server:
    ```bash
    fastapi run app.py
    ```
6. Access the app at ```http://localhost:8000/```. You can add new symbols by clicking on the button "Add New Symbol". The symbol's name must match the symbols in the Meta Trader 5 terminal.

## Frontend Integration
The React-based frontend is precompiled and included in the ```frontend/dist``` folder. It is automatically served by the backend server. No additional setup is required.

If you make changes to the ```index.html``` or recompile the frontend, ensure all asset references include the ```/static/``` prefix to work correctly.

### Updating Frontend Assets
1. Replace the contents of the ```frontend/dist``` with the new build.
2. Update the ```index.html``` file:
    - Add ```/static/``` prefix to all references (e.g., CSS, JS).
    - Example change:
    ```html
    <!-- After building a new frontend -->
    <link href="/assets/style.css" rel="stylesheet">
    <script src="main.js"></script>
    ```
    ```html
    <!-- Adding the '/static/' prefix -->
    <link href="/static/assets/style.css" rel="stylesheet">
    <script src="/static/main.js"></script>
    ```
For more details about the frontend project or to build it yourself, visit the [frontend repository](https://github.com/aguiarjv/react-mt5-forex-values).

## Technologies Used
- **FastAPI**: For building the WebSocket server and serving the frontend.
- **Meta Trader 5 Python API**: For fetching financial data.
- **React.js**: For the user-friendly frontend interface.

## Screenshots
 
### Web App
![Web App](/screenshots/main-page.png?raw=true "Web App")

### Add New Symbol
![Add New Symbol](/screenshots/add-new-symbol.png?raw=true "Add New Symbol")