#include<bits/stdc++.h>
#include <thread>
using namespace std;

void imprimirCombi(string cadena, int n, int tam, ofstream &myfile){
  if(tam == n){
    myfile << cadena << ',';
    return;
  }
  string cadena_0 = cadena+"0";
  string cadena_1 = cadena+"1";
  imprimirCombi(cadena_0,n,tam+1,myfile);
  imprimirCombi(cadena_1,n,tam+1,myfile);
}

int main(){
  ofstream myfile;
  myfile.open ("datos1.txt");
  myfile << '{';
  int opc,n;
  string temp = "";
  cout << "Ingrese n: ";
  cin >> n;
  imprimirCombi(temp,n,0, myfile);
  myfile<<'}';
  cout << "Archivo generado\n";
  myfile.close();
}