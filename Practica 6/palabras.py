from NFA import NDFA
import string

delta={
  "q1":{"w":"q2", "e":"q9", "rest": "q1"},
  "q2":{"e":"q3"},
  "q3":{"b":"q4"},
  "q4":{"s":"q5"},
  "q5":{"i":"q6"},
  "q6":{"t":"q7"},
  "q7":{"e":"q8"},
  "q8":{},
  "q9":{"b":"q10", "l":"q13", "m":"q22"},
  "q10":{"a":"q11"},
  "q11":{"y":"q12"},
  "q12":{},
  "q13":{"e":"q14"},
  "q14":{"c":"q15"},
  "q15":{"t":"q16"},
  "q16":{"r":"q17"},
  "q17":{"o":"q18"},
  "q18":{"n":"q19"},
  "q19":{"i":"q20"},
  "q20":{"c":"q21"},
  "q21":{},
  "q22":{"a":"q23"},
  "q23":{"i":"q24"},
  "q24":{"l":"q25"},
  "q25":{}
}

F_A = NDFA(Q = 25, sigma = list(string.ascii_lowercase), q_0 = "q1", F = ["q4","q8", "q12", "q21", "q25"], delt = delta) 

F_A.drawn()

print(F_A.prueba("asdasdasdasdwebsite"))