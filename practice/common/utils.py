"""ОБЩИЕ ФУНКЦИИ"""

import json
from variables import MAX_PACKAGES_LEN, ENCODING


# Фуннкция приема и декодирования сообщения. Принимает байты и выдает словарь, иначе возращает ValueError
def get_messages(client):
    encoding_response = client.recv(MAX_PACKAGES_LEN)
    if isinstance(encoding_response, bytes):
        json_response = encoding_response.decode(ENCODING)
        if isinstance(json_response, str):
            response = json.loads(json_response)
            if isinstance(response, dict):
                return response
            raise ValueError
        raise ValueError
    raise ValueError


# Функция отправки сообщения и кодирования. Принимает в себя словарь, если нет выводит TypeError,
# получает из него строку, переводит в байты и отправляет.
def send_messages(sock, message):
    if not isinstance(message, dict):
        raise TypeError
    js_message = json.dumps(message)
    encoding_messege = js_message.encode(ENCODING)
    sock.send(encoding_messege)

