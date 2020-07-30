#!/usr/bin/python
import sys
from scapy.all import*

a = input("Digite o IP: ")
b = int(input("Digite a porta: "))
c = str(input("Digite a flag: "))

conf.verb = 0

pIP = IP(dst = a)
pTCP = TCP(dport = b, flags = c)
pacote = pIP/pTCP
resposta = sr1(pacote)
resposta.show()
