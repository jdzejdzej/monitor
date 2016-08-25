This is a simple app for monitoring websites.
It's configurable by config.json.
Config should contain websites with their configurations.
Configurations of websites contains:
    condition - one of available bool functions in operations.py
    reference - reference string passed to condition
    timing - time interval between each request