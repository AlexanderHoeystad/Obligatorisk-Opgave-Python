from socket import *
import threading
import random

def handleClient(connectionSocket, addr):
    print(addr[0])
    keep_communacating = True

    while keep_communacating: 
        sentence = connectionSocket.recv(1024).decode()
        response = "Send a proper message"
        if sentence.strip() == "QUIT":
            keep_communacating = False
            response = "Goodbye closing the connection"
            connectionSocket.send(response.encode())
            break

        elif sentence.startswith("Random"):
            response = "Input Numbers"
            connectionSocket.send(response.encode())

            input = connectionSocket.recv(1024).decode().strip()
            number1, number2 = map(int, input.split())

            random_number = random.randint(number1, number2)
            response = str(random_number)

        elif sentence.startswith("Add"):
            response = "Input Numbers"
            connectionSocket.send(response.encode())

            input = connectionSocket.recv(1024).decode().strip()
            number1, number2 = map(int, input.split())

            response = str(number1 + number2)

        elif sentence.startswith("Subtract"):
            response = "Input Numbers"
            connectionSocket.send(response.encode())

            input = connectionSocket.recv(1024).decode().strip()
            number1, number2 = map(int, input.split())

            response = str(number1 - number2)


        connectionSocket.send(response.encode())
    connectionSocket.close()
    print('Connection closed')

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to listen')

while True:
    connectionSocket, addr = serverSocket.accept()
    #handleClient(connectionSocket, addr)
    threading.Thread(target = handleClient, args = (connectionSocket, addr)).start()
