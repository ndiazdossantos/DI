import math


class CoordenadaNegativaError(Exception):
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return "Erro nas coordenadas, o valor non pode ser negativo "+self.valor


class Punto:
    """Clase que define un punto"""

    def __init__(self, x=0, y=0):
        """Punto coordenadas X>0 Y>0"""
        try:

            if x >= 0:
                self.x = x
            else:
                raise CoordenadaNegativaError("Clase Punto")

            if y >= 0:
                self.y = y
            else:
                raise CoordenadaNegativaError("Clase Punto")
       #capturamos la excepcion
        except CoordenadaNegativaError as erro:
            print("Erro na clase punto"+str(erro))
        else:
            print("Neste caso non existe a excepción")
        finally:
            print("Se executa sempre haxa ou non excepcion")


p1 = Punto(1, 1)
p2 = Punto(-1, 3)


class Circulo (Punto):
    def __init__(self, x=0, y=0, r=1):
        Punto.__init__(self, x, y)
        self.r = r

    def superficie(self):
        return math.pi*self.r**2

    def perimetro(self):
        return 2*math.pi*self.r


class Altura:
    def __init__(self, h=1):
        self.h = h


class Cilindro(Circulo, Altura):
    def __init__(self, x=0, y=0, r=1, h=1):
        Circulo.__init__(self, x, y, r)
        Altura.__init__(self, h)

    def volume(self):
        return Circulo.superficie(self)*self.h

    def superficie(self):
        return Circulo.superficie(self)*2+self.h*self.perimetro()

    def __privado(self):
        print("Metodo privado")

    def publico(self):
        self.__privado()