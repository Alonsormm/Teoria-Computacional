from NFA import NFA

q = 2
sigma = ["0", "1"]
delta = {
    "q0" :{"0": ["q0", "q1"], "1" : "q0"},
    "q1" : {"0": None, "1": "q2"},
    "q2" : {"0": None, "1": None},
}
q_0 = "q0"
F = ["q2"]

automata = NFA(q, sigma, delta, q_0, F)
<<<<<<< HEAD
#automata.drawn()
print(automata.prueba("111111111111111111110101"))
=======
automata.drawn()
print(automata.prueba("111111111111111111110101"))
>>>>>>> 63fac01ddf022262e1ef53efb4ffe0150340bb3c
