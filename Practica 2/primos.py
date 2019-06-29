import random


print("1.-Ingresar un maximo\n2.-Generar un maximo\n")
opc = input("Ingrese la opcion deseada: ")

if opc == '1':
  n = int(input("Ingrese maximo: "))
else:
  n = random.randrange(2,1000)
  print(n)

file = open("datos.txt", "w")
file.write('{')

for i in range(3,n+1):
  no_primo = False
  for j in range(2,i):
    if i % j == 0:
      no_primo = True
  if not no_primo:
    file.write(str(i) + ',')

file.write('}')
