import random
from DFA import FiniteAutomata

# Automata de terminacion
q = 3
sigma = ["0", "1"]
q_0 = "q1"
F = ["q3"]
delta = {
    "q1": {"0":"q2", "1":"q1"},
    "q2": {"0":"q2", "1":"q3"},
    "q3": {"0":"q2", "1":"q1"}
}
F_A = FiniteAutomata(q, sigma, delta, q_0, F, True)

print("1.-Ingresar cadena\n2.-Cadena aleatoria")

opc = input("Ingrese opcion deseada: ")

if opc == '1':
  cadena = input("Ingrese la cadena: ")
else:
  cadena = str(bin(random.randrange(10000))[2:])
  print(cadena)

if F_A.prueba(cadena):
  print("La cadena termina con 01")
else:
  print("La cadena no termina con 01")