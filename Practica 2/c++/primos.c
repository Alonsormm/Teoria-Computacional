#include<stdio.h>










void main() {

FILE *fichero;
    fichero = fopen("primos.txt", "w+");
    if(fichero == NULL ) {
        printf("No fue posible abrir/crear el archivo\n");
        return;
   }

    int n=0,x=0;

    printf("Ingrese n: ");
    scanf("%d",&n);

    int prims[n],nums[n];

    for(int i=2;i<=n;i++) {
        if(nums[i] != 1 || i == 2) {
            prims[x] = i;
            fprintf(fichero,"%d\n",i);
            for(int p=2;(p*i)<=n;p++) {
                nums[(p*i)] = 1;
            }
            x++;
        }
    }
    printf("listo bro");
}