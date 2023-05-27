import logging
import os
import queue
import sys
import datetime
import threading

from config import Config as cfg


class UniqueFilter(logging.Filter):
    def __init__(self):
        self.last_log = None

    def filter(self, record):
        msg = record.getMessage()
        if msg == self.last_log:
            return False
        self.last_log = msg
        return True


class LogWriterThread(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue
        self.daemon = True

    def run(self):
        while True:
            record = self.queue.get()
            if record is None:
                break
            self.handle(record)

    def handle(self, record):
        logger = logging.getLogger(record.name)
        logger.handle(record)


class LevelFileHandler(logging.FileHandler):
    def __init__(self, filename, mode='a', encoding=None, delay=False):
        super().__init__(filename, mode=mode, encoding=encoding, delay=delay)

    def emit(self, record):
        if record.levelno == logging.DEBUG:
            self.baseFilename = self.baseFilename.replace('.log', '_debug.log')
        elif record.levelno == logging.INFO:
            self.baseFilename = self.baseFilename.replace('.log', '_info.log')
        elif record.levelno == logging.WARNING:
            self.baseFilename = self.baseFilename.replace('.log', '_warning.log')
        elif record.levelno == logging.ERROR:
            self.baseFilename = self.baseFilename.replace('.log', '_error.log')
        elif record.levelno == logging.CRITICAL:
            self.baseFilename = self.baseFilename.replace('.log', '_critical.log')
        super().emit(record)
        self.flush()


class ColorFormatter(logging.Formatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Define color codes
        self.RED = '\033[91m'
        self.YELLOW = '\033[93m'
        self.GREEN = '\033[92m'
        self.CYAN = '\033[96m'
        self.END = '\033[0m'

    def format(self, record):
        # Apply color to log level
        if record.levelno == logging.DEBUG:
            levelname = self.GREEN + 'DEBUG' + self.END
        elif record.levelno == logging.INFO:
            levelname = self.CYAN + 'INFO' + self.END
        elif record.levelno == logging.WARNING:
            levelname = self.YELLOW + 'WARNING' + self.END
        elif record.levelno == logging.ERROR:
            levelname = self.RED + 'ERROR' + self.END
        elif record.levelno == logging.CRITICAL:
            levelname = self.RED + 'CRITICAL' + self.END
        else:
            levelname = record.levelname

        # Format log message with color
        record.levelname = levelname
        return super().format(record)


def setup_logging(log_dir='logs', log_level=logging.INFO, logger_name=None):
    # Create a logger and set its level
    logger = logging.getLogger(logger_name or __name__)
    logger.setLevel(log_level)

    # Create a directory for the logs with the current date and time
    now = datetime.datetime.now()
    log_subdir = now.strftime('%d-%m-%y')
    log_path = os.path.join(log_subdir, log_dir)
    os.makedirs(log_path, exist_ok=True)

    # Create a queue and a log writer thread
    log_queue = queue.Queue()
    log_writer = LogWriterThread(log_queue)
    log_writer.start()

    # Create a file handler and set its level
    log_file = now.strftime('%H-%M-%S.log')
    log_path = os.path.join(log_path, log_file)
    file_handler = LevelFileHandler(log_path)
    file_handler.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Create a console handler and set its level
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)

    # Create a color formatter for the console handler
    formatter = ColorFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # Add the console handler to the logger
    logger.addHandler(console_handler)

    # Add the UniqueFilter to the console handler
    console_handler.addFilter(UniqueFilter())

    return logger


mylogger = setup_logging(log_dir='logs', log_level=logging.INFO, logger_name=cfg.LOGGER_NAME)
