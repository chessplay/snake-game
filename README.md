# Full-Stack Snake Game

This is a web-based, full-stack version of the classic Snake game. It features a Python Flask backend and a Vue.js frontend.

## Features

- Classic snake gameplay implemented with HTML5 Canvas.
- User authentication (registration and login).
- A persistent database (SQLite) to store user accounts and scores.
- A leaderboard to display the top 10 scores.

## Project Structure

```
.
├── backend/
│   ├── venv/                 # Python virtual environment
│   ├── app.py                # Flask application, API endpoints
│   ├── models.py             # SQLAlchemy database models
│   ├── requirements.txt      # Python dependencies
│   └── database.db           # SQLite database file
└── frontend/
    ├── node_modules/         # Node.js dependencies
    ├── src/
    │   ├── components/       # Vue components (Game, Login, etc.)
    │   ├── api.js            # Axios API service
    │   ├── main.js           # Vue app entry point
    │   ├── router.js         # Vue router configuration
    │   └── store.js          # Global state management
    ├── index.html            # Main HTML file
    └── package.json          # Frontend dependencies and scripts
```

## How to Run

You will need two separate terminal windows to run both the backend and frontend servers simultaneously.

### 1. Backend Setup

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```
2.  **Create and activate a Python virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    .\\venv\\Scripts\\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Initialize the database:**
    *(You only need to do this once.)*
    ```bash
    flask init-db
    ```
5.  **Start the Flask server:**
    ```bash
    flask run
    ```
    The backend will be running at `http://127.0.0.1:5000`.

### 2. Frontend Setup

1.  **Navigate to the frontend directory:**
    ```bash
    cd frontend
    ```
2.  **Install the dependencies:**
    ```bash
    npm install
    ```
3.  **Start the Vite development server:**
    ```bash
    npm run dev
    ```
    The frontend will be running at `http://127.0.0.1:5173` (or another port if 5173 is busy).

### 3. Play the Game

Open your web browser and navigate to the address provided by the frontend server (e.g., `http://127.0.0.1:5173`). You can register an account, log in, play the game, and see your high scores on the leaderboard! 