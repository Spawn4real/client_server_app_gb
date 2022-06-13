"""ПЕРЕМЕННЫЕ ПО УМОЛЧАНИЮ"""

# Порт по умолчанию
import logging

DEFAULT_PORT = 7777
# IP Адрес по умолчанию для клиента
DEFAULT_IP = '127.0.0.1'
# Максимальное количество подключений
MAX_CONNECTIONS = 10
# Максимальная длинна байтового сообщения
MAX_PACKAGES_LEN = 1024
# Кодировка
ENCODING = 'utf-8'
# Уровень логгирования
LOGGING_LEVEL = logging.DEBUG
# База данных для хранения данных сервера:
SERVER_DATABASE = 'sqlite:///server_base.db3'
#


ACTION = 'action'

PRESENCE = 'presence'

TIME = 'time'

USER = 'user'

ACCOUNT_NAME = 'account_name'

SENDER = 'sender'

DESTINATION = 'to'

RESPONSE = 'responce'

ERROR = 'error'

MESSAGE = 'message'

MESSAGE_TEXT = 'message_text'

EXIT = 'exit'
