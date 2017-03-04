import os

P = []

def menu():
    lista = ['1.Listar', '2.Crear', '3.Modificar', '4.Eliminar', '5.salir']

    for i in lista:
        print i
menu()

def crear():
    opc = int(input("Selecione una Opcion: "))
    if (opc == 2):
        nombre=raw_input('ingrese Nombre del Archivo:')
        archivo = open(nombre+'.txt', 'w')
        archivo.close()
        print 'Archivo Creado'
crear()

def listar():
    opc = int(input("Selecione una Opcion: "))
    if (opc == 1):
      P.append(archivo)
      for i in P:
          print i
listar()


def modificar():
    opc = int(input("Selecione una Opcion: "))
    if (opc == 3):
        mod=raw_input('Ingrese el nombre del Archivo a modificar:   ')
        if(mod == 'archivo1'):
            edicion = raw_input("Escriba para ingrearlo al archivo: \n  ")
            outfile = open('archivo1', 'a')
            outfile.write(edicion)


            infile = open('archivo1', 'r')

            print(infile.read())

modificar()

def eliminar():
    opc = int(input("Selecione una Opcion: "))
    if (opc == 4):
        eli = raw_input('Ingrese el nombre del Archivo para eliminar:   ')
        if (eli == ''):
            os.remove(eli)
            print('El archivo ha Sido Borrado')
eliminar()

def salir():
    opc = int(input("Selecione una Opcion: "))
    if (opc == 5):
        print 'Eligio salir'

salir()

