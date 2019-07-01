#Automata mejorado

from graphviz import Digraph

class FiniteAutomata(object):
    
    "Clase que representa al automata finito"
    
    def __init__(self, num_Q, sigma, delt, q_0, F,guardarPasos = False):
        
        """
            Q: Conjunto finito llamado "de estados" #Numero de estados (Int)
            sigma : Conjunto finito llamado Alfabeto (Set)
            delta : Funcion de transicion tal que Q x sigma => Q #Diccionario de listas
            q_0 : Estado inicial #
            F:  Estados de aceptacion (Set)
        """
        Q_list = []
        self.delta = {}
        for i in range(num_Q):
            Q_list.append("q"+str(i+1))


        self.Q = Q_list
        self.sigma = sigma
        self.delta = delt
        self.completar_diccionario()

        self.q_0 = q_0
        self.F = F
        self.estado_actual = q_0
        self.guardarPasos = guardarPasos
        if self.guardarPasos:
            self.archivo = open("pasos.txt", "w")
        
    def get_estado_actual (self):
        return self.estado_actual
    
    def get_estado_inicial(self):
        return self.q_0
    
    def completar_diccionario(self):
        for i in self.delta.keys():
            for j in self.sigma:
                if not j in self.delta[i].keys():
                    self.delta[i][j] = None

    

    def prueba(self, cadena):

        if self.guardarPasos:
            self.archivo.write("Cadena: " + cadena + "\n") 

        for i in (cadena):
            siguiente_estado = self.delta[self.estado_actual][i]

            if self.guardarPasos:
                self.archivo.write("Por " + i + " Se paso de: " + self.estado_actual + " a: " + siguiente_estado + '\n')

            self.estado_actual = siguiente_estado
            
            if self.estado_actual == None:
                self.estado_actual = self.get_estado_inicial()
                return False
            else:
                None
            
        if self.estado_actual in self.F :
            self.estado_actual = self.get_estado_inicial()
            return True
        else:
            self.estado_actual = self.get_estado_inicial()
            return False
        
        
    def drawn(self):
        

        f = Digraph('finite_state_machine', filename='fsm.gv', format='png')
        f.attr(rankdir='LR', size='8,5')
        
        f.attr('node', shape='doublecircle')
        
        for i in self.F:
            f.node(i)
            
        f.attr('node', shape='circle')
        
        f.node(self.q_0)

        for key in self.delta.keys():
            f.node(key)
        
        '''
        for estado, conexiones in self.delta.items():
            for nombre, conex in conexiones.items():
                if conex != None:
                    f.edge(estado,conex,nombre)'''
                
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
                        count+=1
                        repetidos.append(nombreTemp)
                contados.append(conex)
                if len(repetidos) == 1:
                    f.edge(estado,conex,nombre)                                        
                else:
                    cadena = ""
                    for i in repetidos:
                        cadena +=  (i+",")
                    cadena = cadena[:-1]
                    f.edge(estado,conex,cadena)
        
        f.attr('node', style='filled')
        f.attr('node', color='white')
        f.edge('',"q1")
        
        f.view()
        return None


        
        
        
    
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

    