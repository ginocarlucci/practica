## 2 Ejercicio Hacer un formulario en Tkinter una calculadora que tenga 1 entry y 12 botones para los dígitos 0 al 9
## y las operaciones + - / * = , que al apretar cada botón vaya agregando al valor que muestra en el entry el carácter 
## que le corresponde ( como se ve imagen ) y cuando se aprieta en = pone el resultado de evaluar la cadena entrada . 

from tkinter import *
total1 = 0
operador = ""
def click(boton):
    global total1
    global operador
    if(boton == "="):
        if(operador == "+"):
            total.set(total1 + float(total.get()[total.get().find("+"):]))
        elif(operador=="-"):
            total.set(total1 - float(total.get()[total.get().find("-"):]))
        elif(operador=="/"):
            total.set(total1 / float(total.get()[total.get().find("/"):]))
        elif(operador=="*"):
            total.set(total1 * float(total.get()[total.get().find("*"):]))
    elif(boton == "Ce"):
        total.set("")
    else:
        if(len(total.get())>0):
            if(boton=="+"):
                total.set(total.get() + boton)
                op = total.get().find("+")
                total1 = float(total.get()[0:op])
                operador = "+"
            elif(boton=="-"):
                total.set(total.get() + boton)
                op = total.get().find("-")
                total1 = float(total.get()[0:op])
                operador = "-"
            elif (boton == "/"):
                total.set(total.get() + boton)
                op = total.get().find("/")
                total1 = float(total.get()[0:op])
                operador = "/"
            elif (boton == "*"):
                total.set(total.get() + boton)
                op = total.get().find("*")
                total1 = float(total.get()[0:op])
                operador = "*"
            else:
                total.set(total.get()+boton)
        else:
            total.set(boton)

root = Tk()
root.title("Calculadora")
total = StringVar()
vp = Frame(root)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
Entry(vp,text = "total",textvariable = total).grid(column = 0, row = 0)

vp2 = Frame(root)
vp2.grid(column=0, row=1, padx=(50,50), pady=(10,10))

Button(vp2,text = "7",command = lambda : click("7")).grid(column = 0,row=1)
Button(vp2,text = "8",command = lambda : click("8")).grid(column = 1,row=1)
Button(vp2,text = "9",command = lambda : click("9")).grid(column = 2,row=1)
Button(vp2,text = "/",command = lambda : click("/")).grid(column = 3,row=1)
Button(vp2,text = "4",command = lambda : click("4")).grid(column = 0, row=2)
Button(vp2,text = "5",command = lambda : click("5")).grid(column = 1, row=2)
Button(vp2,text = "6",command = lambda : click("6")).grid(column = 2, row=2)
Button(vp2,text = "*",command = lambda : click("*")).grid(column = 3, row=2)
Button(vp2,text = "1",command = lambda : click("1")).grid(column = 0, row=3)
Button(vp2,text = "2",command = lambda : click("2")).grid(column = 1, row=3)
Button(vp2,text = "3",command = lambda : click("3")).grid(column = 2, row=3)
Button(vp2,text = "-",command = lambda : click("-")).grid(column = 3, row=3)
Button(vp2,text = ".",command = lambda : click(".")).grid(column = 0, row=4)
Button(vp2,text = "0",command = lambda : click("0")).grid(column = 1, row=4)
Button(vp2,text = "=",command = lambda : click("=")).grid(column = 2, row=4)
Button(vp2,text = "+",command = lambda : click("+")).grid(column = 3, row=4)
Button(vp2,text = "Ce",command = lambda : click("Ce")).grid(column = 4, row=4)

root.mainloop()