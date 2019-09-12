#include <stdio.h>
#include <stdlib.h>
typedef struct racional{
     int a;
     int b;
} Racional;
Racional* crearRacional( int num, int den){
     Racional* temp;
     temp = malloc( sizeof(Racional*) );
     temp->a = num;
     temp->b = den; 
     return temp;
}
int main(){
    int num = 1;
    int den = 2;
    Racional* rac;
    rac = crearRacional(num,den);
    return 0;
}