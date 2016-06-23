#include <stdio.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>
#include <string.h>
#include <mpi.h>

int main(int argc, char *argv[]){

	clock_t start = clock();

	int size = 48615;
	int primes [size];
	int global_primes [size];
	int final = floor(sqrt(size)); 
	int stop, i, j;
	int newline=0;
	int l=0;
	double time;


	

	int my_id, ierr, num_procs;
      	
	ierr = MPI_Init(&argc, &argv);
	MPI_Status status;
	ierr = MPI_Comm_rank(MPI_COMM_WORLD, &my_id); //Para saber el número de proceso
     	ierr = MPI_Comm_size(MPI_COMM_WORLD, &num_procs); //Para saber la cantidad de procesos
	
memset(primes,0,size); //Inicializando el vector en true
	for(i=2+my_id;i<=final;i+=num_procs){
		if(primes[i]==0){
			stop= floor(size/i); 
			for(j=i;j<=stop;j++){	
				primes[i*j]=1;
			}		
		}	
		
	}

	ierr = MPI_Barrier(MPI_COMM_WORLD);
	ierr = MPI_Reduce(&primes, global_primes, size, MPI_INT, MPI_LOR, 0, MPI_COMM_WORLD);

	MPI_Finalize();
	time = ((double)clock()-start)/ CLOCKS_PER_SEC*1000;

	if(my_id == 0){
		printf("Los números primos son:\n");
		for(i=2;i<=size;i++){		
			if(global_primes[i]==0){
				printf("%d, ",i);
				newline++;
				l++;
			}
			if(newline==10 | i==size){
				printf("\n");
				newline=0;
			}				
		}
		
		
		
		printf("Se encontraron %d números primos, y el tiempo transcurrido fue de %f milisegundos. Se crearon %i procesos \n",l,time,num_procs);
		
	}
		

   	return 0;
}
