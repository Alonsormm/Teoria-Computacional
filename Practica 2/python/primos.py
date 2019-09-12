import matplotlib.pyplot as plt
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
    file.write(cad+" ")
    unos.append(cad.count("1"))
    p = 2
    while p*i <= n:
      nums[p*i] = 1
      p+=1
    x+=1

file.close()
plt.scatter(np.array(range(len(unos))), unos)
plt.xlabel("Numero de Cadena")
plt.ylabel("Numero de 1's")
unos.clear()
plt.show()
