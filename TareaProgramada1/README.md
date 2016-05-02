Universidad de Costa Rica
Escuela de Ingeniería Eléctrica
Ricardo Quirós Redondo/ Berni Mora Esobar
-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

Instrucciones para ejecución del programa: tarea_programada.py

1. Para la correcta ejecución del programa se debe tener instalado el paquete: python-numpy
2. El programa lee un archivo llamado "aligned.trace" el cuál debe estar disponible en la misma carpeta que se encuentre el ejecutable del programa.
3. El programa recibe 3 parámetros por consola a la hora de ser ejecutado, el orden es: <tipo de asocitividad>, <tamaño del cache en kB>, <tamaño del bloque en B>.

Ejemplo: ./tarea_programada.py 2-way 1 16

4. El tipo de asociatividad ingresado debe ser uno de los siguientes 3:
	*Directo o directo
	*2-Way o 2-way
	*4-Way o 4-way

5. El tamaño de bloque debe ser un número que se potencia de 2, por ejemplo:1,2,4,8,16,32,64,128,256,512...

