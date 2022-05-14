"""КЛИЕНТСКАЯ ЧАСТЬ"""

import sys
import json
import socket
import time
from practice.common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR, DEFAULT_IP, DEFAULT_PORT
from practice.common.utils import send_messages, get_messages


def create_presense(account_name='Guest'):
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        },
    }
    return out


def procces_ans(message):
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError


def main():
    try:
        server_adress = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_adress = DEFAULT_IP
        server_port = DEFAULT_PORT
    except ValueError:
        print('Портом может быть только число в диапозоне от 1024 до 65535')
        sys.exit(1)

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((server_adress, server_port))
    message_to_server = create_presense()
    send_messages(transport, message_to_server)
    try:
        answer = procces_ans((get_messages(transport)))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print("Не удалось декодировать сообщение")


if __name__ == '__main__':
    main()