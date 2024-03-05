from socket import *
import threading
import random
import json

def handleClient(connectionSocket, addr):
    print(addr[0])
    keep_communicating = True

    while keep_communicating:
        sentence = connectionSocket.recv(1024).decode()
        json_sentence = json.loads(sentence)
        Method = json_sentence.get('Method')

        if Method == "QUIT":
            keep_communicating = False
            response = {"Message": "Goodbye closing the connection"}

        elif Method == "Random":
            number1 = json_sentence.get('number1')
            number2 = json_sentence.get('number2')

            if number1 is None or number2 is None:
                response = {"Error": "Wrong input"}
            else:
                random_number = random.randint(number1, number2)
                response = {"Random number": random_number}

        elif Method == "Add":
            number1 = json_sentence.get('number1')
            number2 = json_sentence.get('number2')

            if number1 is None or number2 is None:
                response = {"Error": "Wrong input"}
            else:
                response = {"Result": number1 + number2}

        elif Method == "Subtract":
            number1 = json_sentence.get('number1')
            number2 = json_sentence.get('number2')

            if number1 is None or number2 is None:
                response = {"Error": "Wrong input"}
            else:
                response = {"Result": number1 - number2}

        else:
            response = {"Error": "Wrong Method"}

        connectionSocket.send(json.dumps(response).encode())

    connectionSocket.close()
    print('Connection closed')

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to listen')

while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handleClient, args=(connectionSocket, addr)).start()

