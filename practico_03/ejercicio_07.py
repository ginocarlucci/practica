# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime
import sqlite3

from practico_03.ejercicio_02 import agregar_persona
from practico_03.ejercicio_06 import reset_tabla
from practico_03.ejercicio_04 import buscar_persona


def agregar_peso(id_persona, fecha, peso):
    db = sqlite3.connect('mibase')
    cursor = db.cursor()
    persona = buscar_persona(id_persona)
    if(persona):
        cSQL = 'SELECT idPersona, Fecha, peso FROM PersonaPeso WHERE idPersona = ? and Fecha > ?'
        data = (id_persona,fecha)
        cursor.execute(cSQL,data)
        db.commit()
        elem = cursor.fetchone()
        if(elem):
            db.close()
            return False
        else:
            cSQL = 'insert into PersonaPeso (idPersona, Fecha, peso) Values (?,?,?)'
            datos = (id_persona,fecha,peso)
            cursor.execute(cSQL,datos)
            id = cursor.lastrowid
            db.commit()
            db.close()
            return id
    else:
        db.close()
        return False

@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, '2018-5-26 00:00:00', 80) > 0
    # id incorrecto
    assert agregar_peso(200, '2018-5-26 00:00:00', 80) == False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, '2018-5-16 00:00:00', 80) == False

if __name__ == '__main__':
    pruebas()
