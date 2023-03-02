import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


port = 1234

client.connect(("localhost",1234))

done = False
while not done:
    client.send(input("Message: ").encode('utf-8'))
    msg  = (client.recv(1024).decode('utf-8'))
    if msg == 'quit':
        done = True
    else:
         print("server says: ",msg)
