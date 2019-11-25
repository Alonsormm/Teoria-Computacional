delta={
    "q0":{ "0": ["q1","X", "R"] , "1":None,"X":None,"Y": ["q3","Y","R"], "B":None},
    "q1":{ "0": ["q1","0", "R"], "1":["q2","Y","L"],"X":None,"Y": ["q1","Y","R"], "B":None}, 
    "q2":{ "0": ["q2","0", "L"] , "1":None,"X":["q0","X","R"],"Y": ["q2","Y","L"], "B":None},
    "q3":{ "0": None , "1":None,"X":None,"Y": ["q3","Y","R"], "B":["q4","B","R"]}, 
    "q4":{ "0": None , "1":None,"X":None,"Y": None, "B":None}, 
}

i = 0
cad =input()

estado_actual="q0"
tam = len(cad)
aceptado=0
while True:
    if i == tam:
        aceptado=1
        break
    print("d("+ estado_actual + "," + cad[i] + ")", end ="")
    
    lista=delta[estado_actual][cad[i]]
    if not lista:
        break
    estado_actual=lista[0]
    print(" => ("+ estado_actual + "," + lista[1] + "," + lista[2] + ")")
    cad = cad[:i] + lista[1] + cad[i+1:]
    if lista[2]=="R":
        i+=1
        if i == tam:
            if estado_actual=="q4":
                aceptado=1
                break
            cad+="B"
            tam += 1
    else:
        i-=1

if aceptado==1:
    print("Aceptada")
else:
    print("No aceptada")


