'''
Simple client to send guess number to server
'''
import socket

HOST = 'localhost'
PORT = 5555


def read_input() -> int:
    """read int from input

    Returns:
        int: number
    """
    while True:
        try:
            guess = int(input('Введите число: '))
            return guess
        except ValueError:
            print('Введите целое число')


def run_client():
    """Simple tcp client: send "GUESS <int>" and recv result
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print('Подключение к серверу')
        while True:
            guess = read_input()
            s.sendall(f'GUESS {guess}'.encode())
            data = s.recv(1024).decode().strip()
            print(data)
            if data == 'EQUAL':
                break


if __name__ == '__main__':
    run_client()
