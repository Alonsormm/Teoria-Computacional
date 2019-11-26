#include<iostream>
#include <cstdlib>     /* srand, rand */
#include <ctime>
#include <fstream>

using namespace std;

string generarCadenaIfs(int numeroTab){
    string temp = "";
    for(int i = 0 ; i < numeroTab; i++){
        temp += "\t";
    }    
    return temp;
}

int main(){
    string s = "iCtSA";
    string a = ";eS";
    string cadenaFinal = s;
    std::ofstream outfile;
    outfile.open("ifs.txt", std::ios_base::out);
    double tam = 5;
    double i = tam - 1;
    double max = 100000;
    double count = 0;
    srand(time(0));
    int random;
    int parentesisSaltado = 0;
    while(count < max){
        if(cadenaFinal[i] == ')'){
            i--;
            continue;
        }
        if(cadenaFinal[i] == 'A'){
            random = rand() % 2;
            if (random) {
                cadenaFinal.replace(i, 1, "(;eS)");
                parentesisSaltado++;
                i+=4;
            }
            else{
                cadenaFinal.replace(i,1,"");
            }
        }
        if(cadenaFinal[i] == 'S'){
            cadenaFinal.replace(i,1,"(iCtSA)");
            parentesisSaltado++;
            i+=6;
        }
        i--;
        count++;
    }
    i+=parentesisSaltado;
    int tabulaciones = 0;
    string cadenaIfs = "";
    for(int j = 0; j < i; j++){
	    if (cadenaFinal[j] == 'i')
	    	cadenaIfs+= generarCadenaIfs(tabulaciones) + "if";
	    else if (cadenaFinal[j] == 'C')
	    	cadenaIfs+="(C)";
	    else if (cadenaFinal[j] == 't'){
	    	tabulaciones+=1;
	    	cadenaIfs+="{\n";
        }  
	    else if (cadenaFinal[j] == ';'){
	    	tabulaciones-=1;
	    	cadenaIfs+="\n" + generarCadenaIfs(tabulaciones) +  "}";
        }
	    else if (cadenaFinal[j] == 'e'){
	    	cadenaIfs += "\n" + generarCadenaIfs(tabulaciones) +  "else{\n";
	    	tabulaciones+=1;
        }
	    else if(cadenaFinal[j] == ')'){
	    	tabulaciones-=1;
	    	cadenaIfs += "\n" + generarCadenaIfs(tabulaciones) +  "}";
	    	if(tabulaciones == 0){
	    		break;
            }
        }
    }
    outfile << cadenaIfs <<  '\n';
}
