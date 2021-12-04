####Escribir un programa que pida valores y los añada a una lista hasta que el usuario pulse la
####letra ‘q’. Con esa lista introducida por el usuario y haciendo uso de una función, elimine los
####repetidos en esa lista. Luego nos muestre la lista inicialmente y la lista sin los repetidos.

def eliminar(num1,num2):
    for i in num1:
        if i not in num2:
            num2.append(i)

repetir = True
lista1 = []
lista2 = []



while repetir:
    dato1 = input("Introduce un nº('q' para salir: ")
    lista1.append(dato1)
    if dato1 == "q":
        repetir = False
        
lista1.pop(-1)

eliminar(lista1,lista2)

print("La lista inicial es:",lista1,"\nLa lista final es:",lista2)
