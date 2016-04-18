#!/usr/bin/python

import math
import binascii
import sys
import numpy as np
from math import log

miss = 0
hit = 0

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

print (memoria)

f=open('pruebamemoria','r')

for line in f:
	info = line;
	index = info[6:8]
	tag = info[0:6]
        wr = info[-2:]
        #valor = binascii.unhexlify(tag)
        
	#print valor
	print tag, index, wr
	#print wr
        #if tag in memoria[0]:
	#	hit = hit+1
	#else:
	#	miss = miss+1;
	#	memoria[0][1]=tag;
		
f.close()	


print 'misses: %f, hits: %f' %(miss,hit)
