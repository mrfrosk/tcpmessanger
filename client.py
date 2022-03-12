import socket
import threading

name = input("Введите имя: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 3415))


def receive():
    while True:
        try:

            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(name.encode('utf-8'))
            else:
                print(message)
        except:
            print("Ошибка!")
            client.close()
            break


def write():
    while True:
        message = f"{name}: {input()}"
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
