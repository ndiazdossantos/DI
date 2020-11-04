import modulosPaquetes
from excepciones import Punto,Cilindro
modulosPaquetes.funcion()

#definimos una clase
clase = modulosPaquetes.UnhaClase()

#punto = excepciones.Punto(2,-3)
punto = Punto(2, -3)
cil = Cilindro(3, 4, 5)

"""o tambien puedo traerme la funcion con

from modulosPaquetes import funcion
funcion()

"""

if __name__ == "__main__":
    c = Cilindro(3, 4, 5)