#!/usr/bin/python

import math
import binascii
import sys
import numpy as np
import random
from math import log


miss = 0
hit = 0
caso = 0


asociatividad = sys.argv[1]
cache_size = int(sys.argv[2]) #Tamano del cache en KB
block_size = int(sys.argv[3]) #Tamano del bloque en B


num_posiciones = cache_size * 1024 / block_size #numero de bloques de cache de N palabras de 1 byte c/u

#aqui se elige la cantidad de bits para cada parte de la direccion (index,tag,byte_offset)
num_index = int(math.log(num_posiciones,2)) 
num_byteoffset = int(math.log(block_size,2))
num_tag = 32 -(num_index+num_byteoffset)

print num_index, num_byteoffset, num_tag

#se le agregan los casos para mayor facilidad de seleccion en el algoritmo posterior
if asociatividad == 'directo' or asociatividad == 'Directo':
	memoria = np.empty((num_posiciones, 2)) #Espacio para tag y el indice
	caso = 1
elif asociatividad == '2-way' or asociatividad == '2-Way':
	memoria = np.empty((num_posiciones, 3)) #Espacio para index y los dos tags
	caso = 2
elif asociatividad == '4-way' or asociatividad == '4-Way':
	memoria = np.empty((num_posiciones, 5)) #Espacio para index y los 4 tags
	caso = 3

##Orden en memoria
##memoria [index, tag1, tag2, tag3, tag4]

#print (memoria)

f=open('pruebamemoria','r')


for line in f:
	wr = line[-2:]
        dir_bin = bin(int(line[0:8],16))
	
	if num_byteoffset != 0:
		index = dir_bin[-(num_byteoffset+num_index):-num_byteoffset]
	else:
		index = dir_bin[-(num_index):]

	tag = dir_bin[2:-(num_byteoffset+num_index)]  
	#print dir_bin, index, tag
       
        
        
	#print wr
        #seccion que revisa cantidad de hits y misses y acomoda el dato en el bloque correspondiente
  
	
	if caso == 1:
		if float(tag) == memoria[(int(index,2),1)]:
			hit = hit+1
		else:
			miss = miss+1
			memoria[(int(index,2),1)] = float(tag)
####### SE LE AGREGA ESTA SECCION PARA ASOCIATIVIDAD 2 O 4. ##########
	elif caso == 2:
		if (float(tag) == memoria[(int(index,2),1)] or float(tag) == memoria[(int(index,2),2)]) :
			hit = hit+1
		else:
			miss = miss+1
			memoria[(int(index,2),random.randint(1,2))] = float(tag)
	elif caso == 3:
		if (float(tag) == memoria[(int(index,2),1)] or float(tag) == memoria[(int(index,2),2)] or float(tag) == memoria[(int(index,2),3)] or float(tag) == memoria[(int(index,2),4)]) :
			hit = hit+1
		else:
			miss = miss+1
			memoria[(int(index,2),random.randint(1,4))] = float(tag)
			#print random.randint(1,4)
		
#################################################################################		
f.close()


#np.set_printoptions(precision=8,edgeitems=5)
#print memoria


print 'misses: %f, hits: %f' %(miss,hit)
