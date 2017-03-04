#!/usr/bin/env python
# -*- coding: utf-8 -*

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# direccion ip del servidor y puerto de conexion
server.bind(("", 35000))

server.listen(1)

socket_cliente, direccion = server.accept()

while True:

    mensaje_cliente = socket_cliente.recv(1024)
    if mensaje_cliente == "paulo":
        print "Usuario correcto"
    else:
        print "usuario incorrecto"

    usuario = socket_cliente.recv(1024)
    if usuario == "agudelo":
        print "su contraseña es correta"
        print 'Bienvenido'
    else:
        print "clave incorrecta"

    ip = socket_cliente.recv(1024)
    if ip == "192.30.80":
        print "la direccion IP es correcta"
    else:
        print "La direccion IP es incorrecta"

    fecha = socket_cliente.recv(1024)
    if fecha == "marzo 17":
        print "la fecha es correcta"
    else:
        print "la fecha incorrecta"

    hora = socket_cliente.recv(1024)
    if hora == "8am" :
        print "la Hora correcta"
    else:
        print "la Hora incorrecta"

    import archivo1
    archivo.archivos()
    archivo.escribir()
else:
    print "clave incorrecta"

#    menu.menu_operaciones()

salir = socket_cliente.recv(1024)
if salir == "salir":

#break

    print "estamos para servirle"
    socket_cliente.close()
    server.close()

'''
print str(direccion[0]) + " escribio: ", mensaje_cliente
mensaje_servidor = raw_input("Ingrese Respuesta al Cliente >> ")
socket_cliente.send(mensaje_servidor)
'''
# imprimir la direccion ip del cliente str(addr[0])+

