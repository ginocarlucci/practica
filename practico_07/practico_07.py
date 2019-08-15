"""
Tp7 – Capa Presentacion Socios

Crear en Python usando Tkinter un formulario para gestionar los datos de Socios usando la Clase de la Capa de Negocio Socios .

El Formulario principal tiene que mostrar todos los socios en Treeview y tener los siguientes botones Alta , Baja , Modificar .

Apretar el Boton Alta se tiene que abrir un formulario con los campos para ingresar los datos de socio .
Incluye  2 botones Guardar y Cancelar.

Apretar el Boton Baja se tiene que dar de baja el socio seleccionado .

Apretar el Boton Modificar se tiene que abrir un formulario con los campos con los datos del socio seleccionado .
Incluye 2 botones Aceptar y Cancelar .
"""

from tkinter import *
from practico_06 import capa_negocio
from tkinter import ttk
import tkinter as tk
from practico_05.ejercicio_01 import Socio

def alta():
    e = Toplevel(root)
    e.title("Ingresar nuevo Socio")
    e.geometry('380x200')
    Label(e, text="Ingrese el Dni").grid(column=0, row=0)
    dni = IntVar()
    Entry(e, textvariable=dni).grid(column=1, row=0)

    Label(e, text="Ingrese el nombre").grid(column=0, row=1)
    nombre = StringVar()
    Entry(e, textvariable=nombre).grid(column=1, row=1)

    Label(e, text="Ingrese el apellido").grid(column=0, row=2)
    apellido = StringVar()
    Entry(e, textvariable=apellido).grid(column=1, row=2)

    Button(e, text="Guardar", command=lambda: guardar(dni,nombre,apellido)).grid(column=0, row=4)

    def guardar(dni,nombre,apellido):
        socio = Socio(dni=dni.get(), nombre=nombre.get(), apellido=apellido.get())
        socioNegocio = capa_negocio.DatosSocio()
        socioNegocio.alta(socio)
        socio = socioNegocio.buscar_dni(dni.get())
        tree.insert("", tk.END, text=socio.id, values=(socio.dni, socio.apellido, socio.nombre))
        e.destroy()

def baja():
    item = tree.selection()[0]
    idSocio = tree.item(item,option="text")
    socioNegocio = capa_negocio.DatosSocio()
    socioNegocio.baja(idSocio)
    tree.delete(item)

def modificacion():
    item = tree.selection()[0]
    idSocio = tree.item(item, option="text")
    socioNegocio = capa_negocio.DatosSocio()
    socio = socioNegocio.buscar(idSocio)
    print(socio.id)

    e = Toplevel(root)
    e.title("Ingresar nuevo Socio")
    e.geometry('380x200')
    Label(e, text="Ingrese el Dni").grid(column=0, row=0)
    dni = IntVar()
    dni.set(socio.dni)
    Entry(e, textvariable=dni).grid(column=1, row=0)

    Label(e, text="Ingrese el nombre").grid(column=0, row=1)
    nombre = StringVar()
    nombre.set(socio.nombre)
    Entry(e, textvariable=nombre).grid(column=1, row=1)

    Label(e, text="Ingrese el apellido").grid(column=0, row=2)
    apellido = StringVar()
    apellido.set(socio.apellido)
    Entry(e, textvariable=apellido).grid(column=1, row=2)

    Button(e, text="Guardar", command=lambda: guardar(dni, nombre, apellido)).grid(column=0, row=4)

    def guardar(dni,nombre,apellido):
        socio.dni = dni.get()
        print(socio.dni)
        socio.nombre = nombre.get()
        socio.apellido = apellido.get()
        socioNegocio.modificacion(socio)
        tree.item(item,text=socio.id, values=(socio.dni,socio.apellido,socio.nombre))
        e.destroy()


root = Tk();
root.title("ABM Socios")

columnas = 4;
negocioSocio = capa_negocio.NegocioSocio()
totalSocios = negocioSocio.todos()
filas = len(totalSocios)

tree=ttk.Treeview()
tree["columns"]=("nombre","apellido","DNI")

tree.heading("#0", text="ID");
tree.heading("nombre", text="DNI");
tree.heading("apellido", text="Apellido");
tree.heading("DNI", text="Nombre");

for i in totalSocios:
    tree.insert("",tk.END, text=i.id, values=(i.dni,i.apellido,i.nombre))

tree.pack()

Button(root,text = "Alta",command=alta).pack(side=LEFT)
Button(root,text = "Baja",command=baja).pack(side=LEFT)
Button(root,text = "Modificacion",command=modificacion).pack(side=LEFT)

root.mainloop()
