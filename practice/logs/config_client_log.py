import logging
import sys
import os
sys.path.append('../')
from common.variables import LOGGING_LEVEL


client_formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')


path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(path, 'client.log')

stream_handler = logging.StreamHandler(sys.stderr)
stream_handler.setFormatter(client_formatter)
stream_handler.setLevel(logging.ERROR)
log_file = logging.FileHandler(path, encoding='utf8')
log_file.setFormatter(client_formatter)


logger = logging.getLogger('client')
logger.addHandler(stream_handler)
logger.addHandler(log_file)
logger.setLevel(LOGGING_LEVEL)


if __name__ == '__main__':
    logger.critical('Critical error')
    logger.error('Error')
    logger.debug('Debug info')
    logger.info('Info message')

