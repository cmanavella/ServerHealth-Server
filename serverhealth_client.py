import socket
import sys
import os
from termcolor import colored
import json
import time

#Variables
host = 'localhost'
port = 1992

#Bucle que retiene la conexión
while True:
    #Borro la pantalla
    os.system('clear')

    #Creo el objeto Socket
    server = socket.socket()

    #Trato de conectar con el servidor
    try:
        server.connect((host, port))
    except socket.error as mensaje_refused:
        print(colored('Se produjo un error al intentar conectar con ' +
            'host:', 'red'), host, colored('por el puerto:', 'red'),
            port)
        print(colored(mensaje_refused, 'red'))
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

    print("Conectado al servidor [", colored('OK', 'green'), "]")

    #Capturo la excepcion de cancelacion del teclado para salir del server
    try:
        data = server.recv(1024)
        data = data.decode("utf-8")
        data = json.loads(data)

        print(colored('Sistema:', 'cyan'), data["system"])
        print(colored('Version:', 'cyan'), data["release"])

        server.close()
        time.sleep(1)
    except KeyboardInterrupt:
        try:
            sys.exit(0)
            server.close()
        except SystemExit:
            os._exit(0)
            server.close()
