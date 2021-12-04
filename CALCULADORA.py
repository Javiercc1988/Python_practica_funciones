import math

def sum(num1,num2):
    resultado = num1+num2
    return resultado

def rest(num1,num2):
    resultado = num1-num2
    return resultado

def multi(num1,num2):
    resultado = num1*num2
    return resultado

def divi(num1,num2):
    resultado = num1/num2
    return resultado

def divi_entera(num1,num2):
    resultado = num1//num2
    return resultado

def resto_div(num1):
    resultado = num1%2
    return resultado

def poten(num1,num2):
    resultado = num1**num2
    return resultado

def raizcuadrada(num1):
    resultado = (math.sqrt(num1))
    return resultado



bucle = True

while bucle:
    operacion = int(input("""¿Qué operación quiere realizar?
        1...para SUMAR
        2...para RESTAR
        3...para MULTIPLICAR
        4...para DIVIDIR
        5...para DIVISION ENTERA
        6...para RESTO
        7...para POTENCIA
        8...para RAIZ CUADRADA    
        9...para SALIR
        : """))



    if operacion == 1:
        numero1 = float(input("Introduce el primer número: "))
        numero2 = float(input("Introduce el segundo número: "))
        sumar = sum(numero1,numero2)
        print("\nEl resultado de la suma es,",sumar,"\n")
        bucle = True
        
    elif operacion == 2:
        numero1 = float(input("Introduce el primer número: "))
        numero2 = float(input("Introduce el segundo número: "))
        restar = rest(numero1,numero2)
        print("\nEl resultado de la resta es,",restar,"\n")
        bucle = True
        
    elif operacion == 3:
        numero1 = float(input("Introduce el primer número: "))
        numero2 = float(input("Introduce el segundo número: "))
        multiplicar = multi(numero1,numero2)
        print("\nEl resultado de la multiplicación es,",multiplicar,"\n")
        bucle = True
        
    elif operacion == 4:
        numero1 = float(input("Introduce el primer número: "))
        numero2 = float(input("Introduce el segundo número: "))
        division = divi(numero1,numero2)
        print("\nEl resultado de la división es,",division,"\n")
        bucle = True
        
    elif operacion == 5:
        numero1 = float(input("Introduce el primer número: "))
        numero2 = float(input("Introduce el segundo número: "))
        div_entera = divi_entera(numero1,numero2)
        print("\nEl resultado de la división entera es,",div_entera,"\n")
        bucle = True
        
    elif operacion == 6:
        numero1 = float(input("Introduce el número: "))
        resto = resto_div(numero1)
        print("\nEl resto de la division es,",resto,"\n")
        bucle = True
        
    elif operacion == 7:
        numero1 = float(input("Introduce el primer número: "))
        numero2 = float(input("Introduce su potencia: "))
        potencia = poten(numero1,numero2)
        print("\nEl resultado de la potencia es,",potencia,"\n")
        bucle = True
        
    elif operacion == 8:
        numero1 = float(input("Introduce el número: "))
        raiz = raizcuadrada(numero1)
        print("\nLa raiz cuadrada es,",raiz,"\n")
        bucle = True
        
    elif operacion == 9:
        print("\nHas elegido salir del programa, ¡hasta pronto!","\n")
        bucle = False

    else:
        print("\nLa Opción elegida no es válida\n")
        bucle = True
