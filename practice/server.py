"""СЕРВЕРНАЯ ЧАСТЬ"""

import sys
import json
import socket
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR, \
    DEFAULT_PORT, MAX_CONNECTIONS
from common.utils import send_messages, get_messages


def process_client_message(message):
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and USER in message \
            and message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return f'400 : {message[ERROR]}'


def main():
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = DEFAULT_PORT
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        print("После параметра -\'p\' - необходимо указать порт.")
        sys.exit(1)
    except ValueError:
        print('Номер порта может быть только в диапозоне от 1024 жл 65535')
        sys.exit(1)

    try:
        if '-a' in sys.argv:
            listen_adress = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_adress = ''
    except IndexError:
        print('После параметра -\'a\' необходимо указать адрес, который будет слушать сервер.')
        sys.exit(1)

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    transport.bind((listen_adress, listen_port))

    transport.listen(MAX_CONNECTIONS)

    while True:
        client, client_adress = transport.accept()
        try:
            message_from_client = get_messages(client)
            print(message_from_client)
            response = process_client_message(message_from_client)
            send_messages(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('Принято некорректное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    main()

