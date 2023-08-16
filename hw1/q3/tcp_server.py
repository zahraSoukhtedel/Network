from datetime import datetime
from socket import *

file = open("../q3/server_log.txt", "a")


def main():
    host = 'localhost'
    port = 8888
    address = (host, port)

    # make server socket and bind and listen to 1 client
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(address)
    server_socket.listen(1)

    # start connection
    connection, client_address = server_socket.accept()

    while True:
        # receive message and if its start, receive 3 other messages and calculate result
        message = connection.recv(200).decode()
        log(False, datetime.now(), client_address[1], message)
        if message == 'start':
            connection.send("ok".encode())
            log(True, datetime.now(), client_address[1], "ok")


            # receive first operand and check if its integer; if yes: send ok message, if not: send appropriate response
            operand1 = connection.recv(200).decode()
            if operand1 == "exit":
                break
            log(False, datetime.now(), client_address[1], operand1)
            if not check(operand1, True):
                connection.send("the operand in not an integer!".encode())
                log(True, datetime.now(), client_address[1], "the operand in not an integer!")
                continue
            else:
                connection.send("ok".encode())
                log(True, datetime.now(), client_address[1], "ok")


            # receive operator and check if its among +-/*^; if yes: send ok message, if not: send appropriate response
            operator0 = connection.recv(200).decode()
            if operator0 == "exit":
                break
            log(False, datetime.now(), client_address[1], operator0)
            if check(operator0, False):
                connection.send("ok".encode())
                log(True, datetime.now(), client_address[1], "ok")
            else:
                connection.send("the operator is not correct!".encode())
                log(True, datetime.now(), client_address[1], "the operator is not correct!")
                continue


            # receive second operand and check if its integer; if yes: send ok message, if not: send appropriate
            # response
            operand2 = connection.recv(200).decode()
            if operand2 == "exit":
                break
            log(False, datetime.now(), client_address[1], operand2)
            if check(operand2, True):
                connection.send("ok".encode())
                log(True, datetime.now(), client_address[1], "ok")
            else:
                connection.send("the operand in not an integer!".encode())
                log(True, datetime.now(), client_address[1], "the operand in not an integer!")
                continue

            # calculate result and send it to client
            result = calculate(operand1, operand2, operator0)
            connection.send(str(result).encode())
            log(True, datetime.now(), client_address[1], str(result))

        elif message == 'exit':
            # if received message was exit break and
            break

    # close socket and connection
    file.close()
    connection.close()
    server_socket.close()


def calculate(operand1, operand2, operator):
    operand1 = int(operand1)
    operand2 = int(operand2)
    if operator == "+":
        return operand1 + operand2
    if operator == "-":
        return operand1 - operand2
    if operator == "*":
        return operand1 * operand2
    if operator == "/":
        return operand1 / operand2
    if operator == "^":
        return operand1 ** operand2
    return 0


def check(thing, is_operand):
    # if thing is operand check if its int or not; yes -> true, no -> false
    if is_operand:
        try:
            # if its not int, it will throw exception and returns false
            # else: returns true
            int(thing)
        except:
            return False
        return True
    # if thing is operator check if its in +-/*^; yes -> true, no -> false
    else:
        if thing in "+-/*^":
            return True
        return False


def log(send, born_time, port, message):
    if send:
        file.write(str(born_time) + " sending message : " + message + ", to port : " + str(port) + "\n \r")
    else:
        file.write(str(born_time) + " receiving message : " + message + ", from port : " + str(port) + "\n \r")


if __name__ == '__main__':
    main()
