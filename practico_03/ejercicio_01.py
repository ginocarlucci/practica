# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.
import sqlite3

def crear_tabla():
    db=sqlite3.connect('mibase')
    cur=db.cursor()
    cSQL='CREATE TABLE IF NOT EXISTS personas(id INTEGER PRIMARY KEY ASC, nombre TEXT(30), fecha_nacimiento date, dni int(11), altura int(11))'
    cur.execute(cSQL)
    db.commit()
    db.close()



def borrar_tabla():
    db=sqlite3.connect('mibase')
    cur=db.cursor()
    cSQL = 'DROP TABLE IF EXISTS personas'
    cur.execute(cSQL)
    db.commit()
    db.close()


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        '''borrar_tabla()'''
    return func_wrapper
