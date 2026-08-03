# Automation Supervisor

## Description

Automation Supervisor is a Python application designed to communicate with industrial automation systems. 
The project aims to monitor PLC data through OPC UA communication.

## Current status
The project is currently under development.

Implemented features:

- Configuration management
- Startup service
- Centralized logging
- Unit testing (pytest)
- Domain model (Equipment)
- Equipment service
- External equipment configuration introduced
- Configuration service created
- YAML configuration supported

## Project structure

```text

AutomationSupervisor/
|
|__.venv
|__config/
|    |__ __init__.py
|    |__equipment.yaml
|    |__settings.py
|__docs
|    |__adr
|__domain
|    |__ __init__.py
|    |__equipment.py
|__services
|    |__ __init__.py
|    |__configuration_service.py
|    |__equipment_service.py
|    |__startup.py
|__tests
|    |__ __init__.py
|    |__test_startup.py
|    |__test_equipment_service.py
|__.gitignore
|__logging_config.py
|__main.py
|__README.md
|__requirements.txt

```

### Description

- main.py : Entry point of the application
- config/settings.py : Centralized application configuration
- domain/equipment.py : Domain entity representing industrial equipment
- services/equipment_service.py : Equipment-related business operations
- services/startup.py : Startup-related initialization
- tests/test_equipment_service.py: Unit tests for equipment services
- logging_config.py : Centralized logging configuration
- requirements.txt : Python project dependencies


## Documentation
Architecture decisions are documented using ADRs.

Available decisions:
- ADR 001 - Separate logging configuration from application settings

## Technologies

- Python
- pytest
- OPC UA (planned)
- Git / GitHub

## Configuration
The application configuration is currently stored in: config/settings.py

Current parameters include:

- Application name
- PLC IP address
- OPC UA port

## How to run
Create and activate the virtual environment : python -m venv .venv

Install dependencies : pip install -r requirements.txt

Run the application : python main.py

## Testing

Run all unit tests : pytest

Run a specific test file : pytest tests/test_startup.py
