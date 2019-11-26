from pythonds.basic import Stack
import random as rd
from tkinter import *
from tkinter import ttk
import time


#(inicial)q0=(0,no saca,a)->q0      (1,a,no inserta)->q1
#q1=(1,a,no inserta)->q1          (1,z,no inserta)->q2 
#(final)q2=no hace nada
s=Stack()

window = Tk()
window.geometry('600x600')
window.configure(bg = 'beige')
window.title("Generador y analizador de cadenas de la forma L={0^n1^n|n>=1,neR}")
window.resizable(width=False,height=False)
canvas = Canvas(window) 
canvas.create_oval(500, 500, 80, 80,outline = "black", fill = "white",width = 2)
Texto=Text(window, width=61, height=10)
Texto.place(x=10,y=10)
etiqueta = Label(window, text="Aqui se mostrara si se acepto la cadena")
etiqueta.place(x=100,y=180)

Texto.place(x=100,y=10)
arreglo = []
arreglo.append(Button(window, text="0", font="Helvetica 16 bold", height=1, width=1,bg="blue"))
arreglo.append(Button(window, text="0", font="Helvetica 16 bold", height=1, width=1))
arreglo.append(Button(window, text="0", font="Helvetica 16 bold", height=1, width=1))
arreglo.append(Button(window, text="0", font="Helvetica 16 bold", height=1, width=1))
arreglo.append(Button(window, text="0", font="Helvetica 16 bold", height=1, width=1))
arreglo.append(Button(window, text="0", font="Helvetica 16 bold", height=1, width=1))
arreglo.append(Button(window, text="0", font="Helvetica 16 bold", height=1, width=1))
arreglo.append(Button(window, text="0", font="Helvetica 16 bold", height=1, width=1))
arreglo.append(Button(window, text="0", font="Helvetica 16 bold", height=1, width=1))
arreglo.append(Button(window, text="0", font="Helvetica 16 bold", height=1, width=1))
def generar():
    Texto.delete("1.0",END)
    cadena = ""
    numero=rd.randint(1,100)
    for a in range(numero):
        cadena+=str(rd.randint(0,1))
    print(cadena)
    Texto.insert("1.0", cadena)
    return cadena

def evaluar():
    cadena = Texto.get("1.0",END)[:-1]
    print(cadena)
    s.push("z")
    estado_actual="q0"
    contador=0
    for caracter_actual in cadena:
        contador+=1
        if estado_actual=="q0" and caracter_actual=="0":
            arreglo[contador].after(3000, arreglo[contador].place(x=300,y=(500-(contador*45)))) 
            #arreglo[contador].place(x=300,y=(500-(contador*45)))

            s.push("a")
            estado_actual="q0"
            continue
        if not s.isEmpty():
            popeado = s.pop()
            arreglo[contador].after(3000, arreglo[contador].place_forget) 
        if estado_actual=="q0" and caracter_actual=="1" and popeado=="a":
            estado_actual="q1"
        elif estado_actual=="q1" and caracter_actual=="1" and popeado=="a":
            estado_actual="q1"
        else:
            etiqueta.config(text="Asi nos toco vivir")
            return
    if not s.isEmpty():
        popeado = s.pop()
    if estado_actual=="q1" and popeado=="z":
        estado_actual="q2"
    else:
        etiqueta.config(text="Asi nos toco vivir")
        return
    if estado_actual=="q2":
        etiqueta.config(text="Viva Mexico")
    else:
        return




#Texto.insert("1.0", cadena)
opcion1=ttk.Button(window, text='Generar Cadena', command=generar)
opcion1.place(x=0,y=10)
opcion2=ttk.Button(window, text='Evaluar Cadena', command=evaluar)
opcion2.place(x=500,y=10)
ttk.Button(window, text='Salir', command=quit).place(x=510,y=570)


window.mainloop()