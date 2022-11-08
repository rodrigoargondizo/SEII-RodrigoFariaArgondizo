import socket

TCP_IP = "127.0.0.1"
FILE_PORT = 5005
DATA_PORT = 5006
timeout = 3
buf = 1024

# Criando servidor na porta FILE_PORT para receber o nome do arquivo:
sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_f.bind((TCP_IP, FILE_PORT)) # pedindo permissão ao SO para escutar em FILE_PORT
sock_f.listen(1) # Escutando um cliente por vez

# Criando servidor na porta FILE_PORT para receber o nome do arquivo:
sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_d.bind((TCP_IP, DATA_PORT)) # pedindo permissão ao SO para escutar em DATA_PORT
sock_d.listen(1) # Escutando um cliente por vez

# Loop infinito para ficar à espera de clientes
while True:
    conn, addr = sock_f.accept() # Recebendo solicitação de cliente
    data = conn.recv(buf) # Extraindo dado recebido
    if data: # Filtrando e printando dado recebido
        print("File name:", data)
        file_name = data.strip().decode('ascii').split('/')[-1] # extraindo somente o nome do arquivo p/ salvar no diretório local

    # Abrindo arquivo de destino
    f = open(file_name, 'wb')

    conn, addr = sock_d.accept() # Recebendo solicitação de cliente
    while True: # Recebendo dados recursivamente em chunks do tamanho do buffer
        data = conn.recv(buf)
        if not data:
            break # Interrompendo quando os bytes acabam
        f.write(data) # Escrevendo os dados recebidos pelo socket no arquivo

    print(f"{file_name} Finish!")
    f.close() # Fechando conexão com o arquivo