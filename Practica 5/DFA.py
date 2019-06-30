from graphviz import Digraph

class FiniteAutomata(object):
    
    "Clase que representa al automata finito"
    
    def __init__(self, num_Q, sigma, delt, q_0, F):
        
        """
            Q: Conjunto finito llamado "de estados" #Numero de estados (Int)
            sigma : Conjunto finito llamado Alfabeto (Set)
            delta : Funcion de transicion tal que Q x sigma => Q #Diccionario de listas
            q_0 : Estado inicial #
            F:  Estados de aceptacion (Set)
        """
        Q_list = []
        delta = {}
        for i in range(num_Q):
            Q_list.append("q"+str(i+1))
            delta["q"+str(i+1)] = None
        
        self.Q = (Q_list)
        self.sigma = (sigma)
        self.delta = delt
        self.q_0 = q_0
        self.F = F
        self.estado_actual = q_0
        self.archivo = open("camino.txt", "w")
        
    def get_estado_actual (self):
        return self.estado_actual
    
    def get_estado_inicial(self):
        return self.q_0
    

    def prueba(self, cadena):
        for i in (cadena):
            self.archivo.write(i + '\n')            
            siguiente_estado = self.delta[self.estado_actual[0]][int(i)]
            self.archivo.write("Paso de " + self.estado_actual[0] + " a " + siguiente_estado + '\n') 
            self.estado_actual = [siguiente_estado]
            
            if self.estado_actual[0] == None:
                self.estado_actual = self.get_estado_inicial()
                return False
            else:
                None
            
        if self.estado_actual[0] in self.F :
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
        
        for i in self.q_0:
            f.node(i)


            
        f.attr('node', shape='circle')
        
        for key, value in self.delta.items():
            #print("Evaluando cada par key-value")
            #print(key)
            #print(value)
            k = list(self.sigma)
            
            for j in self.delta.keys():
                n=0
                memory = []                
                for i in value:
                    if i == j:
                        memory.append(k[n])
                        #print("Memoria " + str(memory))
                    n+=1
                    a = str(memory)[1:-1]
                
                if len(a) != 0 and i != None:
                    f.edge(key , j, label = a)
                
#                if i != None:
#                    f.edge(key, i , label=str(k[m]))
#                m +=1
        
        f.attr('node', style='filled')
        f.attr('node', color='white')
        f.edge('',"q1")
        
        f.view()
        
        return None
        
    
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

    