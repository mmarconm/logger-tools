import os
import logging
import inspect
from datetime import datetime
from functools import wraps
from logger_tools import settings


class Logger:
    _logger = None

    def __init__(self, logger_name=None):
        self.logger_name = logger_name or settings.LOGGER_NAME

    def get_logger(self):
        if Logger._logger is None:
            Logger._logger = logging.getLogger(self.logger_name)
            Logger._logger.setLevel(getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO))

            log_path = settings.LOG_FILE_PATH
            log_dir = os.path.dirname(log_path)

            # ✅ Cria diretório apenas se for fornecido
            if log_dir:
                os.makedirs(log_dir, exist_ok=True)

            file_handler = logging.FileHandler(log_path, mode="a", encoding="utf-8")
            formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            file_handler.setFormatter(formatter)

            # ✅ Evita adicionar múltiplos handlers
            if not Logger._logger.hasHandlers():
                Logger._logger.addHandler(file_handler)

        return Logger._logger

    def log(self, name, message, info_message="", level="info"):
        stack = inspect.stack()
        calling_function = stack[1].function
        log_message = f"{datetime.now()} - {name}.{calling_function} - {message}"
        if info_message:
            log_message += f" - {info_message}"

        logger = self.get_logger()
        getattr(logger, level, logger.info)(log_message)

    def inspect_function(self, message, level="info"):
        stack = inspect.stack()
        try:
            current_function = stack[1].function
            calling_function = stack[2].function
            filename = stack[2].filename.split('/')[-1]
        except IndexError:
            current_function = calling_function = filename = 'Unknown'

        log_message = (
            f"[{datetime.now():%Y-%m-%d %H:%M:%S}] "
            f"{filename}::{calling_function} → {current_function} | {message}"
        )
        getattr(self.get_logger(), level)(log_message)



def log_function_call(_func=None, *, level="info", logger_name=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger = Logger()

            stack = inspect.stack()
            try:
                current_function = stack[1].function
                calling_function = stack[2].function
                filename = stack[2].filename.split('/')[-1]
            except IndexError:
                current_function = calling_function = filename = 'Unknown'

            log_message = (
                f"[{datetime.now():%Y-%m-%d %H:%M:%S}] "
                f"{filename}::{calling_function} → {current_function}"
            )
            getattr(logger.get_logger(), level)(log_message)

            return func(*args, **kwargs)
        return wrapper

    return decorator if _func is None else decorator(_func)

