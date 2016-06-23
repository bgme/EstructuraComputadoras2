#Universidad de Costa Rica  
##Escuela de Ingeniería Eléctrica  
##Ricardo Quirós Redondo/ Berni Mora Escobar  
-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

##Instrucciones compilación y ejecución:

1. Para la correcta ejecución de los programa se deben tener instalados los paquetes: libopenmpi-dev lam-runtime mpich openmpi-bin
2. Para compilar los archivos parte2.c y paralelo.c existe un makefile el cual se debe usar con el comando: make, se crearan los archivos llamados "parte" y "paralelo"
3. Para ejecución se tienen 2 casos:

	*Archivo parte2: se ejecuta con el comando ./parte2
	*Archivo paralelo: se ejecuta con el comando mpicc -np X paralelo, donde X es el número de procesos que se desean crear


