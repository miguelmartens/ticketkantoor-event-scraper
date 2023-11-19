import logging
import os

def configure_logging():
    """
    Configures the global logging settings for the application.

    The logging level and format can be customized via environment variables.
    The default logging level is set to INFO if not specified.
    """
    log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Additional configuration can be added here, such as file handlers or loggers for specific libraries.
