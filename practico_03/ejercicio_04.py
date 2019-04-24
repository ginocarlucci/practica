# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import sqlite3
import datetime

from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    db=sqlite3.connect('mibase')
    cur=db.cursor()
    cSQL='SELECT id, nombre, fecha_nacimiento, dni, altura from personas where id='+str(id_persona)
    cur.execute(cSQL)
    db.commit()
    if(cur.fetchone()):
        for i in cur:
            id = i[0]
            nombre = i[1]
            nacimiento = i[2]
            dni = i[3]
            altura = i[4]
            print(id,nombre,nacimiento,dni,altura)
        #id = cur.execute('select id from personas where id='+str(id_persona))
        #nombre = cur.execute('select nombre from personas where id='+str(id_persona))
        #nacimiento = cur.execute('select nacimiento from personas where id='+str(id_persona))
        #dni = cur.execute('select dni from personas where id='+str(id_persona))
        #altura = cur.execute('select altura from personas where id='+str(id_persona))
        return(id,nombre,nacimiento,dni,altura)
    db.close()
    return False


juan= agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
buscar_persona(juan)

'''

@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
'''
