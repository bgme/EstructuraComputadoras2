#!/usr/bin/python

import math
import binascii
import sys
import numpy as np
from math import log


miss = 0
hit = 0
hola = 1
prueba = 0

asociatividad = sys.argv[1]
cache_size = int(sys.argv[2]) #Tamano del cache en KB
block_size = int(sys.argv[3]) #Tamano del bloque en B

num_posiciones = cache_size * 1024 / block_size #numero de bloques de cache de N palabras de 1 byte c/u

byteoffset = int(math.log(block_size,2))

if asociatividad == 'directo' or asociatividad == 'Directo':
	memoria = np.empty((num_posiciones, 2)) #Espacio para tag y el indice
elif asociatividad == '2-way' or asociatividad == '2-Way':
	memoria = np.empty((num_posiciones, 3)) #Espacio para index y los dos tags
elif asociatividad == '4-way' or asociatividad == '4-Way':
	memoria = np.empty((num_posiciones, 5)) #Espacio para index y los 4 tags

##Orden en memoria
##memoria [index, tag1, tag2, tag3, tag4]

#print (memoria)

f=open('pruebamemoria','r')


for line in f:
	wr = line[-2:]
        dir_bin = bin(int(line[0:8],16))
	index = dir_bin[-3:]  #esto se tiene que cambiar por variables que dependen de los tamanos introducidos en la consola
	tag = dir_bin[2:-3]  #igual aqui
	#print dir_bin, index, tag
        #print int(index,2)
        
        
	#print wr
        #seccion que revisa cantidad de hits y misses y acomoda el dato en el bloque correspondiente
  
	#print float(tag),memoria[(int(index,2),1)]
	
	if float(tag) == memoria[(int(index,2),1)]:
		hit = hit+1
	else:
		miss = miss+1
		memoria[(int(index,2),1)] = float(tag)
		
f.close()


np.set_printoptions(precision=8)
print memoria


print 'misses: %f, hits: %f' %(miss,hit)
