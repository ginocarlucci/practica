## 2 Ejercicio Hacer un formulario en Tkinter una calculadora que tenga 1 entry y 12 botones para los dígitos 0 al 9
## y las operaciones + - / * = , que al apretar cada botón vaya agregando al valor que muestra en el entry el carácter 
## que le corresponde ( como se ve imagen ) y cuando se aprieta en = pone el resultado de evaluar la cadena entrada . 

from tkinter import *
def sumar():
    pass
def restar():
    pass
def multiplicar():
    pass
def dividir():
    pass
def uno():
    pass


root = Tk()
root.title("Calculadora")
total = DoubleVar()
vp = Frame(root)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
Entry(vp,text = "total",textvariable = total).grid(column = 0, row = 0)

vp2 = Frame(root)
vp2.grid(column=0, row=1, padx=(50,50), pady=(10,10))

Button(vp2,text = "7",command = uno).grid(column = 0,row=1)
Button(vp2,text = "8",command = uno).grid(column = 1,row=1)
Button(vp2,text = "9",command = uno).grid(column = 2,row=1)
Button(vp2,text = "4",command = uno).grid(column = 0, row=2)
Button(vp2,text = "5",command = uno).grid(column = 1, row=2)
Button(vp2,text = "6",command = uno).grid(column = 2, row=2)
Button(vp2,text = "1",command = uno).grid(column = 0, row=3)
Button(vp2,text = "2",command = uno).grid(column = 1, row=3)
Button(vp2,text = "3",command = uno).grid(column = 2, row=3)
root.mainloop()