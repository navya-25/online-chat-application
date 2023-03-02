import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 1234
server.bind(("localhost",port))

server.listen()

client,addr = server.accept()

done = False


while not done:
    msg = client.recv(1024).decode('utf-8')
    if msg == 'quit':
        done = True
    else:
        #print(msg)
        print("client says:", msg)
    client.send(input("message:").encode('utf-8'))





