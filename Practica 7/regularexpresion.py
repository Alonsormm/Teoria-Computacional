import random


###Evaluador de expresion por arbol

class Nodo(object):
    def __init__(self,dato):
        self.dato = dato
        self.izq = None
        self.der = None
    def imprimirNodo(self):
        print(self.dato)
def isCharacter(car):
    if car == "1" or car == "0" or car == "c"  or car == "e":
        return True
    else:
        return False
def isOperant(car):
    if car == "+" or car == '*' or car == 'x':
        return True
def precedence(car):
    if car == '*':
        return 2
    if car == 'x':
        return 1
    return 0
def existOperant(expresion):
    for i in expresion:
        if isOperant(i):
            return True
    return False
def inorder(raiz):
    if raiz == None:
        return
    inorder(raiz.izq)
    raiz.imprimirNodo()
    inorder(raiz.der)
def postorder(raiz):
    if raiz == None:
        return
    inorder(raiz.izq)
    inorder(raiz.der)
    raiz.imprimirNodo()
def expressionToTree(raiz, t):
    if not existOperant(t):
        return Nodo(t)
    tam = len(t)
    if(t[0] == '('):
        if(t[tam-1] == ')'):
            for i in range(tam):
                if t[i] == ')':
                    if(i == tam-1):
                        t = t[1:tam-1]
                    else:
                        break
    temp = 10
    indice = 0
    parentsis = 0
    for i in range(len(t)):
        if t[i] == '(':
            parentsis+=1
        if t[i] == ')':
            parentsis-=1
        if parentsis > 0:
            continue
        if isOperant(t[i]):
            if(precedence(t[i]) < temp):
                temp = precedence(t[i])
                indice = i
    raiz = Nodo(t[indice])
    izquierda = t[:indice]
    derecha = t[indice+1:]
    raiz.izq = expressionToTree(raiz.izq, izquierda)
    raiz.der = expressionToTree(raiz.der,derecha)
    return raiz

class RegEx(object):
    def __init__(self, regex):
        self.regex = regex
        self.regexOriginal = regex
        self.cadenas = []
        self.completarRegEx()
    def isCharacter(self,car):
        if car == "1" or car == "0" or car == "c" or car == "e":
            return True
        else:
            return False
    def completarRegEx(self):
        i = 0
        tam = len(self.regex) - 1
        while(i < tam):
            if self.isCharacter(self.regex[i]) and self.isCharacter(self.regex[i +1]) or self.isCharacter(self.regex[i]) and self.regex[i+1] == '(':  
                self.regex= self.regex[:i+1] + 'x' + self.regex[i+1:]
                tam +=1
            if self.regex[i+1] == '*':
                self.regex= self.regex[:i+2] + 'c' + self.regex[i+2:]
                tam +=1
            i+=1
    def generarCadena(self,raiz, universo = False):
        if isCharacter(raiz.dato):
            return raiz.dato
        if raiz.dato == '+':
            if universo:
                return self.suma(self.universo(self.generarCadena(raiz.izq,True)),self.universo(self.generarCadena(raiz.der,True)))
            return self.suma(self.generarCadena(raiz.izq),self.generarCadena(raiz.der))
        if raiz.dato == 'x':
            if universo:
                return self.producto(self.generarCadena(raiz.izq,True), self.generarCadena(raiz.der, True))
            return self.producto(self.generarCadena(raiz.izq), self.generarCadena(raiz.der))
        if raiz.dato == '*':
            return self.generarCadena(raiz.izq,True)
    ###Operaciones
    def suma(self, a,b):
        rand = random.randint(0,2)
        if rand == 0:
            if a == 'e':
                return ""
            return a
        if rand == 1:
            if b == 'e':
                return ""
            return b
        if rand == 2:
            if a == 'e':
                return b
            if b == 'e':
                return a
            return a+b
    def producto(self, a, b):
        return a+b
    def universo(self,a):
        final = ""
        if a == 'e':
            return ""
        for i in range(random.randint(0,100)):
            final += a
        return final



ExpresionRegular = input()
reg = RegEx(ExpresionRegular)
arbol = Nodo(None)
arbol = expressionToTree(arbol, reg.regex)
for i in range(100):
    print(reg.generarCadena(arbol))