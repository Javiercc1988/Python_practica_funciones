###### AGENDA TELEFONICA

############################################
############ F U N C I O N E S #############
############################################


def añadir_modificar():
    nombre = input("Introduce un nombre: ").capitalize()
    telefono = int(input("Introduce un telefono: "))
    if nombre in dicc_agenda:
        modificar = input("El registro ya existe, quiere modificarlo(S/N): ").lower()
        if modificar == "s":
            dicc_agenda[nombre]=telefono
        else:
            print("El registro no se modificará")
    else:
        dicc_agenda[nombre]=telefono

def borrar():
    borrado = input("Introduzca el nombre que quiere borrar: ").capitalize()
    if borrado in dicc_agenda:
        confirmar = input("¿Seguro que quiere eliminar el registro?(S/N): ").lower()
        if confirmar == "s":
            del dicc_agenda[borrado]
        else:
            print(borrado,"no será eliminado")
    else:
        print("El registro no existe.")

def buscar():
    iniciales = input("Introduce el nombre a buscar: ").capitalize()
    for i in dicc_agenda:
        if i.startswith(iniciales):
            print("Nombre:",i,"Telefono:",dicc_agenda[i])
                
def listar():
    contador = 0
    print("\nSu listado de telefonos:")
    for i in dicc_agenda:
        contador +=1
        print(contador,i,dicc_agenda[i],sep=".")
    print()



############################################
############  P R O G R A M A  #############
############################################
        

dicc_agenda = {'Sara':635124521,'Pedro':654741258,'Marta':645231512,'Nuria':652159753,'Silvia':659758451}
repetir = True

while repetir:
    menu = int(input("""\nOpciones del menú:
        1.Añadir/modificar
        2.Buscar
        3.Borrar
        4.Listar
        5.Salir
¿Qué opción quiere usar?
:"""))
    
    if menu == 1:
        añadir_modificar()
        print(dicc_agenda)
        
    elif menu == 2:
        buscar()
        
    elif menu == 3:
        borrar()
        print(dicc_agenda)
        
    elif menu == 4:
        listar()
        
    elif menu == 5:
        print("El programa ha finalizado.")
        repetir = False
    else:
        print("Seleccione una opcion válida.")
        repetir = True
