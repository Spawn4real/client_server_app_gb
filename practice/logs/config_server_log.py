import sys
import os
import logging
import logging.handlers
from common.variables import LOGGING_LEVEL
sys.path.append('../')

server_formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')


path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(path, 'server.log')

stream_handler = logging.StreamHandler(sys.stderr)
stream_handler.setFormatter(server_formatter)
stream_handler.setLevel(logging.ERROR)
log_file = logging.handlers.TimedRotatingFileHandler(path, encoding='utf8', interval=1, when='D')
log_file.setFormatter(server_formatter)


logger = logging.getLogger('server')
logger.addHandler(stream_handler)
logger.addHandler(log_file)
logger.setLevel(LOGGING_LEVEL)


if __name__ == '__main__':
    logger.critical('Critical error')
    logger.error('Error')
    logger.debug('Debug info')
    logger.info('Info message')