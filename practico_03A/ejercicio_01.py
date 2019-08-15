from ORM import Base,engine,session,Persona
def crear_tabla():
    Persona.__table__.create()


def borrar_tabla():
    Persona.__table__.drop()


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
