# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 18:51:14 2020

@author: WSX
"""
if __name__ == '__main__':
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8001))
    sock.listen(5)
    while True:
        connection, address = sock.accept()
        try:
            connection.settimeout(5)
            buf = connection.recv(1024)
            print(buf)
            if buf == b'1':
                connection.send(b'welcome!')
            else:
                connection.send(b'no!')
        except sock.timeout:
            print('timeout!')
            connection.close()
            
