from pythonds.basic import Stack
import random as rd


#(inicial)q0=(0,no saca,a)->q0      (1,a,no inserta)->q1
#q1=(1,a,no inserta)->q1          (1,z,no inserta)->q2 
#(final)q2=no hace nada

def evaluar(cadena):
    s.push("z")
    estado_actual="q0"
    for caracter_actual in cadena:
        if estado_actual=="q0" and caracter_actual=="0":
            s.push("a")
            estado_actual="q0"
            continue
        if not s.isEmpty():
            popeado = s.pop()
        if estado_actual=="q0" and caracter_actual=="1" and popeado=="a":
            estado_actual="q1"
        elif estado_actual=="q1" and caracter_actual=="1" and popeado=="a":
            estado_actual="q1"
        else:
            print("No se acepta la cadena")
            return
    if not s.isEmpty():
        popeado = s.pop()
    if estado_actual=="q1" and popeado=="z":
        estado_actual="q2"
    else:
        print("No se acepta la cadena")
        return
    if estado_actual=="q2":
        print("Se acepto la cadena")
    else:
        return




def generar():
    cadena = ""
    numero=rd.randint(1,100000)
    for a in range(numero):
        cadena+=str(rd.randint(0,1))
    print(cadena)
    return cadena



if __name__ == "__main__":
    s=Stack()
    print("Generador y analizador de cadenas de la forma L={0^n1^n|n>=1,neR}\nSeleccione Su opcion:\n1.-Generar Cadena\n2.-Analizar Cadena")
    opcion = int(input())
    if opcion==1:
        cadena=generar()
        evaluar(cadena)
    else:
        cadena= input()
        evaluar(cadena)




