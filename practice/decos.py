"""Декораторы"""

import sys
import logging
import logs.config_server_log
import logs.config_client_log
import traceback
import inspect


def log(func_to_log):
    def log_saver(*args, **kwargs):
        logger_name = 'server' if 'server.py' in sys.argv[0] else 'client'
        logger = logging.getLogger(logger_name)

        ret = func_to_log(*args, **kwargs)
        logger.debug(f'Была вызвана функция {func_to_log.__name__} с параметрами {args}, {kwargs}. '
                     f'Вызов из модуля {func_to_log.__module__}.')
        return ret
    return log_saver
