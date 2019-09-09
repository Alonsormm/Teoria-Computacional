from DFA import FiniteAutomata
import string
import random
import progressbar
import time
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
F_A = FiniteAutomata(q,sigma,delta,q_0,F,True)

numCadenas = int(input("Ingrese el numero de cadenas que desea generar: "))
tamCadenas = int(input("Ingrese el tamaño de las cadenas: "))

while random.randint(0,1):
  file = open("datos.txt", "w")
  print("El protocolo inicio!")
  print("Generando cadenas!")
  for i in progressbar.progressbar(range(numCadenas)):
    cadTemp = ""
    for j in range(tamCadenas):
      cadTemp += str(random.randint(0,1))
    file.write(cadTemp+ "\n")
  file.close()
  print("Se generaron las cadenas!")
  file = open("datos.txt", "r")
  print("Probando las cadenas!")
  for i in progressbar.progressbar(range(numCadenas)):
      line = file.readline()
      F_A.prueba(line[:-1])
  print("Cadenas probadas!")
  file.close()
  print("2s Timeout")
  time.sleep(2)

print("Fin de los protocolos")