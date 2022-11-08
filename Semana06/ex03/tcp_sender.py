#!/bin/usr

import socket
import sys

TCP_IP = "127.0.0.1"
FILE_PORT = 5005
DATA_PORT = 5006
buf = 1024
file_name = sys.argv[1]


try:
    # Criando socket para enviar o nome do arquivo:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, FILE_PORT))
    sock.send(file_name.encode('ascii'))
    sock.close()

    print(f"Sending {file_name} ...")

    # Criando socket para enviar os dados do arquivo:
    f = open(file_name, "rb") # lendo o arquivo
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, DATA_PORT))
    data = f.read() # extraindo dados do arquivo
    sock.send(data) # enviando dados do arquivo pelo socket

finally: # Fechando conexões com o server e o arquivo.
    sock.close()
    f.close()