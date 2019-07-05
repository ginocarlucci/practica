# Implementar los metodos de la capa de negocio de socios.

from practico_05.ejercicio_01 import Socio
from practico_05.ejercicio_02 import DatosSocio


class DniRepetido(Exception):
    pass


class LongitudInvalida(Exception):
    pass


class MaximoAlcanzado(Exception):
    pass


class NegocioSocio(object):

    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 200

    def __init__(self):
        self.datos = DatosSocio()

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return DatosSocio.buscar(id_socio)

    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return DatosSocio.buscar_dni(dni_socio)

    def todos(self):
        """
        Devuelve listado de todos los socios.
        :rtype: list
        """
        return DatosSocio.todos(self)

    def alta(self, socio):
        """
        Da de alta un socio.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type socio: Socio
        :rtype: bool
        """
        return DatosSocio.alta(socio)

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        return DatosSocio.baja(id_socio)

    def modificacion(self, socio):
        """
        Modifica un socio.
        Se debe validar la regla 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type socio: Socio
        :rtype: bool
        """
        return DatosSocio.modificacion(socio)

    def regla_1(self, socio):
        """
        Validar que el DNI del socio es unico (que ya no este usado).
        :type socio: Socio
        :raise: DniRepetido
        :return: bool
        """
        if(DatosSocio.buscar_dni(socio.dni)==socio.dni):
            raise DniRepetido("El dni ya se encuentra en uso")
            return False
        else:
            return True

    def regla_2(self, socio):
        """
        Validar que el nombre y el apellido del socio cuenten con mas de 3 caracteres pero menos de 15.
        :type socio: Socio
        :raise: LongitudInvalida
        :return: bool
        """
        nombre = 0
        apellido = 0
        for letra in socio.nombre:
            nombre+=1
        for letra in socio.apellido:
            apellido+=1

        if(nombre<self.MIN_CARACTERES):
            raise LongitudInvalida("El nombre tiene menos de 3 caracteres")
            return False
        elif(nombre>self.MAX_CARACTERES):
            raise LongitudInvalida("El nombre tiene mas de 15 caracteres")
            return False
        elif(apellido<self.MIN_CARACTERES):
            raise LongitudInvalida("El apellido tiene menos de 3 caracteres")
            return False
        elif(apellido>self.MAX_CARACTERES):
            raise LongitudInvalida("El apellido tiene mas de 15 caracteres")
            return False
        else:
            return True

    def regla_3(self):
        """
        Validar que no se esta excediendo la cantidad maxima de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """
        i = 0
        socios = DatosSocio.todos(self)
        for s in socios:
            i+=1
        if(i<=self.MAX_SOCIOS):
            return True
        else:
            raise MaximoAlcanzado("Se supero el limite de socios registrados")
            return False
