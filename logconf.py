# -*- coding: utf-8 -*-
"""Backend settings."""
from colorlog import ColoredFormatter
import logging


class Logger:
    """Basic logging configuration."""

    def __init__(self, logger_name):
        """init."""
        formatter = ColoredFormatter(
            '%(log_color)s%(levelname)-5s%(reset)s '
            '%(yellow)s[%(asctime)s]%(reset)s%(white)s '
            '%(name)s %(funcName)s %(bold_purple)s:%(lineno)d%(reset)s '
            '%(log_color)s%(message)s%(reset)s',
            datefmt='%y-%m-%d %H:%M:%S',
            log_colors={
                'DEBUG': 'blue',
                'INFO': 'bold_cyan',
                'WARNING': 'red,',
                'ERROR': 'bg_bold_red',
                'CRITICAL': 'red,bg_white',
            }
        )

        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)

        # StreamHandler
        sh = logging.StreamHandler()
        sh.setLevel(logging.DEBUG)
        sh.setFormatter(formatter)

        # Add handlers
        logger.addHandler(sh)

        self.logger = logger

    def __getattr__(self, name):  # noqa
        return getattr(self.logger, name)
