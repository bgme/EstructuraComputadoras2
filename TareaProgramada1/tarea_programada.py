#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import binascii
import sys
import numpy as np
import random
from math import log

#se inicializan los contadores de misses y hits
miss = 0
hit = 0

#manejo de excepción en caso de tener error en los parametros
try:
	asociatividad = sys.argv[1]
	cache_size = int(sys.argv[2]) #Tamano del cache en KB
	block_size = int(sys.argv[3]) #Tamano del bloque en B
except:
	print '\033[1;41mError:\033[1;m'+' Parámetros incorrectos, deben indicarse: tipo de asociatividad, tamaño de cache en kB y tamaño del bloque en B.'
	sys.exit(1)

##Orden en memoria
##memoria [index, tag1, tag2, tag3, tag4]

num_posiciones = cache_size * 1024 / block_size #numero de bloques de cache de N palabras de 1 byte c/u

#aqui se elige la cantidad de bits para cada parte de la direccion (index,tag,byte_offset)
num_index = int(math.log(num_posiciones,2)) 
offset=math.log(block_size,2)
num_byteoffset = int(math.log(block_size,2))
num_tag = 32 -(num_index+num_byteoffset)

#error si el tamaño de bloque no es correcto
if offset.is_integer() == False:
	print '\033[1;41mError:\033[1;m'+' El tamaño de bloque debe ser una potencia de 2.Ej:1,2,4,8,16,32,64...'
	sys.exit(1)


if asociatividad == 'directo' or asociatividad == 'Directo': #resolución del problema para directo
	print "Bits de index: %s , Bits de offset: %s , Bits de tag: %s" %(num_index, num_byteoffset, num_tag)
	memoria = np.empty((num_posiciones, 2)) #Espacio para tag y el indice
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
elif asociatividad == '2-way' or asociatividad == '2-Way': #resolución del problema para 2-way
	print "Bits de index: %s , Bits de offset: %s , Bits de tag: %s" %(num_index, num_byteoffset, num_tag)
	memoria = np.empty((num_posiciones, 3)) #Espacio para indice y los dos tags
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
elif asociatividad == '4-way' or asociatividad == '4-Way': #resolución del problema para 4-way
	print "Bits de index: %s , Bits de offset: %s , Bits de tag: %s" %(num_index, num_byteoffset, num_tag)
	memoria = np.empty((num_posiciones, 5)) #Espacio para el indice y los 4 tags
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
else: #Mensaje de error en caso de no introducir adecuadamente la asocitividad
	print '\033[1;41mError:\033[1;m'+' El valor de asociatividad no es correcto, intente con: directo, 2-way o 4-way.'
	sys.exit(1)

print 'misses: %f, hits: %f' %(miss,hit) #impresión de la cantidad de misses y hits de la ejecución
