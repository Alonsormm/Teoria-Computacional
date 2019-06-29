import random

opc = input('1.-Ingresar Potencia\n2.-Potencia aleatoria\n Ingrese la opcion deseada: ')

if opc == '1':
  k = int(input("Ingrese la potencia: "))
else:
  k = random.randrange(30)
  print(k)

file = open("datos.txt", "w")
file.write('{')

cadena = ''

def imprimirCombi(cadena, tam,k):
  if tam == k:
    return
  cadena_1 = cadena+'0'
  cadena_0 = cadena+'1'
  file.write(cadena_1 + ',')
  file.write(cadena_0+ ',')
  imprimirCombi(cadena_0,tam+1,k)
  imprimirCombi(cadena_1,tam+1,k)


imprimirCombi(cadena,0,k)


file.write("}")