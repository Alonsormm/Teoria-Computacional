import random
from DFA import FiniteAutomata
import threading

#Automata de paridad
q = 4
sigma = ["0", "1"]
q_0 = "q1"
F = ["q1"]
delta={
        "q1":{"0":"q2", "1":"q4"},
        "q2":{"0":"q1", "1":"q3"},
        "q3":{"0":"q4", "1":"q2"},
        "q4":{"0":"q3", "1":"q1"}
        }
F_A = FiniteAutomata(q, sigma, delta, q_0, F)

# Menu

print("1.-Ingresar N\n2.-Generar N")

opc = input("Ingrese opcion deseada: ")

if opc == '1':
    n = int(input("Ingrese N: "))
else:
    n = random.randrange(100)
    print(n)

# Volado para saber que protocolo usar


def generador(identificador):
    archivo = open("Datos/Protocolo_paridad" +
                   str(identificador) + ".txt" , "w")
    for i in range(1000):
        rand = random.randrange(10000)
        binary = str(bin(rand)[2:])
        if F_A.prueba(binary):
            archivo.write("Par: " + binary + "\n\n")
        else:
            archivo.write("Impar: " + binary + "\n\n")


for i in range(n):
    if random.randint(0, 1) == 1:
        print("\nPrueba" + str(i+1) + ": Protocolo " + str(i) + " corriendo.")
        t = threading.Thread(target=generador, args=(i,))
        t.start()
        t.join()
    else:
        print("\nPrueba" + str(i+1) + ": El prototocolo no inicio")
