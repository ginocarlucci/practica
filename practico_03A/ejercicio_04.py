# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime
import sqlite3

from ejercicio_01 import reset_tabla,Persona
from ORM import Base,engine,Persona,session
from ejercicio_02 import agregar_persona

def buscar_persona(id_persona):
<<<<<<< HEAD:practico_03A/ejercicio_04.py
    if(session.query(Persona).filter(Persona.idPersona == id_persona).count()==1):
        persona = session.query(Persona).filter(Persona.idPersona == id_persona).first()
        return (persona.idPersona,persona.nombre,persona.fechaNacimiento,persona.DNI,persona.altura)
    else:
        return False

=======
    db = sqlite3.connect('mibase')
    cursor = db.cursor()
    cSQL = 'SELECT * FROM Personas WHERE idPersona = '+str(id_persona)
    cursor.execute(cSQL)
    db.commit()
    elem = cursor.fetchone()
    if(elem):
        return elem
    else:
        return False
>>>>>>> master:practico_03/ejercicio_04.py

@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez',  '1988-05-15 00:00:00', 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()

