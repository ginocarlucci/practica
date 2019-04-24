# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import sqlite3
import datetime

from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_01 import borrar_tabla


def agregar_persona(nombre, nacimiento, dni, altura):
    db=sqlite3.connect('mibase')
    cur=db.cursor()
    cSQL = 'INSERT INTO personas(nombre,fecha_nacimiento, dni, altura) VALUES(?,?,?,?)'
    tdatos=(nombre,nacimiento,dni,altura)
    cur.execute(cSQL,tdatos)
    id=cur.lastrowid
    db.commit()
    db.close()
    return id


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()


'''db=sqlite3.connect('mibase')
cur=db.cursor()
cSQL='SELECT * FROM personas'
cur.execute(cSQL)
lista=cur.fetchall()
for row in lista:
    print(row)
db.commit()
db.close()
'''
