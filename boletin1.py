"""
def ejer1 (numero):
    print(numero*1)
    print(numero*2)
    print(numero*3)
    print(numero*4)
    print(numero*5)
    print(numero*6)
    print(numero*7)
    print(numero*8)
    print(numero*9)
    print(numero*10)

ejer1(5)
"""

def ejer1_1():
    numero=int(input("Introduce el número que deseas obtener su tabla de multiplicar: "))
    multiplicar = 1

    while multiplicar < 10:
        resto = numero * multiplicar
        print("Numero "+str(numero)+" * "+ str(multiplicar)+" = "+str(resto))
        multiplicar = multiplicar+1

    else:
        print("Terminado")

ejer1_1()

def ejer2():
    for i in range(10,21):
        print(i)

ejer2()


def ejer3():
    print("  ")
    print("  ")
    fahrenheit = int(input('Ingrese una temperatura en grados Fahrenheit: '))
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    print('{} grados Fahrenheit son {} grados Celsius '.format(fahrenheit, celsius))
    print("  ")
    print("  ")
ejer3()

def ejer3_1(x):
    op =(x - 32) * 5.0 / 9.0
    return op

def ejer3_2():
    for i in range(0,130,10):
     print('{} grados Fahrenheit son {} grados Celsius '.format(str(i), str(ejer3_1(i))))
ejer3_2()


def ejer4():
    ano = int(input('Introduce un ano: '))

    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                print('O ano é bisiesto')
            else:
                print('O año non é bisiesto')
        else:
            print('O ano é bisiesto')
    else:
        print('O año non é bisiesto')
ejer4()

def ejer5():
    mes = int(input("Ingresa o número do mes"))
    if (mes >= 3 and mes <= 12 or mes == 1):
        if (mes <= 7):
            if (mes % 2 == 0):
                print("O mes " + str(mes) + " ten 30 dias")
            else:
                print("O " + str(mes) + " ten 31 dias")
        else:
            if (mes % 2 == 0):
                print("O " + str(mes) + " ten 31 dias")
            else:
                print("O " + str(mes) + " ten 30 dias")
    else:
        print("Datos erroneos")
ejer5()



#Exercicio 1.8.1
#Opcion manuel
"""
def calculos (n1,n2):
    suma = n1 + n2
    resta = n1 - n2
    multiplicacion = n1 * n2
    division = n1 / n2
    return suma,resta,multiplicacion,division

var = calculos(8,2)
sum,rest,mult,div = calculos(10,5)
print(var)
"""
#mi opcion
def calculos2():
    n3 = int(input("Introduce o primeiro número: "))
    n4 = int(input("Introduce o segundo número: "))
    suma2 = n3 + n4
    resta2 = n3 - n4
    multiplicacion2 = n3 * n4
    division2 = n3 / n4
    return suma2,resta2,multiplicacion2,division2
print(calculos2())
