#include<bits/stdc++.h>
using namespace std;

void imprimirCombi(string cadena, int tam, int k, ofstream &myfile){
  if(tam == k)
    return;
  string cadena_1 = cadena+"0";
  string cadena_0 = cadena+"1";
  myfile << cadena_1 << ',' << cadena_0 << ',';
  imprimirCombi(cadena_0,tam+1,k,myfile);
  imprimirCombi(cadena_1,tam+1,k,myfile);
}

int main(){
  ofstream myfile;
  myfile.open ("datos.txt");
  myfile << '{';
  int opc,k;
  string temp = "";
  cout << "1.-Ingresar Potencia\n2.-Potencia aleatoria\n Ingrese la opcion deseada: ";
  cin >> opc;
  if(opc == 1){
    cout << "Ingrese la potencia: ";
    cin >> k;
  }
  else{
    srand(time(0));
    k = (rand()%30) + 1;
    cout << k << '\n';
  }
  imprimirCombi(temp,0,k, myfile);
  myfile<<'}';
  myfile.close();
}