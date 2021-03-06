import DFA
import string

q = 142
sigma = list(string.printable)
q_0 = "q1"
F = ["q1"]
delta={
        "q0":{" " : "q1","\n":"q1", "RDA":"q0"},
        "q1":{"a":"q2", "b":"q6", "c": "q11","d":"q27", "e": "q39","f": "q51", "g": "q58","i":"q62","l":"q66","r": "q70","s":"q82","t":"q110","u":"q117","v":"q122","w":"q132"," " : "q1","\n":"q1","RDA":"q0"},
        
        #auto        
        "q2":{"u":"q3", "RDA":"q0"},
        "q3":{"t":"q4", "RDA":"q0"},
        "q4":{"o":"q5", "RDA":"q0"},
        "q5":{"RDA":"q0", " " : "q1"},
        #inicio con B
        #break
        "q6":{"r":"q7", "RDA":"q0"},
        "q7":{"e":"q8", "RDA":"q0"},
        "q8":{"a":"q9", "RDA":"q0"},
        "q9":{"k":"q10", "RDA":"q0"},
        "q10":{"RDA":"q0", " " : "q1", ";":"q1"},

        #incio con C
        "q11":{"a":"q12", "h" : "q15", "o": "q18","RDA":"q0"},
        #case
        "q12":{"s":"q13", "RDA":"q0"},
        "q13":{"e":"q14", "RDA":"q0"},
        "q14":{"RDA":"q0", " " : "q1"},
        
        #char
        "q15":{"a":"q16", "RDA":"q0"},
        "q16":{"r":"q17", "RDA":"q0"},
        "q17":{"RDA":"q0", " " : "q1", "*":"q1"},
        
        #inicio con "con"

        "q18":{"n":"q19", "RDA":"q0"},
        "q19":{"s":"q20","t": "q22","RDA":"q0"},
        #const
        "q20":{"t":"q21", "RDA":"q0"},
        "q21":{"RDA":"q0", " " : "q1"},

        #continue
        "q22":{"i":"q23", "RDA":"q0"},
        "q23":{"n":"q24", "RDA":"q0"},
        "q24":{"u":"q25", "RDA":"q0"},
        "q25":{"e":"q26", "RDA":"q0"},
        "q26":{"RDA":"q0", " " : "q1", ";" : "q1"},
        #inicio con d

        "q27":{"e":"q28", "o":"q34", "RDA":"q0"},

        #default
        "q28":{"f":"q29", "RDA":"q0"},
        "q29":{"a":"q30", "RDA":"q0"},
        "q30":{"u":"q31", "RDA":"q0"},
        "q31":{"l":"q32", "RDA":"q0"},
        "q32":{"t":"q33", "RDA":"q0"},
        "q33":{"RDA":"q0", " " : "q1", ":":"q1"},

        #inicio con do
        "q34":{"u":"q35", " " : "q1", "{" : "q1","RDA":"q1"},
        "q35":{"b":"q36", "RDA":"q0"},
        "q36":{"l":"q37", "RDA":"q0"},
        "q37":{"e":"q38", "RDA":"q0"},
        "q38":{"RDA":"q0", " " : "q1"},

        #inicio con e
        "q39":{"l":"q40", "n":"q43","x":"q46","RDA":"q0"},

        #else
        "q40":{"s":"q41","RDA":"q0"},
        "q41":{"e":"q42","RDA":"q0"},
        "q42":{"RDA":"q0", " " : "q1", "{":"q1"},

        #enum
        "q43":{"u":"q44","RDA":"q0"},
        "q44":{"m":"q45","RDA":"q0"},
        "q45":{"RDA":"q0", " " : "q1"},

        #extern
        "q46":{"t":"q47","RDA":"q0"},
        "q47":{"e":"q48","RDA":"q0"},
        "q48":{"r":"q49","RDA":"q0"},
        "q49":{"n":"q50","RDA":"q0"},
        "q50":{"RDA":"q0", " " : "q1"},

        #inicio con f
        "q51":{"l":"q52", "o":"q56","RDA":"q0"},

        #float
        "q52":{"o":"q53","RDA":"q0"},
        "q53":{"a":"q54","RDA":"q0"},
        "q54":{"t":"q55","RDA":"q0"},
        "q55":{"RDA":"q0", " " : "q1"},

        #for
        "q56":{"r":"q57","RDA":"q0"},
        "q57":{"RDA":"q0", " " : "q1", "{" : "q1"},
        
        #inicio con g
        #goto
        "q58":{"o":"q59","RDA":"q0"},
        "q59":{"t":"q60","RDA":"q0"},
        "q60":{"o":"q61","RDA":"q0"},
        "q61":{"RDA":"q0", " " : "q1"},

        #inicio con i
        "q62":{"f":"q63", "n": "q64","RDA":"q0"},
        #if
        "q63":{"RDA":"q0", " " : "q1", "{" : "q1"},
        #int
        "q64":{"t":"q65","RDA":"q0"},
        "q65":{"RDA":"q0", " " : "q1", "*":"q1"},
        
        #inicio con l
        #long
        "q66":{"o":"q67","RDA":"q0"},
        "q67":{"n":"q68","RDA":"q0"},
        "q68":{"g":"q69","RDA":"q0"},
        "q69":{"RDA":"q0", " " : "q1", "*":"q1"},

        #inicio con re
        "q70":{"e":"q71","RDA":"q0"},
        "q71":{"g":"q72","t": "q78","RDA":"q0"},
        
        #register
        "q72":{"i":"q73","RDA":"q0"},
        "q73":{"s":"q74","RDA":"q0"},
        "q74":{"t":"q75","RDA":"q0"},
        "q75":{"e":"q76","RDA":"q0"},
        "q76":{"r":"q77","RDA":"q0"},
        "q77":{"RDA":"q0", " " : "q1"},
        #return
        "q78":{"u":"q79","RDA":"q0"},
        "q79":{"r":"q80","RDA":"q0"},
        "q80":{"n":"q81","RDA":"q0"},
        "q81":{"RDA":"q0", " " : "q1", ";": "q1"},

        #inicio con s
        "q82":{"h":"q83","i": "q87","t":"q96","w": "q105","RDA":"q0"},
        #short
        "q83":{"o":"q84","RDA":"q0"},
        "q84":{"r":"q85","RDA":"q0"},
        "q85":{"t":"q86","RDA":"q0"},
        "q86":{"RDA":"q0", " " : "q1", "*":"q1"},
        #inicio con si
        "q87":{"g":"q88","z": "q92","RDA":"q0"},
        #signed
        "q88":{"n":"q89","RDA":"q0"},
        "q89":{"e":"q90","RDA":"q0"},        
        "q90":{"d":"q91","RDA":"q0"},        
        "q91":{"RDA":"q0", " " : "q1"},
        #sizeof
        "q92":{"e":"q93","RDA":"q0"},
        "q93":{"o":"q94","RDA":"q0"},
        "q94":{"f":"q95","RDA":"q0"},
        "q95":{"RDA":"q0", " " : "q1", "(" : "q1"},
        #inicio con st
        "q96":{"a":"q97","r": "q101","RDA":"q0"},
        #static
        "q97":{"t":"q98","RDA":"q0"},
        "q98":{"i":"q99","RDA":"q0"},
        "q99":{"c":"q100","RDA":"q0"},
        "q100":{"RDA":"q0", " " : "q1"},
        #struct
        "q101":{"u":"q102","RDA":"q0"},
        "q102":{"c":"q103","RDA":"q0"},
        "q103":{"t":"q104","RDA":"q0"},
        "q104":{"RDA":"q0", " " : "q1"},
        
        #switch
        "q105":{"i":"q106","RDA":"q0"},
        "q106":{"t":"q107","RDA":"q0"},
        "q107":{"c":"q108","RDA":"q0"},
        "q108":{"h":"q109","RDA":"q0"},
        "q109":{"RDA":"q0", " " : "q1" , "(" : "q1"},

        #inicio con t
        #typedef
        "q110":{"i":"q111","RDA":"q0"},
        "q111":{"p":"q112","RDA":"q0"},
        "q112":{"e":"q113","RDA":"q0"},
        "q113":{"d":"q114","RDA":"q0"},
        "q114":{"e":"q115","RDA":"q0"},
        "q115":{"f":"q116","RDA":"q0"},
        "q116":{"RDA":"q0", " " : "q1"},

        #inicio con u
        "q117":{"n":"q118","RDA":"q0"},
        #inicio con un
        "q118":{"i":"q119","s":"q137","RDA":"q0"},
        #union
        "q119":{"o":"q120","RDA":"q0"},
        "q120":{"n":"q121","RDA":"q0"},
        "q121":{"RDA":"q0", " " : "q1"},

        #unsigned

        #unsigned
        "q137":{"i":"q138","RDA":"q0"},        
        "q138":{"g":"q139","RDA":"q0"},
        "q139":{"n":"q140","RDA":"q0"},        
        "q140":{"e":"q141","RDA":"q0"},        
        "q141":{"d":"q142","RDA":"q0"},
        "q142":{"RDA":"q0", " " : "q1"},

        #incio con v
        "q122":{"o":"q123","RDA":"q0"},
        #incio con vo
        "q123":{"i":"q124","l":"q126","RDA":"q0"},
        #void
        "q124":{"d":"q125","RDA":"q0"},
        "q125":{"RDA":"q0", " " : "q1"},
        #volatile
        "q126":{"a":"q127","RDA":"q0"},
        "q127":{"t":"q128","RDA":"q0"},
        "q128":{"i":"q129","RDA":"q0"},
        "q129":{"l":"q130","RDA":"q0"},
        "q130":{"e":"q131","RDA":"q0"},
        "q131":{"RDA":"q0", " " : "q1"},
        #inicio con w
        "q132":{"h":"q133","RDA":"q0"},
        "q133":{"i":"q134","RDA":"q0"},
        "q134":{"l":"q135","RDA":"q0"},
        "q135":{"e":"q136","RDA":"q0"},
        "q136":{"RDA":"q0", " " : "q1", "(":"q1"},

      }


F_A = DFA.FiniteAutomata(q,sigma,delta,q_0,F, True)
F_A.drawn()
file = open("holamundo.c", "r")
cad = ""
for i in file.readlines():
  cad += i
F_A.prueba(cad)
print("Codigo analizado")

