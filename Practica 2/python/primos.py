import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import numpy as np
n = int(input("Ingrese maximo: "))

x = 0
prims = [0] * (n+1)
nums = [0] * (n+1)
file = open("datos.txt", "w")
unos = []
for i in range(2,n+1):
  if nums[i] != 1 or i == 2:
    prims[0] = i
    cad = str(bin(i)[2:])
    file.write(cad+"\n")
    unos.append(cad.count("1"))
    p = 2
    while p*i <= n:
      nums[p*i] = 1
      p+=1
    x+=1


plt.scatter(np.array(range(len(unos))), unos)
unos.clear()
plt.show()
