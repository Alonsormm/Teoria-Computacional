import random as rd
#regla 1 = (P ->e)
#regla 2 = (P ->0)
#regla 3 = (P ->1)
#regla 4 = (P -> 0P0)
#regla 5 = (P -> 1P1)

#inicio = P


def generar(longitud, longitudReal):
    palindromo="P"
    for numero in range(longitud):
        seleccion = rd.randint(0,1)
        if seleccion == 0:
            lugar = int(len(palindromo)/2)
            palindromo=palindromo[:lugar] + "0" +palindromo[lugar] + "0" + palindromo[lugar+1:] 
            print(palindromo)
        elif seleccion == 1:
            lugar = int(len(palindromo)/2)
            palindromo=palindromo[:lugar] + "1" +palindromo[lugar] + "1" + palindromo[lugar+1:] 
            print(palindromo)

    seleccion = rd.randint(0,2)
    if seleccion == 0 or longitudReal % 2 == 0:
        lugar = int(len(palindromo)/2)
        print(palindromo[:lugar]+"e"+palindromo[lugar+1:])
        palindromo=palindromo[:lugar]+palindromo[lugar+1:]
        
    elif seleccion == 1:
        lugar = int(len(palindromo)/2)
        print(palindromo[:lugar]+"0"+palindromo[lugar+1:])
        palindromo=palindromo[:lugar]+"0"+palindromo[lugar+1:]
    elif seleccion == 2:
        lugar = int(len(palindromo)/2)
        print(palindromo[:lugar]+"1"+palindromo[lugar+1:])
        palindromo=palindromo[:lugar]+"1"+palindromo[lugar+1:]   
    return palindromo
            
        




if __name__ == "__main__":

    print("Generador de Palindromos\nIndique si desea longitud manual o generada\n1.-Manual\n2.-Automatica")
    opcion = int(input())
    if opcion==1:
        print("Indique su longitud")
        longitudReal = int(input())
        longitud = int(longitudReal/2)
        palindromo=generar(longitud, longitudReal)
    else:
        longitud=rd.randint(1,50000)
        palindromo=generar(longitud, longitud)
    print("El palindromo quedaria asi: "+palindromo)

