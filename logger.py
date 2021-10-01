import logging
from logging.handlers import RotatingFileHandler
import sys
import os

APP_LOG_FILE = "debug.log"
ERROR_LOG_FILE = "error.log"
MESSAGE_FORMAT = "%(name)s: %(message)s"

# This is just so we don't get some stupid errors when trying to read files that don't exist. Why it doesn't check if the files exist upon creation, is beyond me.
if not os.path.isdir("logs"):
	os.mkdir("logs")
open(f"logs/{APP_LOG_FILE}", "a").close()
open(f"logs/{ERROR_LOG_FILE}", "a").close()

formatter = logging.Formatter(MESSAGE_FORMAT)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

app_handler = RotatingFileHandler(f"logs/{APP_LOG_FILE}", mode="w", encoding="utf-8")
app_handler.setFormatter(formatter)
app_handler.setLevel(logging.DEBUG)
logger.addHandler(app_handler)

error_handler = logging.FileHandler(f"logs/{ERROR_LOG_FILE}", mode="w", encoding="utf-8")
error_handler.setFormatter(formatter)
error_handler.setLevel(logging.ERROR)
logger.addHandler(error_handler)

def handle_exception(exc_type, exc_value, exc_traceback):
	if issubclass(exc_type, KeyboardInterrupt):
		sys.__excepthook__(exc_type, exc_value, exc_traceback)
		return
	logger.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = handle_exception
