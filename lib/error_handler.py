# Creating a logger
import logging
import sys

logger = logging.getLogger(__name__)
# Logging file must be in C:\tmp\remote-controller-errors.log
logging.basicConfig(filename="C:\\tmp\\remote-controller-errors.log", level=logging.DEBUG)


# Creating a handler
def handle_unhandled_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        # Will call default excepthook
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
        # Create a critical level log message with info from the except hook.
    logger.critical("Unhandled exception", exc_info=(exc_type, exc_value, exc_traceback))


# Assign the excepthook to the handler
sys.excepthook = handle_unhandled_exception
