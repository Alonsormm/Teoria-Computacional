#include<bits/stdc++.h>

using namespace std;

class DFA{
  int num_Q;
  vector<string> sigma;
  map<string,map<string,string>> delta;
  string q_0;
  vector <string> F;
  vector <string> Q_list;
  string estado_actual;

  public :
    DFA(int numq, vector<string>  sig, map<string,map<string,string>> delt, string q0, vector <string> f):
      num_Q(numq), sigma(sig), delta(delt), q_0(q0), F(f){
        string temp;
        for(int i = 0; i < num_Q; i++){
          temp = "q" + to_string(i+1);
          Q_list.push_back(temp);
        }
      }
  
    bool prueba(string cadena){
      string siguiente_estado;
      estado_actual = q_0;
      map<string,string> dictTemp;
      for(char i : cadena){
        dictTemp = delta.find(estado_actual)->second;
        siguiente_estado =  dictTemp.find(string(1,i)) ->second;
        estado_actual = siguiente_estado;
      }
      for(string i: F){
        if (estado_actual==i){
          return true;
        }
      }
      return false;
    }


};

/* 
  Ejemplo automata de paridad
  
  int num_Q = 4;
  vector <string> sigma = {"0", "1"};
  map<string,map<string,string>> delta;
  delta.insert({"q1", {{"0","q2"}, {"1","q4"}}});
  delta.insert({"q2", {{"0","q1"}, {"1","q3"}}});
  delta.insert({"q3", {{"0","q4"}, {"1","q2"}}});
  delta.insert({"q4", {{"0","q3"}, {"1","q1"}}});
  string q_0 = "q1";
  vector <string> F = {"q1"};

  DFA dfa(num_Q,sigma,delta,q_0,F);
  cout << dfa.prueba("00000011");
  
*/