# ADR 001 - Separate logging configuration from application settings

## Status
Accepted

## Context
The Automation Supervisor application requires a logging system to provide traceability during operation and troubleshooting.

The project already contains an application configuration module (config/settings.py) responsible for functional parameters such as PLC connection settings.
But Logging configuration has a different purpose and represents technical infrastructure behavior, not functional configuration of the application.

## Decision
Created a dedicated logging configuration module.

## Reasons
- Application settings and logging settings have different responsibilities 
- Separating them improves maintainability
- Future changes to logging will not impact application parameters

The project will contain:

- config/settings.py for application configuration
- logging_config.py for logging infrastructure configuration