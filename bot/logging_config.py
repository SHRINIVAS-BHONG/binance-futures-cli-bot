import logging
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "trading_bot.log")

os.makedirs(LOG_DIR, exist_ok=True)

def setup_logging():
    """
    Configure logging so that:
    - All logs go ONLY to a file
    - No logs appear in the console
    - Existing handlers (including from third-party libs) are removed
    """

    # Get the root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # Remove ALL existing handlers (very important)
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)

    # Create file-only handler
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    file_handler.setFormatter(formatter)

    # Attach only the file handler
    root_logger.addHandler(file_handler)
