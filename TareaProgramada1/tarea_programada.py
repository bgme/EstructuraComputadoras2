#!/usr/bin/python

import math
import binascii
import sys
import numpy as np


miss = 0
hit = 0
hola = 1
prueba = 0

asociatividad = sys.argv[1]
cache_size = int(sys.argv[2]) #Tamano del cache en KB
block_size = int(sys.argv[3]) #Tamano del bloque en B

num_posiciones = cache_size * 1024 / block_size

memoria = np.empty((num_posiciones, 2))

print (memoria)

f=open('pruebamemoria','r')

for line in f:
	info = line;
	index = info[6:8]
	tag = info[0:6]
        wr = info[-2:]
        
        
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
