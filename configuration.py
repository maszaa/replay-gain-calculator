import datetime
import logging
import sys

PYTHON3_PATH = "/usr/bin/python3"
REGAINER_PATH = "/usr/bin/regainer.py"

ALLOWED_EXTENSIONS = [".flac"]

MODIFICATION_DATETIME_DELTA = datetime.timedelta(days=5)
MODIFICATION_DATETIME_THRESHOLD = datetime.datetime.now() - MODIFICATION_DATETIME_DELTA

LOGGER_NAME = "replay-gain-calculator"
LOG_FORMAT = "[%(asctime)-15s: %(levelname)s/%(funcName)s] %(message)s"
LOG_FORMATTER = logging.Formatter(LOG_FORMAT)

LOGGER = logging.getLogger(LOGGER_NAME)
LOGGER.setLevel(logging.DEBUG)

STDOUT_HANDLER = logging.StreamHandler(sys.stdout)
STDOUT_HANDLER.setFormatter(LOG_FORMATTER)
LOGGER.addHandler(STDOUT_HANDLER)

STDERR_HANDLER = logging.StreamHandler(sys.stderr)
STDERR_HANDLER.setFormatter(LOG_FORMATTER)
STDERR_HANDLER.setLevel(logging.ERROR)
LOGGER.addHandler(STDERR_HANDLER)

try:
  from local_configuration import *
except ModuleNotFoundError:
  pass
