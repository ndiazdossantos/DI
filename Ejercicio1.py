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


#exercicio 7.1

tupla = ("Pedro","Eduardo","Juan","Pablo","Sofia","Maria")

def lista(tupla):
    for x in (tupla):
        print("Estimado",x)
lista(tupla)

"""
def listaX(tupla1,ini,fin):
    for x in (tupla1[ini:fin]):
        print("Estimado",x)
listaX(tup1,2,5)
"""

#exercicio 7.2
def lista2(tupla):
    for valor in range(1,5,1):
        print("Estimado",tupla[valor])
lista2(tupla)

#Exercicio 7.3
tuplaGenero=(("Pedro","Hombre"),("Eduardo","Hombre"),("Juan","Hombre"),("Pablo","Hombre"),("Sofia","Mujer"),("Maria", "Mujer"))
def lista3(tupla):
    for valor in tupla:
        valor[1]
        if valor [1] == "Mujer":
            print("Estimada Sra.",valor[0])
        else:
            print("Estimado Sr.",valor[0])
lista3(tuplaGenero)
