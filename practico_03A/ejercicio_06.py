# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

<<<<<<< HEAD:practico_03A/ejercicio_06.py
from ejercicio_01 import borrar_tabla, crear_tabla
from ORM import Base,engine,Persona,session,PersonaPeso

def crear_tabla_peso():
    PersonaPeso.__table__.create()


def borrar_tabla_peso():
    PersonaPeso.__table__.drop()

=======
import datetime
import sqlite3
from practico_03.ejercicio_01 import borrar_tabla, crear_tabla


def crear_tabla_peso():
    db = sqlite3.connect('mibase')
    cursor = db.cursor()
    cSQL = 'CREATE TABLE IF NOT EXISTS PersonaPeso(idPeso INTEGER PRIMARY KEY, idPersona INTEGER ,Fecha date ,peso int, FOREIGN KEY (idPersona) REFERENCES Personas(idPersona))'
    cursor.execute(cSQL)
    db.commit()
    db.close()


def borrar_tabla_peso():
    db = sqlite3.connect('mibase')
    cursor = db.cursor()
    cSQL = 'DROP TABLE IF EXISTS PersonaPeso'
    cursor.execute(cSQL)
    db.commit()
    db.close()
>>>>>>> master:practico_03/ejercicio_06.py

# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
