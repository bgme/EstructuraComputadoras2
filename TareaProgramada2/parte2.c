#include <stdio.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>
#include <string.h>

int main(int argc, char *argv[]){

	clock_t start = clock();

	int size = 48615;
	bool primes [size];
	int stop = floor(sqrt(size)); 
	int stop1, i, j, k;
	int newline=0;
	int l=0;
	double time;

	memset(primes,false,size); //Inicializando el vector en false
	
	for(i=2;i<=stop;i++){
		if(!primes[i]){
			stop1= floor(size/i); 
			for(j=i;j<=stop1;j++){	
				primes[i*j]=true;
			}		
		}	
		
	}

	time = ((double)clock()-start)/ CLOCKS_PER_SEC*1000;

	printf("Los primeros números primos son:\n");
	for(i=2;i<=size;i++){		
		if(!primes[i]){
			printf("%d, ",i);
			newline++;
			l++;
		}
		if(newline==10 | i==size){
			printf("\n");
			newline=0;
		}				
	}

	printf("Se encontraron %d números primos, y el tiempo transcurrido fue de %f milisegundos \n",l,time);

	
   return 0;
}
