import logging
# Import Python's built-in logging module


def get_logger():
    # Function to create and return a logger object

    logging.basicConfig(
        filename="logs/test.log",
        # File where logs will be stored

        level=logging.INFO,
        # Logging level:
        # INFO → logs normal execution steps
        # (can also be DEBUG, ERROR, WARNING)

        format="%(asctime)s - %(levelname)s - %(message)s"
        # Format of log messages:
        # time - type - actual message
    )

    return logging.getLogger()
    # Returns logger instance which we can use in code