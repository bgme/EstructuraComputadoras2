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
cache_size = int(sys.argv[2])
block_size = int(sys.argv[3])

memoria = np.empty((cache_size, block_size))

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
