# Automation Supervisor

## Description

Automation Supervisor is a Python application designed to communicate with industrial automation systems. 
The project aims to monitor PLC data through OPC UA communication.

## Current status
The project is currently under development.

Implemented features:

- Python project structure
- Configuration management
- Git version control

## Project structure
AutomationSupervisor/

├── config/
│ ├── init.py
│ └── settings.py
│
├── main.py
│
└── README.md

## Technologies

- Python
- OPC UA (planned)
- Git / GitHub

## Configuration
The application configuration is currently stored in: config/settings.py

Current parameters include:

- Application name
- PLC IP address
- OPC UA port

## How to run
Create and activate the virtual environment: python -m venv .venv
Install dependencies: pip install -r requirements.txt
Run the application: python main.py