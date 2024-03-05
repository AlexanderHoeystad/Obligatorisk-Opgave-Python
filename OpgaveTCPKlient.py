from socket import *

serverName = "localhost"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

keep_communacating = True

while keep_communacating:
    sentence = input('Input yor sentence:')
    if sentence == "QUIT": 
        clientSocket.send(sentence.encode())
        modifiedSentence = clientSocket.recv(1024)
        print('From server: ', modifiedSentence.decode())
        keep_communacating = False
        break

    else:
        clientSocket.send(sentence.encode())
        modifiedSentence = clientSocket.recv(1024)
        print('From server: ', modifiedSentence.decode())

        
clientSocket.close()

    