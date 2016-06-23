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
	int stop, i, j,k;
	int newline=0;
	int l=0;
	double time;
	int fin, inicio, an_id, inicio_id, final_id;
	int root_process = 0;
	int inicio_enviar, final_enviar, inicio_recibido, final_recibido;

	int my_id, ierr, num_procs;
      	MPI_Status status;

	ierr = MPI_Init(&argc, &argv);
	ierr = MPI_Comm_rank(MPI_COMM_WORLD, &my_id); //Para saber el número de proceso
     	ierr = MPI_Comm_size(MPI_COMM_WORLD, &num_procs); //Para saber la cantidad de procesos
	
	
	if(my_id == root_process){	
		memset(primes,0,size); //Inicializando el vector en false
		inicio = 2;			//Inicio de iteraciones para el proceso maestro
		fin= floor(final/num_procs); 	//Final de iteraciones para el proceso maestro
	
		
		printf("Soy el proceso principal e inicio en %i y finalizo en %i \n",inicio,fin);

		for(an_id = 1; an_id < num_procs; an_id++) {
		   	inicio_enviar = an_id*fin + 1;	//Inicio de iteraciones para cada proceso

			if(an_id==(num_procs-1)){	//Final de iteraciones para cada proceso
				final_enviar = final;
			}else{
			    final_enviar  = (an_id + 1)*fin;
			}

			 ierr = MPI_Send( &inicio_enviar, 1 , MPI_INT, an_id, 0, MPI_COMM_WORLD); //Envio inicio al proceso

			 ierr = MPI_Send( &final_enviar, 1, MPI_INT, an_id, 1, MPI_COMM_WORLD);	//Envio final al proceso
		 }

		for(i=inicio;i<=fin;i++){		//Calculo de los primos que le toca al proceso maestro
			if(primes[i]==0){
				stop= floor(size/i); 
				for(j=i;j<=stop;j++){	
					primes[i*j]=1;
				}		
			}	
		
		}
		
		for(an_id = 1; an_id < num_procs; an_id++) { //Recibo los vectores resultado de cada proceso
		    
		   	ierr = MPI_Recv( &global_primes, size, MPI_INT, MPI_ANY_SOURCE, 3, MPI_COMM_WORLD, &status);

	  		printf("Recibi de %i \n",status.MPI_SOURCE);

		  	 // sender = status.MPI_SOURCE; 
       			for(k=2;k<=size;k++){	//Unifico el resultado
		  		primes[k] = primes[k] + global_primes[k];
			}
		 }
		//printf("Los primeros números primos son:\n");
		for(i=2;i<=size;i++){		
			if(primes[i]==0){
				//printf("%d, ",i);
				//newline++;
				l++;
			}
			//if(newline==10 | i==size){
			//	printf("\n");
			//	newline=0;
			//}				
		}
		
		//MPI_Barrier( MPI_COMM_WORLD );
		time = ((double)clock()-start)/ CLOCKS_PER_SEC*1000;
		printf("Se encontraron %d números primos, y el tiempo transcurrido fue de %f milisegundos. Se crearon %i procesos \n",l,time,num_procs);
		
		
	}else{
		for(an_id = 1; an_id < num_procs; an_id++) {

			ierr = MPI_Recv( &inicio_recibido, 1, MPI_INT, root_process, 0, MPI_COMM_WORLD, &status);//Recibo inicio
			  
			ierr = MPI_Recv( &final_recibido, 1, MPI_INT, root_process, 1, MPI_COMM_WORLD, &status);//Recibo final

			inicio_id = inicio_recibido;
			final_id = final_recibido;

			for(i=inicio_id;i<=final_id;i++){ //Ejecuto la parte de la criba que le toca a cada proceso
				if(primes[i]==0){
					stop= floor(size/i); 
					for(j=i;j<=stop;j++){	
						primes[i*j]=1;
					}		
				}	
		
			}

			ierr = MPI_Send( &primes, size, MPI_INT, 0, 3, MPI_COMM_WORLD);
			printf("Soy el proceso %i e inicio en %i y finalizo en %i \n",my_id,inicio_id,final_id);
		}


	}
	MPI_Finalize();
   return 0;
}
