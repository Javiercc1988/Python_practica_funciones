SALIDA = "salir"
ARCHIVO_LISTA = "lista_compra.txt"

def pregunta_producto_usuario():
    return input("Introduce un producto [{} para salir]: ".format(SALIDA)).lower()


def guardar_lista_a_disco(lista_compra):
    with open(ARCHIVO_LISTA, "w") as mi_archivo:
        mi_archivo.write("\n".join(lista_compra))
    
    ### Estas 3 lineas podemos hacerla de una forma diferente y mas elegante ( es la que se suele utilizar):
    """
    with open(nombre_fichero + ".txt", "w") as mi_archivo:
        mi_archivo.write("\n".join(lista_compra))
    """

def guardar_item_en_lista(lista_compra, item_a_guardar):
    if item_a_guardar.lower() in [a.lower() for a in lista_compra]:
        print("El producto ya existe!")
    else:
        lista_compra.append(item_a_guardar)


def cargar_o_crear_lista():
    lista_compra = []

    # Con esta función vamos a preguntar si quieren recuperar el último archivo o crear uno nuevo.
    if input("¿Quieres volver a cargar el ultimo fichero?").lower() == "s":
        try:
            with open(ARCHIVO_LISTA, "r") as a:
                lista_compra = a.read().split("\n")
        except FileNotFoundError:
            print("¡El archivo de la compra no existe!")
    else:
        pass
    return lista_compra


def mostrar_lista(lista_compra):
    print("\n".join(lista_compra))



def main():
    lista_compra = cargar_o_crear_lista()
    mostrar_lista(lista_compra)
    input_usuario = pregunta_producto_usuario()

    while input_usuario != SALIDA:
        guardar_item_en_lista(lista_compra, input_usuario)
        input_usuario = pregunta_producto_usuario()
    mostrar_lista(lista_compra)
    guardar_lista_a_disco(lista_compra)


if __name__ == "__main__":
    main()
