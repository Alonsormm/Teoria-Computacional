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
window.title("Generador y analizador de cadenas de la forma L={0^n1^n|n>=1,neR}")
window.resizable(width=False,height=False)
canv = Canvas(window,width=600,height=600)

Texto=Text(window, width=49, height=10)
Texto.place(x=10,y=10)
etiqueta = Label(window, text="Aqui se mostrara si se acepto la cadena")
etiqueta.place(x=10,y=180)
etiqueta2 =Label(window, text="Aqui se mostrara como se va evaluando la cadena")
etiqueta2.place(x=10,y=210)




canv.pack() 
xspeed=5
yspeed=0

Texto.place(x=100,y=10)

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
    y1=540
    y2=545
    aux=0
    
    cadena_imprimir="La cadena se esta evaluando asi: "
    if len(cadena)>60:
        etiqueta2.config(text="Tu cadena es muy grande, no se mostrara animacion, unicamente se te dira si se acepta o no")
    else:
        canv.create_rectangle(300, 200, 400, 550, width=0, fill='black')
        #for a in range(0,60):
            #canv.create_rectangle(305, 540, 395, 545, width=0, fill='red')
            #canv.create_rectangle(305, 535, 395, 539, width=0, fill='red')
            #canv.create_rectangle(305, 529, 395, 534, width=0, fill='red')
            #canv.create_rectangle(305, y1, 395, y2, width=0, fill='red')
            #y1=529
            #y2=534
            #canv.create_rectangle(305, 529, 395, 534, width=0, fill='red')
            #canv.create_rectangle(305, 535, 395, 539, width=0, fill='red')
            #canv.create_rectangle(305, 540, 395, 545, width=0, fill='red')
#
            #canv.create_rectangle(305, y1, 395, y2, width=0, fill='red')
#
            #canv.create_rectangle(305, y2+1, 395, y2+10, width=0, fill='red')
            #aux=y1
            #y1=y2+1
            #y2=aux+10

    for caracter_actual in cadena:
        cadena_imprimir+=caracter_actual

        window.update()
        if len(cadena)<=60:
            etiqueta2.config(text=cadena_imprimir)
        time.sleep(.5)
        if estado_actual=="q0" and caracter_actual=="0":
            if len(cadena)<60:
                canv.create_rectangle(305, y1, 395, y2, width=0, fill='red')

            s.push("a")
            estado_actual="q0"
            aux=y1
            y1=y2-10
            y2=aux-1
            continue
        if not s.isEmpty():
            popeado = s.pop()

        if estado_actual=="q0" and caracter_actual=="1" and popeado=="a":
            aux=y1
            y1=y2+1
            y2=aux+10
            if len(cadena)<60:
                canv.create_rectangle(305, y1, 395, y2, width=0, fill='black')
            estado_actual="q1"
        elif estado_actual=="q1" and caracter_actual=="1" and popeado=="a":
            if len(cadena)<60:
                canv.create_rectangle(305, y1, 395, y2, width=0, fill='black')
            estado_actual="q1"
        else:
            etiqueta.config(text="No se acepta la cadena")
            return
        aux=y1
        y1=y2+1
        y2=aux+10
    window.update()
    if not s.isEmpty():
        popeado = s.pop()
        if len(cadena)<60:
            canv.create_rectangle(305, 540, 395, 545, width=0, fill='black')
    if estado_actual=="q1" and popeado=="z":
        estado_actual="q2"
    else:
        etiqueta.config(text="No se acepta la cadena")
        return
    if estado_actual=="q2":
        etiqueta.config(text="Se acepta la cadena")
    else:
        return




opcion1=ttk.Button(window, text='Generar Cadena', command=generar)
opcion1.place(x=0,y=10)
opcion2=ttk.Button(window, text='Evaluar Cadena', command=evaluar)
opcion2.place(x=500,y=10)
ttk.Button(window, text='Salir', command=quit).place(x=510,y=570)


window.mainloop()
