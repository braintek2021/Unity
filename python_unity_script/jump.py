import time
import math
import socket
import time


UDP_IP = "127.0.0.1"
UDP_PORT = 5065

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



while True:
    #User_inp = input("User command:")
    User_inp = "Jump"
    if User_inp =='Jump':
        sock.sendto( ("JUMP!").encode(), (UDP_IP, UDP_PORT) )
        print("_"*10, "Jump Action Triggered!", "_"*10) 
    else:
        print("_"*10, "Jump Action not Triggered!", "_"*10) 
    time.sleep(5)