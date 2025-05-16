import os
import logging
import inspect
from datetime import datetime
from functools import wraps
from logger_tools import log_setup


class Logger:
    _logger = None

    def __init__(self, logger_name=None):
        self.logger_name = logger_name or log_setup.LOGGER_NAME

    def get_logger(self):
        if Logger._logger is None:
            Logger._logger = logging.getLogger(self.logger_name or "odoo_logger")
            Logger._logger.setLevel(getattr(logging, log_setup.LOG_LEVEL.upper(), logging.INFO))
            
            Logger._logger.handlers.clear()      # remove todos os handlers existentes
            Logger._logger.propagate = False     # bloqueia propagação pro root logger (terminal)

            log_path = log_setup.LOG_FILE_PATH
            log_dir = os.path.dirname(log_path)
            if log_dir:
                os.makedirs(log_dir, exist_ok=True)

            file_handler = logging.FileHandler(log_path, mode="a", encoding="utf-8")
            formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            file_handler.setFormatter(formatter)
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
        frame = inspect.currentframe()
        current_frame = frame.f_back  # quem chamou inspect_function
        caller_frame = (
            current_frame.f_back if current_frame else None
        )  # quem chamou a função

        current_function = current_frame.f_code.co_name if current_frame else "Unknown"
        calling_function = caller_frame.f_code.co_name if caller_frame else "Unknown"
        filename = (
            caller_frame.f_code.co_filename.split("/")[-1]
            if caller_frame
            else "Unknown"
        )

        timestamp = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
        log_message = f"[{timestamp}] {filename}::{calling_function} → {current_function} | {message}"

        getattr(self.get_logger(), level)(log_message)


def log_function_call(_func=None, *, level="info", logger_name=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger = Logger()
            frame = inspect.currentframe()
            decorated_func_frame = frame.f_back
            caller_frame = decorated_func_frame.f_back

            current_function = (
                decorated_func_frame.f_code.co_name
                if decorated_func_frame
                else "Unknown"
            )
            calling_function = (
                caller_frame.f_code.co_name if caller_frame else "Unknown"
            )
            filename = (
                caller_frame.f_code.co_filename.split("/")[-1]
                if caller_frame
                else "Unknown"
            )

            log_message = f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {filename}::{calling_function} → {current_function}"
            getattr(logger.get_logger(), level)(log_message)

            return func(*args, **kwargs)

        return wrapper

    return decorator if _func is None else decorator(_func)
