# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime
import sqlite3

from ejercicio_02 import agregar_persona
from ejercicio_06 import reset_tabla
from ejercicio_04 import buscar_persona
from ORM import Base,engine,Persona,session,PersonaPeso


def agregar_peso(id_persona, fecha, peso):
    if(buscar_persona(id_persona)):
        if(session.query(PersonaPeso).filter(PersonaPeso.fecha>fecha).count()==0):
            personaPeso = PersonaPeso()
            personaPeso.idPersona = id_persona
            personaPeso.fecha = fecha
            personaPeso.peso = peso
            session.add(personaPeso)
            session.commit()
            return personaPeso.idPeso
        else:
            return False
    else:
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
