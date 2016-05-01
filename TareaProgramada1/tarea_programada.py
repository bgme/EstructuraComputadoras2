#!/usr/bin/python

import math
import binascii
import sys
import numpy as np
import random
from math import log


miss = 0
hit = 0

asociatividad = sys.argv[1]
cache_size = int(sys.argv[2]) #Tamano del cache en KB
block_size = int(sys.argv[3]) #Tamano del bloque en B

##Orden en memoria
##memoria [index, tag1, tag2, tag3, tag4]

num_posiciones = cache_size * 1024 / block_size #numero de bloques de cache de N palabras de 1 byte c/u

#aqui se elige la cantidad de bits para cada parte de la direccion (index,tag,byte_offset)
num_index = int(math.log(num_posiciones,2)) 
num_byteoffset = int(math.log(block_size,2))
num_tag = 32 -(num_index+num_byteoffset)

print "Bits de index: %s , Bits de offset: %s , Bits de tag: %s" %(num_index, num_byteoffset, num_tag)



#se le agregan los casos para mayor facilidad de seleccion en el algoritmo posterior
if asociatividad == 'directo' or asociatividad == 'Directo':
	memoria = np.empty((num_posiciones, 2)) #Espacio para tag y el indice
	#caso = 1
	f=open('aligned.trace','r')
	for line in f:
		dir_bin = bin(int(line[0:8],16))
		index = dir_bin[len(dir_bin)-(num_byteoffset+num_index):len(dir_bin)-num_byteoffset]
		tag = dir_bin[2:-(num_byteoffset+num_index)]  
		if float(tag) == memoria[(int(index,2),1)]:
			hit = hit+1
		else:
			miss = miss+1
			memoria[(int(index,2),1)] = float(tag)
	f.close()
elif asociatividad == '2-way' or asociatividad == '2-Way':
	memoria = np.empty((num_posiciones, 3)) #Espacio para index y los dos tags
	#caso = 2
	f=open('aligned.trace','r')
	for line in f:
		dir_bin = bin(int(line[0:8],16))
		index = dir_bin[len(dir_bin)-(num_byteoffset+num_index):len(dir_bin)-num_byteoffset]
		tag = dir_bin[2:-(num_byteoffset+num_index)]  
		if (float(tag) == memoria[(int(index,2),1)] or float(tag) == memoria[(int(index,2),2)]) :
			hit = hit+1
		else:
			miss = miss+1
			memoria[(int(index,2),random.randint(1,2))] = float(tag)
	f.close()
elif asociatividad == '4-way' or asociatividad == '4-Way':
	memoria = np.empty((num_posiciones, 5)) #Espacio para index y los 4 tags
	#caso = 3
	f=open('aligned.trace','r')
	for line in f:
		dir_bin = bin(int(line[0:8],16))
		index = dir_bin[len(dir_bin)-(num_byteoffset+num_index):len(dir_bin)-num_byteoffset]
		tag = dir_bin[2:-(num_byteoffset+num_index)]  
		if (float(tag) == memoria[(int(index,2),1)] or float(tag) == memoria[(int(index,2),2)] or float(tag) == memoria[(int(index,2),3)] or float(tag) == memoria[(int(index,2),4)]) :
			hit = hit+1
		else:
			miss = miss+1
			memoria[(int(index,2),random.randint(1,4))] = float(tag)
	f.close()

print 'misses: %f, hits: %f' %(miss,hit)
