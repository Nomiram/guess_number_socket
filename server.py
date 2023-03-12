'''
Server, that accept string "GUESS <int>" at socket and returns "MORE", "LESS" or "EQUAL"
'''
import random
import socket
from typing import Type, Union

HOST = '0.0.0.0'
PORT = 5555


def generate_number(a=1, b=100) -> int:
    """generate random int from a to b

    Args:
        a (int, optional): from. Defaults to 1.
        b (int, optional): to. Defaults to 100.

    Returns:
        int: random number
    """
    return random.randint(a, b)


def handle_guess(number: int, guess: int):
    """check if guess equal number

    Args:
        number (int): generated number
        guess (int): guess number

    Returns:
        str: MORE, LESS or EQUAL
    """
    if guess < number:
        return 'MORE'
    elif guess > number:
        return 'LESS'
    else:
        return 'EQUAL'


def handle_command(command: str, number: int) -> Union[str, Type[None]]:
    """Handling accepted connection

    Args:
        command (str): command
        number (int): generated number

    Returns:
        str or None: MORE, LESS, EQUAL or None
    """
    parts = command.split(' ')
    if len(parts) < 2:
        return None
    if parts[0] == 'GUESS':
        guess = int(parts[1])
        return handle_guess(number, guess)
    # else:
    return None


def run_server(host: str, port: int):
    """Simple socket server, that accept string "GUESS <int>" at socket
    and returns "MORE", "LESS" or "EQUAL"

    Args:
        host (str): host to bind
        port (int): port to bind
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        number = generate_number()
        print(f'Сервер запущен на порту {port}')
        conn, addr = s.accept()
        with conn:
            print(f'Подключен клиент {addr}')
            while True:
                data = conn.recv(1024).decode().strip()
                if not data:
                    break
                result = handle_command(data, number)
                conn.sendall(result.encode())
            print(f'Клиент {addr} отключился')


if __name__ == '__main__':
    run_server(HOST, PORT)
