# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.
import sqlite3
import datetime

from ejercicio_01 import reset_tabla,Persona
from ORM import Base,engine,Persona,session
from ejercicio_02 import agregar_persona


def borrar_persona(id_persona):
    if(session.query(Persona).filter(Persona.idPersona == id_persona).count()==1):
        session.query(Persona).filter(Persona.idPersona == id_persona).delete()
        session.commit()
        return True
    else:
        return False

@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()


