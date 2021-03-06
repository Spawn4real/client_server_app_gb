"""ОБЩИЕ ФУНКЦИИ"""

import json
from common.variables import MAX_PACKAGES_LEN, ENCODING
import sys
sys.path.append('../')
from errors import IncorrectDataRecivedError, NonDictInputError
from decos import log


# Фуннкция приема и декодирования сообщения. Принимает байты и выдает словарь, иначе возращает ValueError
@log
def get_message(client):
    encoding_response = client.recv(MAX_PACKAGES_LEN)
    if isinstance(encoding_response, bytes):
        json_response = encoding_response.decode(ENCODING)
        if isinstance(json_response, str):
            response = json.loads(json_response)
            if isinstance(response, dict):
                return response
            raise IncorrectDataRecivedError
        raise IncorrectDataRecivedError
    raise IncorrectDataRecivedError


# Функция отправки сообщения и кодирования. Принимает в себя словарь, если нет выводит TypeError,
# получает из него строку, переводит в байты и отправляет.
@log
def send_message(sock, message):
    if not isinstance(message, dict):
        raise NonDictInputError
    js_message = json.dumps(message)
    encoding_message = js_message.encode(ENCODING)
    sock.send(encoding_message)

