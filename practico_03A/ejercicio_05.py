# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

import datetime

from ejercicio_01 import reset_tabla,Persona
from ORM import Base,engine,Persona,session
from ejercicio_02 import agregar_persona
from ejercicio_04 import buscar_persona


def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
    if (session.query(Persona).filter(Persona.idPersona == id_persona).count() == 1):
        persona = session.query(Persona).filter(Persona.idPersona == id_persona).first()
        persona.nombre = nombre
        persona.fechaNacimiento = nacimiento
        persona.DNI = dni
        persona.altura = altura
        session.add(persona)
        session.commit()
        return True
    else:
        return False

@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    #en la linea a continuacion me parecio que tendria q aparecer un assert, si no es asi la linea original era
    #   actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181) is False

if __name__ == '__main__':
    pruebas()
