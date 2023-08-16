import random
import sys
import time
from datetime import datetime
from socket import *

file = open("../q1/server_log.txt", "a")


def main():
    host = "localhost"
    port = 8686
    address = (host, port)
    # make server socket
    udp_server_socket = socket(AF_INET, SOCK_DGRAM)
    # bind server socket
    udp_server_socket.bind(address)

    counter = 0
    while counter < 10:
        counter += 1
        # receive message from client
        message, client_address = udp_server_socket.recvfrom(200)
        # print received messages
        print(message.decode() + ". receive time : " + str(time.time()))
        # log message
        log(False, datetime.now(), client_address[1], message.decode())
        # make response message
        response_message = message.decode().upper()
        # send response with 70% probability
        if random.randint(0, 10) < 7:
            # log message
            log(True, datetime.now(), client_address[1], response_message)
            # send response
            udp_server_socket.sendto(response_message.encode(), client_address)

    file.close()
    # close socket
    udp_server_socket.close()


def log(send, born_time, port, message):
    if send:
        file.write(str(born_time) + " sending message : " + message + ", to port : " + str(port) + "\n \r")
    else:
        file.write(str(born_time) + " receiving message : " + message + ", from port : " + str(port) + "\n \r")


if __name__ == '__main__':
    main()
