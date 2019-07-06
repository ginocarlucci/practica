# Implementar los casos de prueba descriptos.

import unittest

from practico_05.ejercicio_01 import Socio
from practico_06.capa_negocio import NegocioSocio, LongitudInvalida, DniRepetido, MaximoAlcanzado


class TestsNegocio(unittest.TestCase):

    def setUp(self):
        super(TestsNegocio, self).setUp()
        self.ns = NegocioSocio()

    def tearDown(self):
        super(TestsNegocio, self).tearDown()
        self.ns.datos.borrar_todos()

    def test_alta(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # ejecuto la logica
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)

        # post-condiciones: 1 socio registrado
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 1)

    def test_regla_1(self):
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)

        valido = Socio(dni=12345672, nombre='raul', apellido='valido')
        self.assertTrue(self.ns.regla_1(valido))

        # DNI repetido
        invalido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertRaises(DniRepetido, self.ns.regla_1, invalido)

    def test_regla_2_nombre_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='J', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_nombre_mayor_15(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='Juanaguilar35231', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='P')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_mayor_15(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='Perezguimenes23512')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_3(self):
        usuariosRegistrados = len(self.ns.todos())
        usuariosAAgregar = self.ns.MAX_SOCIOS-usuariosRegistrados

        self.assertTrue(self.ns.regla_3)

        for i in range(usuariosAAgregar+1):
            socio = Socio(dni=12345679+i, nombre='Juan', apellido='Perez')
            exito = self.ns.alta(socio)

        self.assertRaises(MaximoAlcanzado,self.ns.regla_3)

    def test_baja(self):
        socio = Socio(dni=45345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)
        usuariosRegistrados = len(self.ns.todos())
        respuesta = self.ns.baja(self.ns.buscar_dni(socio.dni).id)
        self.assertTrue(respuesta)
        self.assertEqual(len(self.ns.todos()), (usuariosRegistrados-1))

    def test_buscar(self):
        """no se como obtener el id del usuario recien generado, por eso utilizo la funcion buscar_dni para obtenerlo"""
        soc = Socio(dni=45345678, nombre='Juan', apellido='Perez')
        self.ns.alta(soc)
        socioABuscar = self.ns.buscar_dni(soc.dni)
        self.assertEqual(self.ns.buscar(socioABuscar.id),socioABuscar)

    def test_buscar_dni(self):
        socio = Socio(dni=45345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)
        self.assertEqual((self.ns.buscar_dni(socio.dni)).dni, socio.dni)

    def test_todos(self):
        socio = Socio(dni=45345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)
        socio = Socio(dni=45345679, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)
        socio = Socio(dni=45345677, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)
        self.assertEqual(len(self.ns.todos()),3)

    def test_modificacion(self):
        socio = Socio(dni=45345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)
        socio = self.ns.buscar_dni(socio.dni)
        socio.dni=45345672
        socio.nombre='Raul'
        socio.apellido='Rodriguez'
        self.ns.modificacion(socio)

        self.assertEqual(self.ns.buscar(socio.id).dni, socio.dni)

