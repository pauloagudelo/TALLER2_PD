import json

def menu():
    lista = ["Bienvenidos al deposito Arco Iris","1.comprar productos", "2.ventas del dia", "3.inventarios", "4.salir"]
    cadena = json.dumps(lista)
    return cadena

def comprar_productos():
    lista = ["1. Frijoles   $ 2000","2. Arroz $ 1400", "3. Lentejas $ 2500", "4. Yuca $ 400", "5. Spaguettis $ 1000", "7. Panela $ 3500", "8. Leche $ 1800", "9. Aceite $ 5500", "10. Sal $ 600"]
    cadena = json.dumps(lista)
    return cadena

def ventas_dia():
    lista = ["1. frijol"]
    cadena = json.dumps(lista)
    return cadena

def inventarios():
    lista = ["2. arroz"]
    cadena = json.dumps(lista)
    return cadena

