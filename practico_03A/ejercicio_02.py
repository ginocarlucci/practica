# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import datetime
<<<<<<< HEAD:practico_03A/ejercicio_02.py

from ejercicio_01 import reset_tabla,Persona
from ORM import Base,engine,Persona,session

def agregar_persona(nombre, nacimiento, dni, altura):
    persona = Persona()
    persona.nombre = nombre
    persona.fechaNacimiento = nacimiento
    persona.DNI = dni
    persona.altura = altura
    session.add(persona)
    session.commit()
    return persona.idPersona
=======
import sqlite3
from practico_03.ejercicio_01 import reset_tabla

def agregar_persona(nombre, nacimiento, dni, altura):
    db = sqlite3.connect('mibase')
    cursor = db.cursor()
    cSQL = 'INSERT INTO Personas(nombre,fechaNacimiento,DNI,altura) VALUES(?,?,?,?)'
    datos = ( nombre, nacimiento, dni, altura )
    cursor.execute(cSQL, datos)
    id = cursor.lastrowid
    db.commit()
    db.close()
    return id
>>>>>>> master:practico_03/ejercicio_02.py


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()
