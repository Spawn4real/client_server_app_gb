"""ОБЩИЕ ФУНКЦИИ"""

import json
from common.variables import MAX_PACKAGES_LEN, ENCODING
import sys
sys.path.append('../')
from common.decos import log


# Фуннкция приема и декодирования сообщения. Принимает байты и выдает словарь, иначе возращает ValueError
@log
def get_message(client):
    encoding_response = client.recv(MAX_PACKAGES_LEN)
    json_response = encoding_response.decode(ENCODING)
    response = json.loads(json_response)
    if isinstance(response, dict):
        return response
    else:
        raise TypeError

# Функция отправки сообщения и кодирования. Принимает в себя словарь, если нет выводит TypeError,
# получает из него строку, переводит в байты и отправляет.
@log
def send_message(sock, message):
    js_message = json.dumps(message)
    encoding_message = js_message.encode(ENCODING)
    sock.send(encoding_message)

