import sqlite3 as dbapi

# print(dbapi.apilevel)
# print(dbapi.threadsafety)
# print(dbapi.paramstyle)
try:
    bbdd = dbapi.connect("baseDatos.dat")
    print(bbdd)
except dbapi.Error as e:
    print(e)
else:
    print("Base de datos aberta")

try:
    cursor = bbdd.cursor()
    print(cursor)
except dbapi.Error as e:
    print(e)
else:
    print("Cursor preparado")

try:
    # cursor.execute("create table usuarios (dni text, nome text, direccion text)")
    # cursor.execute("insert into usuarios values ('1234a', 'Noe', 'calle 123')")
    # cursor.execute("insert into usuarios values ('1234b', 'Marcos', 'calle 124')")
    # cursor.execute("""insert into usuarios values ('1235a', 'Sergi', 'calle 127')""")
    bbdd.commit()
except dbapi.DatabaseError as e:
    print("Erro insertando os datos: "+str(e))
else:
    print("Base de datos creada")

try:
    cursor.execute("select * from usuarios")
    # fetchone a seguinte tupla
    # fetchall devolta un obxecto iterable con todalas tuplas
    # fetchmany numero de tuplas pasado por parametro
    for fila in cursor.fetchall():
        # print(fila)
        print("Nome: " + fila[1])
        print("DNI: " + fila[0])
        print("Direccion: " + fila[2])
except dbapi.DatabaseError as e:
    print("Erro facendo a consulta: "+str(e))
else:
    print("Consulta executada")

try:
    dni = input("Introduce o DNI")
    consulta = "select * from usuarios where dni = '"+dni+"'"
    cursor.execute(consulta)
    for fila in cursor.fetchall():
        print(fila)

except dbapi.Error as e:
    print(e)
else:
    print("Consulta executada 2")
finally:
    cursor.close()
    bbdd.close()
