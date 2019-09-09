#include<bits/stdc++.h>

using namespace std;

void encontrarPrimos(int n){
  ofstream myfile;
  myfile.open("datos.txt");
  //myfile << '{';
  bool no_primo;
  for(int i = 3; i <= n ; i++){
    no_primo = false;
    for(int j = 3; j < i; j++){
      if(i % j == 0)
        no_primo = true;
    }
    if(!no_primo){
      myfile << i << "\n";
    }
  }
  //myfile << '}';
}

int main(){
  
  int opc,n;
  cout << "1.-Ingresar maximo\n2.-Maximo aleatorio\n Ingrese la opcion deseada: ";
  cin >> opc;
  if(opc == 1){
    cout << "Ingrese el maximo: ";
    cin >> n;
  }
  else{
    srand(time(0));
    n = (rand()%30) + 1;
    cout << "Maximo: " << n << '\n';
  }
  encontrarPrimos(n);
}