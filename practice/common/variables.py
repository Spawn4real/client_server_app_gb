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
SERVER_CONFIG = 'serever_dist+++.ini'

ACTION = 'action'

PRESENCE = 'presence'

TIME = 'time'

USER = 'user'

ACCOUNT_NAME = 'account_name'

SENDER = 'sender'

DESTINATION = 'to'

DATA = 'bin'

PUBLIC_KEY = 'pubkey'

RESPONSE = 'responce'

ERROR = 'error'

MESSAGE = 'message'

MESSAGE_TEXT = 'message_text'

EXIT = 'exit'

GET_CONTACTS = 'get_contacts'

LIST_INFO = 'data_list'

REMOVE_CONTACT = 'remove'

ADD_CONTACT = 'add'

USERS_REQUEST = 'get_users'

PUBLIC_KEY_REQUEST = 'pubkey_need'



RESPONSE_200 = {
    RESPONSE: 200
}

RESPONSE_202 = {
    RESPONSE: 202,
    LIST_INFO: None
}

RESPONSE_400 = {
    RESPONSE: 400,
    ERROR: None
}

RESPONSE_205 = {
    RESPONSE: 205,
}

RESPONSE_511 = {
    RESPONSE: 511,
    DATA: None
}