print("Ola Phython")

print("Remato o programa")

"""
/*Exemplo de código java*/

int numero;
"""

# Comentario dunha liña en python

# Exemplo de declaración dunha variable en phyton

# O tipado en phyton é dinámico

numero = 1
print(type(numero))

print(" O tipo resultante de dividir un real cun enteiro é: " + str(type(5.0 / 3)))

# Tipos básicos
# Números

entero = 2
enteroLargo = 2
octal = 0o26
hex = 0x24A

comaFlotante = 15.89
notacionCientifica = 9.1e-3
print(type(comaFlotante))

complexos = 5 + 3j

print(complexos)
print(type(complexos))

# Cadeas

cadena = "Un texto cualquiera"
print(type(cadena))

booleano = True
print(type(booleano))

# + - * ** / // %

print(5 // 3)
print(5 % 3)

# Operadores a nivel de bits : & and | or ^ xor ~ not  << desplazamiento a la izquierda >> desplazamiento a la derecha

print(3 & 2)

print(3 >> 1)

# 00000011 >> 0000001

print(3 << 1)
# 00000011 << 00000110

cadena = 'Texto con "comillas" dobles'
print(cadena)

cadena2 = "Texto multilinea \n mediante caracteres de escape"

cadena3 = """ Escribir texto de
forma mas natural,
y permite la documentación del código
equivalente al comentario en Java /* */
"""
print(cadena2 + "\n" + cadena3)

print("abe" * 3)

# Operadores Booleanos and or not

print(True and False)

# == != < > <= >=

if booleano == False:
    print("Boleano es falso")
    print("Pongo tantas instrucciones")
    print("como precise")

condicion = False
if condicion == True:
    print("A condición cúmplese")
else:
    print("A condición non se cumple")
    print("A condicion non se cumple")
    print("A condición non se cumple")

numero = 0
if numero == 0:
    print("O número é cero")
elif numero == 1:
    print("O número é un")
elif numero == 2:
    print("O número é dous")
else:
    print("A condición non se cumple")

    # A if C else B

    valor = "Par" if (numero % 2 == 0) else "Impar"

while numero < 15:
    numero = numero + 1
    print("Numero: " + str(numero))
    # fai falta castear para facer o print
    # podemos usar o break para salir do bucle

numero = 0

while True:
    numero = numero + 1
    print("Numero: " + str(numero))
    if numero >= 15:
        print("Rematamos o ciclo")
        break

serie = [1, 2, 3, 4]
for numero in serie:
    print(numero)
    """
    int vector[] = { 1, 2, 3, 4,}
    for (int i =0; i < 5; i++){
    println("%d\n", vector [i]);
    """


def nome_funcion(parametro1, parametro2):
    """ Esta función vai a imprimir os parámetros
    pasados como argumentos"""
    print(parametro1)
    print(parametro2)


nome_funcion("Ola", 4)
nome_funcion(parametro2="6", parametro1="Adeus")


# nome_funcion("Que tal") fai falta un parámetro

def funcion2(parametro1, parametro2=8):
    """ Esta función vai a imprimir os parámetros
        pasados como argumentos"""
    print(parametro1)
    print(parametro2)
    funcion2("Outra función", 10)
    funcion2("De novo outra función")


def funcion3(numero1, numero2, *masNumeros):
    print(numero1)
    print(numero2)

    for parametro in masNumeros:
        print(parametro)

    funcion3(2, 5, 8, 10)

    funcion3(2, 5, 8, 10, 1, 1, 2, 4, 6)

#Alternativa o bucle for en java con range

for i in range(5):
    print("valor: "+ str(i))

#Outro exemplo

for a in range(2,20,3):
    print("valor: "+ str(a))


lista = [1, 3, 4, 6, "Cadeas", 2.3, True, ["outra lista", 2, 5]]
print(lista[5])
print(lista[7][1])
print(lista[0:3])
print(lista[:3])
print(lista[1:7:2])
print(lista[::2])
lista[3] = False
print(lista)

lista[0:2] = [7, 8, 9, 0, 10]
print(lista)

lista2 = list()
# lista2 = []
print(type(lista2))

tupla = (1, 3, "Hola", True, (4, "Que tal"))
tupla2 = (1)
print(type(tupla))
print(type(tupla2))
# unha tupla é estática,non se modifica

tupla3 = 1,
print(type(tupla3))

diccionario = {

    "Azul": "#2E86C1",
    "Vermello": "R74C3C",
    "Verde": "#2ECC71"

}


def funcion4(nome, apelidos, **datosPersoais):
    print(nome)
    print(apelidos)
    for valor in datosPersoais.values():
        print (valor)
    for claves in datosPersoais.keys():
        print(claves)
    for clave in datosPersoais.keys():
        print(datosPersoais[clave])

        l = list()
        t = tuple()
        d = dict()



funcion4("Manuel", "Guimarey", cidade="Vigo", direccion="García Barbón 48")

def incrementa (x,y):
    x = x+1
    y[0] = y[0]+1
    print(x,y)

a = 4
b = [6]
incrementa(a,b)

print(a,b)

def suma(x,y):
    resultado = x + y
    return resultado

s = suma(5,6)
print(s)

def dobrar (x,y):
    dobreX = x * 2
    dobreY = x * 2
    return dobreX, dobreY

a,b = dobrar (2,3)
print(a)

valores = dobrar(4,5)
print(valores[0],valores[1])



def producto ():
    print("Cálculo do producto de dous números")
    n1 = input("Introduce o primeiro número: ")
    n2 = input("Introduce o segundo número: ")
    print(" O producto é: ", int(n1)*int(n2))

producto()

def producto2 (n1,n2, *restoValores):
    producto = n1*n2
    for valor in restoValores:
        producto = producto * valor
    print(producto)

def suma2 (n1, n2, *restoValores):
    suma = n1 + n2
    for valor in restoValores:
        suma = suma +valor
    print(suma)

suma2(5,4)
suma2(5,4,12,6,8,18,22,5)


def esta_a_tupla_ordeada(tupla):
    ordeada = True
    valor1 = tupla[0]
    for valor in tupla:
        if valor1> valor:
         ordeada = False
        valor1 = valor
    return ordeada
print(esta_a_tupla_ordeada((3,5,6,7,7,8)))


lista.append("novo valor añadido") #añadir valores a la tupla ( un elemento)
lista.extend(("outro","outro",("outro",))) # añadir valores a la tupla ( varios elementos)
lista.insert(4,"inserto") #añado un valor dando la posición y luego el contenido
print(lista)
print (lista.count(['Pepe','Asia','Oceania']))
print(lista.count('outro'))
print(len(lista))
#print(lista.index('outro',10,12)) # podemos decirlle dende que opinión queremos que conte
lista.pop(4)  #Me dice el indice del elemento que yo quiero eliminar
lista.remove(4)#serve para eliminar el elemento ( la primera coincidencia)
lista.reverse()
lista2=[3,2,5,7,5,9,3]
lista2.sort()
print(lista2)
lista3 = [("Raul",15),("Belen",17),("Ana",16)]
#lista3.sort()
#print(lista3)

def comparacion (elemento):
    return elemento[1]

lista3.sort(key = comparacion, reverse=True)
print(lista)




diccionario = {
    "Azul": "#2E86C1",
    "Vermello": "#E74C3C",
    "Verde": "#2ECC71"
}

print(diccionario["Verde"])

print(diccionario.get("Verdesssss", "O obxecto non existe"))
print("Verde" in diccionario)
print(diccionario.items())
for entrada in diccionario.items():
    print("Clave: " + entrada[0] + " Valor: " + entrada[1])

print(diccionario.keys())
print(diccionario.values())
print("Borrando a entrada con clave: verde\n Que devolta o valor: " + diccionario.pop("Verde", "#0000000"))

                       #Ampliación de cadeas
cadea = "Unha cadea para traballar como exemplo"
print(cadea.count("cadea"))
print(cadea.find("cadea",6,30))
print(cadea.join(("Ola","que","tal")))
print(cadea.partition(' '))
print(cadea.split(' ',5))
print(cadea.replace('cadea', "******",1))


