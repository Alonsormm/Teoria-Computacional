# Automata mejorado

from graphviz import Digraph


class FiniteAutomata(object):

    "Clase que representa al automata finito"

    def __init__(self, num_Q, sigma, delt, q_0, F, guardarPasos=False):
        """
            Q: Conjunto finito llamado "de estados" #Numero de estados (Int)
            sigma : Conjunto finito llamado Alfabeto #Lista de un alfabeto(List<Int or Strings>)
            delta : Funcion de transicion tal que Q x sigma => Q #Diccionario de diccionarios
            q_0 : Estado inicial #
            F:  Estados de aceptacion (List<String>)
            guardarPasos: Guardar los pasos del automata en un archivo de texto(Opcional bool)
            Eg. Automata de paridad
            q = 4
            sigma = ["0", "1"]
            q_0 = "q1"
            F = ["q1"]
            delta={
                    "q1":{"0":"q2", "1":"q4"},
                    "q2":{"0":"q1", "1":"q3"},
                    "q3":{"0":"q4", "1":"q2"},
                    "q4":{"0":"q3", "1":"q1"}
                    }
            F_A = FiniteAutomata(q,sigma,delta,q_0,F)
        """

        Q_list = []
        self.delta = {}
        for i in range(num_Q+1):
            Q_list.append("q"+str(i))

        self.Q = Q_list
        self.sigma = sigma
        self.delta = delt


        self.nombreEstados = {
            "q5":"auto",
            "q10":"break",
            "q14":"case",
            "q17":"char",
            "q21":"const",
            "q26":"continue",
            "q33":"default",
            "q38":"double",
            "q42":"else",
            "q45":"enum",
            "q50":"extern",
            "q55":"float",
            "q57":"for",
            "q61":"goto",
            "q63":"if",
            "q65":"int",
            "q69":"long",
            "q77":"register",
            "q81":"return",
            "q86":"shor",
            "q91":"signed",
            "q95":"sizeof",
            "q100":"static",
            "q104":"struct",
            "q109":"switch",
            "q116":"typedef",
            "q121":"union",
            "q142":"unsigned",
            "q125":"void",
            "q131":"volatile",
            "q136":"while",
        }

        self.apariciones = {
            "auto":0,
            "break":0,
            "case":0,
            "char":0,
            "const":0,
            "continue":0,
            "default":0,
            "double":0,
            "else":0,
            "enum":0,
            "extern":0,
            "float":0,
            "for":0,
            "goto":0,
            "if":0,
            "int":0,
            "long":0,
            "register":0,
            "return":0,
            "shor":0,
            "signed":0,
            "sizeof":0,
            "static":0,
            "struct":0,
            "switch":0,
            "typedef":0,
            "union":0,
            "unsigned":0,
            "void":0,
            "volatile":0,
            "while":0,
        }


        self.q_0 = q_0
        self.F = F
        self.estado_actual = q_0
        self.guardarPasos = guardarPasos
        self.dictCompletado = False
        if self.guardarPasos:
            self.archivo = open("pasos.txt", "w")
        self.palabrasReservadas = open("palabras.txt", "w")

    def get_estado_actual(self):
        return self.estado_actual

    def get_estado_inicial(self):
        return self.q_0

    def completar_diccionario(self):
        for i in self.delta.keys():
            if "RDA" in self.delta[i].keys():
                for j in self.sigma:
                    if not j in self.delta[i].keys():
                        self.delta[i][j] = self.delta[i]["RDA"]
                self.delta[i].pop("RDA", None)
            else:
                for j in self.sigma:
                    if not j in self.delta[i].keys():
                        self.delta[i][j] = None
        #print(self.delta["q1"]["p"])
    # Prueba una cadena en el automata, retorna True si el automata acepta lacadena

    def prueba(self, cadena):
        if self.guardarPasos:
            self.archivo.write("Cadena: " + cadena + "\n")
        if not self.dictCompletado:
            self.completar_diccionario()
        self.palabrasReservadas.write("Analizando el codigo: \n")
        self.palabrasReservadas.write(cadena + "\n")
        indice = 0
        renglon = 1
        for i in cadena:
            if i == "\n":
                renglon+=1
                indice = 0
            indice +=1
            # Busca en el diccionario delta que estado es al que tiene que ir
            siguiente_estado = self.delta[self.estado_actual][i]

            if self.guardarPasos:
                self.archivo.write("Por " + i + " Se paso de: " +
                                   self.estado_actual + " a: " + siguiente_estado + '\n')

            if siguiente_estado in self.F and self.estado_actual != "q0" and self.estado_actual != "q1":
                self.apariciones[self.nombreEstados[self.estado_actual]] += 1
                self.palabrasReservadas.write("Palabra reservada: ")
                self.palabrasReservadas.write(self.nombreEstados[self.estado_actual])
                self.palabrasReservadas.write(" en el renglon "+ str(renglon))
                self.palabrasReservadas.write(" en el indice "+ str(indice-1-len(self.nombreEstados[self.estado_actual])) + "\n")


            self.estado_actual = siguiente_estado

            

            if self.estado_actual == None:
                self.estado_actual = self.get_estado_inicial()
                return False
        for i in self.apariciones.keys():
            if self.apariciones[i] != 0:
                self.palabrasReservadas.write("La palabra "+ i + " aparece " + str(self.apariciones[i]) + " veces\n")
        '''
            Si el estado actual despues de evaluar toda la cadena
            esta en la lista de estados finales retorna True
            de lo contrario retorna False
        '''
        if self.estado_actual in self.F:
            self.estado_actual = self.get_estado_inicial()
            return True
        else:
            self.estado_actual = self.get_estado_inicial()
            return False
        


    #Genera una imagen png con un diagrama que representa el automata
    def drawn(self):
        # inicializa el diagrama
        f = Digraph('finite_state_machine', filename='fsm.gv', format='png')
        f.attr(rankdir='LR', size='300,300')

        # Dibuja los nodos finales con doblecirculo
        f.attr('node', shape='doublecircle')

        for i in self.F:
            f.node(i)

        f.attr('node', shape='circle')

        # Agrega todos los nodos de todos los estados
        for key in self.delta.keys():
            f.node(key)
        #Agrega todas las conexiones
        #Cuando una misma conexion tiene varios inputs los une en una sola flecha
        for estado, conexiones in self.delta.items():
            contados = []
            for nombre, conex in conexiones.items():
                count = 0
                repetidos = []
                if conex in contados or conex == None:
                    continue
                for nombreTemp, conexTemp in conexiones.items():
                    if nombreTemp in repetidos:
                        continue
                    if conex == conexTemp:
                        count += 1
                        repetidos.append(nombreTemp)
                contados.append(conex)
                if len(repetidos) == 1:
                    f.edge(estado, conex, nombre)
                else:
                    cadena = ""
                    for i in repetidos:
                        cadena += (i+",")
                    cadena = cadena[:-1]
                    f.edge(estado, conex, cadena)

        #Se crea un nodo transparente para poner la flecha del estado inicial
        f.attr('node', style='filled')
        f.attr('node', color='white')
        f.edge('', "q1")
        f.view()
