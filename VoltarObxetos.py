def saudar(idioma):
    def saudar_es():
        print("Hola")
    def saudar_gl():
        print("Ola")
    def saudar_en():
        print("Hi")
    def saudar_fr():
        print("salut")

    idioma_funcion = {"es" : saudar_es,
                      "gl" : saudar_gl,
                      "en" : saudar_en,
                      "fr" : saudar_fr }
    return idioma_funcion [idioma]

f = saudar("fr")
print(f)
saudar("fr")()
f()


def cadrado(n):
    return n**2

l = [2,7,3,8]
l2 = map(cadrado,l)
print(l2)

for num in l2:
    print(num)

l3 = [n**2 for n in l]
print(l3)

l4 = map(lambda n: n*2, l)
for num in l4:
    print(num)

l5 = [n for 5 in l if n % 2 == 0]

votantes = [("Pablo","Sr"),("Ana","Sra"),("Puri","Sra"),("Jose","Sr")]
votantes_femeninas = [votante[0] for votante in votantes]

num = [0,1,-3,2,3,4]
letra = [ 'a','b','c']
letras = [ n * l for l in letra
                 for n in num
                 if n>0]
print(letras)
x = (n ** 2 for n in l)
print(x)

def xenerador (n,m,s):
    while(n<=m):
        yield n
        n +=s
