class Data():
    def __init__(self):
     self.__dia = 1

    def getDia(self):
        return self.__dia

    def setDia(self,dia):
        if dia>0 and dia<=31:
            self.__dia=dia
        else:
          print("Erro insertando a data")

    dia = property(getDia, setDia)

    def __str__(self):
        return object.__str__(self)+" Pero isto que é!"
    #dia = property(getDia,setDia)

    def __cmp__(self,outro):
        if self.__dia == outro.dia:
            return 0
        elif  self.__dia>outro.dia:
            return 1
        elif self.__dia > outro.dia:
            return -1

    def __len__(self):
        return 10


data = Data()
data.setDia(45)
data.setDia(15)

print(data.getDia())

data.dia = "catorce"
print(data.dia)

print(data.dia)
data.__dia=60
print(data.__dia)


print(data.getDia())
print(data)

if data3.__cmp__(data2):
    print(" data3 é data2 son iguais")
else:
    print(" data2 son distintos")

print(len(data))
t = 2,3,4
print(len(t))

"""
__init__(self,args)
__new__(cls,args)                       contructor, se ejecuta antes de init, le pasamos como parametros la clase
__del__(self)
__str__(self)
__cmp__(self,otro)
"""

