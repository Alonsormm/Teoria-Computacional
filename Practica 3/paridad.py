import random
from DFA import FiniteAutomata


#Automata de paridad
q = 4
sigma = [0,1]
q_0 = ["q1"]
F = ["q1"]
delta={
        "q1":["q2", "q4"],
        "q2":["q1", "q3"],
        "q3":["q4", "q2"],
        "q4":["q3", "q1"]
        }
F_A = FiniteAutomata(q,sigma,delta,q_0,F)



print("1.-Ingresar cadena\n2.-Cadena aleatoria")

opc = input("Ingrese opcion deseada: ")

if opc == '1':
  cadena = input("Ingrese la cadena: ")
else:
  cadena = str(bin(random.randrange(10000))[2:])
  print(cadena)


print(F_A.prueba(cadena))