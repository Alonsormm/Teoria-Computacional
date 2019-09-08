import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import numpy as np
n = int(input("Ingrese una n: "))

file = open("datos_3.txt", "w")

cadena = ''

unos = []

def guardarCadenas(cadena, tam,n):
  if tam == n:
    file.write(cadena )
    return
  cadena_0 = cadena+'0'
  cadena_1 = cadena+'1'
  guardarCadenas(cadena_0,tam+1,n)
  guardarCadenas(cadena_1,tam+1,n)
for i in range(n+1):
  guardarCadenas(cadena,0,i)
file.close()
cadTemp = ""
bits = 0
    
print("Cadena generada")
with open("datos_4.txt") as f:
  while True:
    c = f.read(1)
    if not c:
      break
    bits += 1
    cadTemp += c
    if bits == 16:
      unos.append(cadTemp.count("1"))
      cadTemp = ""
      bits = 0
plt.scatter(np.array(range(len(unos))), unos)
unos.clear()
plt.show()