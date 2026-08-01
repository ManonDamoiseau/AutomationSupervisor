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

```text

AutomationSupervisor/
|
|__.venv
|__config/
|    |__ __init__.py
|    |__settings.py
|__docs
|    |__adr
|__services
|    |__ __init__.py
|    |__startup.py
|__.gitignore
|__logging_config.py
|__main.py
|__README.md
|__requirements.txt

```

### Description

- main.py : Entry point of the application
- config/settings.py : Centralized application configuration
- services/startup.py : Startup-related functions

## Documentation
Architecture decisions are documented using ADRs.

Available decisions:
- ADR 001 - Separate logging configuration from application settings

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