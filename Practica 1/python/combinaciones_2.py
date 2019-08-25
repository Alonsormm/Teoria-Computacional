import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import numpy as np
n = int(input("Ingrese una n: "))

file = open("datos_2.txt", "w")
file.write('{E')

cadena = ''

unos = []

def guardarCadenas(cadena, tam,n):
  if tam == n:
    file.write(cadena + ',')
    unos.append(cadena.count("1"))
    return
  cadena_0 = cadena+'0'
  cadena_1 = cadena+'1'
  guardarCadenas(cadena_0,tam+1,n)
  guardarCadenas(cadena_1,tam+1,n)
for i in range(n+1):
  guardarCadenas(cadena,0,i)
file.write("}")
file.close()
print("Cadena generada")
plt.plot(unos, marker='o')
unos.clear()
plt.show()

