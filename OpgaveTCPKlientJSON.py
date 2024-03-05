from socket import *
import json

serverName = "localhost"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM) 
clientSocket.connect((serverName, serverPort))

keep_communacating = True

while keep_communacating:
    Method = input('Enter Method: (Random/Add/Subtract/QUIT)')
    if Method == "QUIT":
        request = json.dumps({"Method": Method})
        keep_communacating = False
    else:
        number1 = int(input('Enter number1: '))
        number2 = int(input('Enter number2: '))
        request = json.dumps({"Method": Method, "number1": number1, "number2": number2})

    clientSocket.send(request.encode())
    response = clientSocket.recv(1024).decode()
    print('From server: ', response)
clientSocket.close()