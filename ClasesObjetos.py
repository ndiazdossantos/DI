import math

class Punto:
    "Clase que define un punto"
    def __init__(self, x=0, y=0):   #podemos poner unos valores por defecto por si el usuario no pone nada
        self.x = x
        self.y = y

meuPunto = Punto(4,5)
meuPunto.x = 10  #como podemos observar no está protegido, puede cambiarse (no encaptsula la información)
print(meuPunto.x)

class Circulo (Punto): #se leería, círculo que hereda de punto
    def __init__(self, x=0, y=0, r=1):
        Punto.__init__(self, x,y)
        self.r = r

    def superficie (self):
        return math.pi*self.r**2

    def perimeto (self):
        return 2*math.pi*self.r

class Altura:
    def __init__(self, h=1):
        self.h = h

class Cilindro (Circulo, Altura):
    def __init__(self, x=0, y=0, r=1, h=1):
        Circulo.__init__(self, x, y, r)
        Altura.__init__(self, h)

    def volume(self):
       return Circulo.superficie(self)*self.h

    def superficie(self):
        return Circulo.superficie(self)*2+ self.h*self.perimeto()

    def __privado(self):
        print("Metodo privado")

    def publico(self):
        self.__privado()

c = Cilindro()
print(c.volume())
print(c.superficie())
print(c.x)
#print(c.__h)
print(c.getH())
#print(c.publico())
c.publico()
c._Cilindro__privado()


