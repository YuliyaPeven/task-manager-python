# Task Manager (Python + SQLite)

Task Manager is a simple console application for creating and managing tasks.  
The project demonstrates work with a relational database, CRUD operations, and basic application architecture in Python.

## Features
- Add new tasks  
- View all tasks  
- Update task status  
- Delete tasks  
- Persistent storage using SQLite  

## Technologies
- Python 3  
- SQLite3  
- Dataclasses  
- Modular project structure  

## Project Structure
task_manager/
├── main.py # Entry point, user interface
├── database.py # DB connection and initialization
├── services.py # Business logic (CRUD)
├── models.py # Task model
└── requirements.txt


## How to Run
### 1. Create virtual environment
python -m venv venv
### 2. Activate environment  
Windows:
venv\Scripts\activate

### 3. Run the program
python main.py

The database file `tasks.db` will be created automatically if it doesn't exist.

## Future Improvements
- Deadlines for tasks  
- Filtering by status  
- Search by task title  
- Export to CSV  
- GUI version  

## About the Author
Created by **Yuliya Peven** as part of a portfolio for Junior Software Engineer positions.  
GitHub: https://github.com/YuliyaPeven
