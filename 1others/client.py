# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 18:56:27 2020

@author: WSX
"""

if __name__ == '__main__':
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 8001))
    import time
    time.sleep(1)
    sock.send(b'hahahahaha!!')
    print(sock.recv(1024))
    sock.close()
