"""ОБЩИЕ ФУНКЦИИ"""

import json
from common.variables import MAX_PACKAGES_LEN, ENCODING
import sys
sys.path.append('../')
from common.decos import log


@log
def get_message(client):
    """
       Функция приёма сообщений от удалённых компьютеров.
       Принимает сообщения JSON, декодирует полученное сообщение
       и проверяет что получен словарь.
       :param client: сокет для передачи данных.
       :return: словарь - сообщение.
    """
    encoding_response = client.recv(MAX_PACKAGES_LEN)
    json_response = encoding_response.decode(ENCODING)
    response = json.loads(json_response)
    if isinstance(response, dict):
        return response
    else:
        raise TypeError


@log
def send_message(sock, message):
    """
        Функция отправки словарей через сокет.
        Кодирует словарь в формат JSON и отправляет через сокет.
        :param sock: сокет для передачи
        :param message: словарь для передачи
        :return: ничего не возвращает
    """
    js_message = json.dumps(message)
    encoding_message = js_message.encode(ENCODING)
    sock.send(encoding_message)

