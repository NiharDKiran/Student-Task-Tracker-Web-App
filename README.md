# Student Task Tracker

A simple, lightweight web application built with Python (Flask) and HTML/CSS to help keep track of student tasks and their completion status. It features an aesthetic UI and allows adding tasks with a "Pending" or "Completed" status.

## Prerequisites

- **Python 3.x**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

## Setup & Installation

1. Open a terminal or command prompt.
2. Navigate to the project root directory (`Project`).
3. Install the required dependency, **Flask**:
   ```bash
   pip install flask
   ```

## Folder Structure

```
Project/
├── Backend/
│   └── app.py         # Main Flask server
├── Frontend/
│   └── index.html     # Frontend UI and Template
└── README.md
```

## How to Run

1. Open your terminal or command prompt.
2. Navigate into the `Backend` directory:
   ```bash
   cd Backend
   ```
3. Run the Flask application:
   ```bash
   python app.py
   ```
4. Once the server is running, you will see an output like `* Running on http://127.0.0.1:5000`.
5. Open your web browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Features
- Add student names and task descriptions.
- Set statuses to either "Pending" or "Completed".
- View the entire list in an organized, beautiful data table.
- Informative success/error alerts upon submission.
