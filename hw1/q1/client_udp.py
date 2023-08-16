import socket
import time
from datetime import datetime
from socket import *

file = open("../q1/client_log.txt", "a")


def main():
    host = "localhost"
    server_port = 8686
    server_address = (host, server_port)
    # make client socket
    udp_client_socket = socket(AF_INET, SOCK_DGRAM)

    for i in range(10):
        try:
            # make sending ping
            message = "Ping " + str(i + 1) + " " + str(time.time())
            # log sending message
            log(True, datetime.now(), server_port, message)
            start = time.time()
            # send message to server
            udp_client_socket.sendto(message.encode(), server_address)
            # apply a timeout for socket, if after 2 sec it doesnt receive any response, it will throw an exception
            udp_client_socket.settimeout(2)
            # receive response
            received_message, _ = udp_client_socket.recvfrom(200)
            end = time.time()
            received_message = received_message.decode()
            # log response
            log(False, datetime.now(), server_port, received_message)
            print(received_message + " ,ping time: " + str(end - start) )
        except:
            print("Request timed out")
            pass
    file.close()
    udp_client_socket.close()


def log(send, born_time, port, message):
    if send:
        file.write(str(born_time) + " sending message : " + message + ", to port : " + str(port) + "\n \r")
    else:
        file.write(str(born_time) + " receiving message : " + message + ", from port : " + str(port) + "\n \r")


if __name__ == '__main__':
    main()
