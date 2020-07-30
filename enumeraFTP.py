#!/usr/bin/python

import socket

ip = input("Digite o IP: ")
porta = int(input("Digite a Porta: "))


tc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tc.connect((ip,porta))
banner = tcp.recv(1024)
print (banner)

tcp.send( "USER ftp\r\n")
user = tcp.recv(1024)
print (user)

tcp.send( "PASS ftp\r\n")
pw = tcp.recv(1024)
print (pw)

tcp.send( "HELP ftp\r\n")
cmd = tcp.recv(1024)
print (cmd)
