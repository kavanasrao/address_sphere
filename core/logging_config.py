import os
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

load_dotenv()

LOG_LEVEL = os.getenv("LOGINFO", 'INFO').upper()


logger = logging.getLogger(__name__)
logger.setLevel(getattr(logging, LOG_LEVEL, logging.INFO))


formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s |%(name)s | %(message)s ",
    datefmt= "%y-%m-%d %H:%M:%S"
)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)


file_handler = RotatingFileHandler("app.log",
                                   maxBytes = 5_00_000 ,
                                   backupCount= 3)

file_handler.setFormatter(formatter)


if not logger.hasHandlers():
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

logger.propagate = False