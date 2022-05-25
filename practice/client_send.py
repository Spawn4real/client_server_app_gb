"""КЛИЕНТСКАЯ ЧАСТЬ"""

import argparse
import json
import logging
import socket
import sys
import time

from common.utils import send_message, get_message
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR, DEFAULT_IP, DEFAULT_PORT, \
    SENDER, MESSAGE, MESSAGE_TEXT

from decos import log
from errors import ReqFieldMissingError, ServerError

logger = logging.getLogger('client')


@log
def message_from_server(message):
    if ACTION in message and message[ACTION] == MESSAGE and SENDER in message and MESSAGE_TEXT in message:
        print(f'Получено сообщение от пользователя {message[SENDER]}:{message[MESSAGE_TEXT]}')
        logger.info(f'Получено сообщение от пользователя {message[SENDER]}:{message[MESSAGE_TEXT]}')
    else:
        logger.error(f'Получено сообщение от пользователя {message[SENDER]}:{message[MESSAGE_TEXT]}')


def create_message(sock, account_name='Guest'):
    message = input('Введите сообщение для отправки или \'!!!\' для завершения работы: ')
    if message == '!!!':
        sock.close()
        logger.info('Завершение работы по команде пользователя.')
        print('Спасибо что пользуетесь нашим сервисом')
        sys.exit(0)
    message_dict = {
        ACTION: MESSAGE,
        TIME: time.time(),
        ACCOUNT_NAME: account_name,
        MESSAGE_TEXT: message
    }

    logger.debug(f'Сформировано словарь сообщения: {message_dict}')
    return message_dict


@log
def create_presence(account_name='Guest'):
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
                ACCOUNT_NAME: account_name,
            },
    }
    logger.debug(f'Сформировано {PRESENCE} сообщение для пользователя {account_name}')
    return out


@log
def procces_response_ans(message):
    logger.debug(f'Разбор приветсвенного сообщения от сервера: {message}')
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        elif message[RESPONSE] == 400:
            raise ServerError(f'400 : {message[ERROR]}')
    raise ReqFieldMissingError(RESPONSE)


@log
def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', default=DEFAULT_IP, nargs='?')
    parser.add_argument('port', default=DEFAULT_PORT, type=int, nargs='?')
    parser.add_argument('-m', '--mode', default='send', nargs='?')
    namespace = parser.parse_args(sys.argv[1:])
    server_address = namespace.addr
    server_port = namespace.port
    client_mode = namespace.mode

    # проверим подходящий номер порта
    if not 1023 < server_port < 65536:
        logger.critical(
            f'Попытка запуска клиента с неподходящим номером порта: {server_port}.'
            f' Допустимы адреса с 1024 до 65535. Клиент завершается.')
        sys.exit(1)

    logger.info(f'Запущен клиент с парамертами: '
                f'адрес сервера: {server_address}, порт: {server_port}')

    if client_mode not in ('listen', 'send'):
        logger.critical(
            f'Указан недопустимый режим работы: {client_mode}.'
            f' Допустимые режимы: listen, send.')
        sys.exit(1)
    return server_address, server_port, client_mode


@log
def main():
    server_address, server_port, client_mode = arg_parser()

    logger.info(
        f'Запущен клиент с параметрами: адрес сервера: {server_address}, порт: {server_port}, '
        f'режим работы: {client_mode}'
    )
    # Инициализация сокета и обмен
    try:
        transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        transport.connect((server_address, server_port))
        send_message(transport, create_presence())
        answer = procces_response_ans(get_message(transport))
        logger.info(f'Установлено соеденение с сервером. Ответ сервера: {answer}')
        print('Установлено соеденение с сервером.')
    except json.JSONDecodeError:
        logger.error('Не удалось декодировать полученную Json строку.')
        sys.exit(1)
    except ServerError as error:
        logger.error(f'При установке соединения сервер вернул ошибку: {error.text}')
    except ReqFieldMissingError as missing_error:
        logger.error(f'В ответе сервера отсутствует необходимое поле '
                            f'{missing_error.missing_field}')
        sys.exit(1)
    except ConnectionRefusedError:
        logger.critical(f'Не удалось подключиться к серверу {server_address}:{server_port}, '
                               f'конечный компьютер отверг запрос на подключение.')
        sys.exit(1)
    else:
        if client_mode == 'send':
            print('Режим работы - отправка сообщений.')
        else:
            print('Режим работы - приём сообщений.')
        while True:
            if client_mode == 'send':
                try:
                    send_message(transport, create_message(transport))
                except (ConnectionResetError, ConnectionError, ConnectionAbortedError):
                    logger.error(f'Соединение с сервером {server_address} было потерено. ')
                    sys.exit(1)

            if client_mode == 'listen':
                try:
                    message_from_server(get_message(transport))
                except (ConnectionResetError, ConnectionError, ConnectionAbortedError):
                    logger.error(f'Соединение с сервером {server_address} было потерено. ')
                    sys.exit(1)


if __name__ == '__main__':
    main()