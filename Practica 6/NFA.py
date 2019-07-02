from graphviz import Digraph

class NDFA(object):
  def __init__(self, Q, sigma, delt, q_0, F):
    """
        Q: Conjunto finito llamado "de estados" #Numero de estados (Int)
        sigma : Conjunto finito llamado Alfabeto #Lista
        delta : Funcion de transicion tal que Q x sigma => P(Q x Sigma) #Diccionario de listas
        q_0 : Estado inicial #String
        F:  Estados de aceptacion #Lista de strings
    """
    '''
        delta={
              "q1":{"0":None, "1": ["q2","q3"]},
              "q2":{"0":"q5", "1": None},
              "q3":{"0":"q4", "1": None},
              "q4":{"0":"q3", "1": None},
              "q5":{"0":["q5",q6"], "1" : None},
              "q6":{"0":"q2", "1": None}
              }
        automata_finito_no_det = NDFA(Q = 6,
                   sigma=[0],
                   delt = delta,
                   q_0 = ["q1"],
                   F = ["q2","q3"])
    '''
    Q_list = []
    for i in range(Q):
        Q_list.append("q"+str(i+1))
    self.Q = Q_list
    self.sigma = sigma
    self.delta = delt
    self.completar_diccionario()
    self.q_0 = q_0
    self.F = F
    self.estado_actual = [q_0]
  def get_estado_actual(self):
      return self.estado_actual

  def set_estado_actual(self, estado_actual):
    self.estado_actual = estado_actual

  def get_F(self):
    return self.F

  def completar_diccionario(self):
    sigmaTemp = self.sigma
    sigmaTemp.append(chr(1013))
    for i in self.delta.keys():
      if "rest" in self.delta[i].keys():
        for j in self.sigma:
          if j == chr(1013) and not (j in self.delta[i].keys()):
            self.delta[i][j] = None
            continue
          if not (j in self.delta[i].keys()):
            self.delta[i][j] = self.delta[i]["rest"]
        self.delta[i].pop("rest")
      else:
        for j in sigmaTemp:
          if not j in self.delta[i].keys():
            self.delta[i][j] = None

  def prueba(self, cadena):
    for i in cadena:
      print("Bit leido de la cadena: " + i)
      estado_actual = self.get_estado_actual()
      print("Estado actual: " + str(estado_actual))
      estado_siguiente = []
      for estados in estado_actual:
        if estados == None:
          continue
        conexionesTemp = self.delta[estados][i]
        if conexionesTemp != None:
          if isinstance(conexionesTemp, list):
            for sig_estados in conexionesTemp:
              estado_siguiente.append(sig_estados)
          else:
            estado_siguiente.append(conexionesTemp)
        if conexionesTemp == None:
          estado_siguiente.append(None)
        episilon = conexionesTemp = self.delta[estados][chr(1013)]
        if episilon == None:
          continue
        if isinstance(episilon ,list):
          for estados in episilon:
              estado_siguiente.append(estados)
        else:
          estado_siguiente.append(episilon)
        
      print("Los siguientes estados " + str(estado_siguiente))
      self.set_estado_actual(estado_siguiente)
    for i in self.get_estado_actual():
      if i in self.get_F():
        return True
    return False
  def drawn(self):
    # inicializa el diagrama
    f = Digraph('finite_state_machine', filename='fsm.gv', format='png')
    f.attr(rankdir='LR', size='8,5')
    # Dibuja los nodos finales con doblecirculo
    f.attr('node', shape='doublecircle')
    for i in self.F:
        f.node(i)
    f.attr('node', shape='circle')
    f.attr('edge', )
    # Agrega todos los nodos de todos los estados
    for key in self.delta.keys():
        f.node(key)
    #Agrega todas las conexiones
    #Cuando una misma conexion tiene varios inputs los une en una sola flecha
    for estado, conexiones in self.delta.items():
      for nombre, conex in conexiones.items():
        if conex == None:
          continue
        if isinstance(conex,list):
          for i in conex:
            f.edge(estado,i,nombre)
        else:
          f.edge(estado,conex,nombre)

            
    #Se crea un nodo transparente para poner la flecha del estado inicial
    f.attr('node', style='filled')
    f.attr('node', color='white')
    f.edge('', "q1")
    f.view()