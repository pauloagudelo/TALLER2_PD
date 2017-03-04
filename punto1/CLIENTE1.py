#!/usr/bin/env python
# -*- coding: utf-8 -*

import socket

cliente = socket.socket()

"""direccion ip del servidor, puerto del servidor"""

cliente.connect(("localhost", 35000))

while True:

    mensaje_cliente = raw_input("ingrese el nombre: ")
    cliente.send(mensaje_cliente)

    usuario = raw_input("ingrese la contrasena: ")
    cliente.send(usuario)

    ip = raw_input("ingrese la direccion ip: ")
    cliente.send(ip)

    fecha = raw_input('fecha de inicio de sesion: ')
    cliente.send(fecha)

    hora = raw_input('Hora de inicio de sesion: ')
    cliente.send(hora)

    if (mensaje_cliente == 'paulo' and usuario == 'agudelo1977'):
        print "CALCULAD0RA"

    else:
        print'No puede Acceder'
        break

    lista = ['1.sumar', '2.Restar', '3.Multiplicar', '4.Dividir', '5.salir']

    for i in lista:
        print i

    import operaciones1

    operaciones.suma()
    operaciones.resta()
    operaciones.producto()
    operaciones.division()

    if mensaje_cliente == "salir":

        break

#mensaje_servidor = socket_cliente.recv(1024)
#print mensaje_servidor

print "estamos para servirle"
cliente.close()


