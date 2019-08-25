import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
n = int(input("Ingrese maximo: "))


file = open("datos.txt", "w")
file.write('{')
unos = []
for i in range(3,n+1):
  no_primo = False
  for j in range(2,i):
    if i % j == 0:
      no_primo = True
  if not no_primo:
    print(i)
    bina = str(bin(i)[2:])
    file.write(bina + '')
    unos.append(bina.count("1"))
plt.plot(unos, marker='o')
unos.clear()
plt.show()
file.write('}')
