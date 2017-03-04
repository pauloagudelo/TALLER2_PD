# -*- coding: utf-8 -*-

import socket
import funciones_cliente

def main():

    cliente = socket.socket()
    cliente.connect(("localhost", 5000))

    mostrar_menu = False

    while True:

        mensaje_servidor = cliente.recv(1024)
        if mostrar_menu == False:
            funciones_cliente.menu(mensaje_servidor)
            mostrar_menu = True
        else:
            print mensaje_servidor

        mensaje_cliente = raw_input("Ingrese Mensaje al Servidor >>> ")
        cliente.send(mensaje_cliente)

        if mensaje_cliente == "4":
            break

    print "Vuelva Pronto"
    cliente.close()

if __name__ == '__main__':
    main()