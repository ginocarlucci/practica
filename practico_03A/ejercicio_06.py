# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.


from ejercicio_01 import borrar_tabla, crear_tabla
from ORM import Base,engine,Persona,session,PersonaPeso

def crear_tabla_peso():
    PersonaPeso.__table__.create()


def borrar_tabla_peso():
    PersonaPeso.__table__.drop()

# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
