#include<bits/stdc++.h>
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
  myfile.open ("datos2.txt");
  myfile << '{';
  int opc,n;
  string temp = "";
  cout << "Ingrese n: ";
  cin >> n;
  for(int i = 1; i < n+1; i++){
    imprimirCombi(temp,i,0, myfile);
    cout <<  i << '\n';
  }
  myfile<<'}';
  cout << "Archivo generado\n";
  myfile.close();
}