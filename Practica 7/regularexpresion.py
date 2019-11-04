import random

class Nodo(object):
    def __init__(self,dato):
        self.dato = dato
        self.izq = None
        self.der = None
    def imprimirNodo(self):
        print(self.dato)

class BinaryTree(object):
    def __init__(self, dato = None):
        self.raiz = Nodo(dato)

class RegEx(object):
    def __init__(self, regex):
        self.regex = regex
        self.regexOriginal = regex
        self.cadenas = []
        self.arbol = BinaryTree()
        self.completarRegEx()
    def isCharacter(self,car):
        if car == "1" or car == "0" or car == "c":
            return True
        else:
            return False
    def completarRegEx(self):
        i = 0
        tam = len(self.regex) - 1
        while(i < tam):
            if self.isCharacter(self.regex[i]) and self.isCharacter(self.regex[i +1]):  
                self.regex= self.regex[:i+1] + 'x' + self.regex[i+1:]
                tam +=1
            if self.regex[i+1] == '*':
                self.regex= self.regex[:i+2] + 'c' + self.regex[i+2:]
                tam +=1
            i+=1
    def generarCadenas(self,raiz):
        if isCharacter(raiz.dato):
            return raiz.dato
        if raiz.dato == '+':
            return self.suma(self.generarCadenas(raiz.izq),self.generarCadenas(raiz.der))
        if raiz.dato == 'x':
            return self.producto(self.generarCadenas(raiz.izq), self.generarCadenas(raiz.der))
        if raiz.dato == '*':
            return self.universo(self.generarCadenas(raiz.izq))
    ###Operaciones
    def suma(self, a,b):
        rand = random.randint(0,2)
        if rand == 0:
            return a
        if rand == 1:
            return b
        if rand == 2:
            return a+b
    def producto(self, a, b):
        return a+b
    def universo(self,a):
        final = ""
        for i in range(random.randint(0,100)):
            final += a
        return final
    
###Evaluador de expresion por arbol
def isCharacter(car):
    if car == "1" or car == "0" or car == "c":
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
        return 0
    return 1
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


regexaa = input()
reg = RegEx(regexaa)
arbol = Nodo(None)
arbol = expressionToTree(arbol, reg.regex)
#inorder(arbol)
print(reg.generarCadenas(arbol))