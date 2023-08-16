from datetime import datetime
from socket import *

file = open("../q3/client_log.txt", "a")


def main():
    host = "localhost"
    server_port = 8888
    server_address = (host, server_port)

    # make client socket and connect to server
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(server_address)

    while True:
        # get input and if its start, get 3 other messages and send to server to receive result
        message = input()
        if message == 'start':
            client_socket.send(message.encode())
            log(True, datetime.now(), server_port, message)
            ok = client_socket.recv(200).decode()
            log(False, datetime.now(), server_port, ok)

            # get first operand and send it to server, if the response is ok, means that the format is right,
            # if not ok print response text and go to next step, waiting for another start or exit
            operand1 = input()
            client_socket.send(operand1.encode())
            if operand1 == "exit":
                break
            log(True, datetime.now(), server_port, operand1)
            response1 = client_socket.recv(200).decode()
            log(False, datetime.now(), server_port, response1)
            if response1 != "ok":
                print(response1)
                continue

            # get operator and send it to server, if the response is ok, means that the format is right,
            # if not ok print response text and go to next step, waiting for another start or exit
            operator0 = input()
            client_socket.send(operator0.encode())
            if operator0 == "exit":
                break
            log(True, datetime.now(), server_port, operator0)
            response2 = client_socket.recv(200).decode()
            log(False, datetime.now(), server_port, response2)
            if response2 != "ok":
                print(response2)
                continue

            # get second operand and send it to server, if the response is ok, means that the format is right,
            # if not ok print response text and go to next step, waiting for another start or exit
            operand2 = input()
            client_socket.send(operand2.encode())
            if operand2 == "exit":
                break
            log(True, datetime.now(), server_port, operand2)
            response3 = client_socket.recv(200).decode()
            log(False, datetime.now(), server_port, response3)
            if response3 != "ok":
                print(response3)
                continue

            # receive result from server and print
            result = client_socket.recv(200).decode()
            log(False, datetime.now(), server_port, result)
            print(result)

        elif message == "exit":
            # if message is exit, send to server to close itself and break the loop
            client_socket.send(message.encode())
            log(True, datetime.now(), server_port, message)
            break
    file.close()
    # close socket
    client_socket.close()


def log(send, born_time, port, message):
    if send:
        file.write(str(born_time) + " sending message : " + message + ", to port : " + str(port) + "\n \r")
    else:
        file.write(str(born_time) + " receiving message : " + message + ", from port : " + str(port) + "\n \r")


if __name__ == '__main__':
    main();
