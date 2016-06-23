#!/usr/bin/python

import math
import binascii
import numpy as np



cant_index_L1 = 9
cant_byteoffset_L1 = 2
cant_tag_L1 = 21


cant_index_L2 = 12
cant_byteoffset_L2 = 2
cant_tag_L2 = 18

CPU_active = 1
CPU_inactive = 2

a = 1

#primero hay que crear los 3 caches (2 L1 y L2)

#3 columnas: index, tag, estado

cacheL11 = np.empty((512, 3))
cacheL12 = np.empty((512, 3))
cacheL2 = np.empty((4096, 3))

#Estados: M = 00, E = 01, S = 10, I = 11

f=open('aligned.trace','r')

for line in f:
	dir_bin = bin(int(line[0:8],16))
	#print dir_bin + '\t'	
	accion = line[-2:-1]
	#print accion + 'prueba'
	index_L1 = dir_bin[cant_tag_L1+2:-cant_byteoffset_L1]
	tag_L1 = dir_bin[2:cant_tag_L1+2]
	#print tag_L1 + '\t' + index_L1 + '\n'

	index_L2 = dir_bin[cant_tag_L2+2:-cant_byteoffset_L2]
	tag_L2 = dir_bin[2:cant_tag_L2+2]

	#aqui comienza la logica de estados:

	#primero se elige cual CPU ejecuta la instruccion
	if CPU_active == 1:
		mem_L1 = cacheL11
		N_mem_L1 = cacheL12
	elif CPU_active == 2:
		mem_L1 = cacheL12
		N_mem_L1 = cacheL11
		
	if accion == 'L':
			#si hay hit:
			if float(tag_L1) == mem_L1[(int(index_L1,2),1)]:
				if mem_L1[(int(index_L1,2),2)] == 11:
					mem_L1[(int(index_L1,2),2)] == 10;
					N_mem_L1[(int(index_L1,2),2)] == 10;
					cacheL2[(int(index_L2,2),2)] == 10;
					#el otro cache detecta que se quiere leer y por lo tanto envia el valor correcto al otro L1 y al L2, y se pasa a el estado S 
				#de lo contrario no se cambia el estado
			else:
				
				#si no hay copias:
				if float(tag_L1) != N_mem_L1[(int(index_L1,2),1)]:
					if float(tag_L2) == cacheL2[(int(index_L2,2),1)]: #si hay copia en L2 se toma de ahi y se coloca el estado E
						mem_L1[(int(index_L1,2),1)] = float(tag_L1);
						mem_L1[(int(index_L1,2),2)] = 01;
					else: #de lo contrario primero se copia en el L2 de la 'memoria principal' y luego en L1
						
						cacheL2[(int(index_L2,2),1)] = float(tag_L2);
						mem_L1[(int(index_L1,2),1)] = float(tag_L1);
						mem_L1[(int(index_L1,2),2)] = 01;
						cacheL2[(int(index_L2,2),2)] == 01;
						
						
				#si hay copias:
				elif float(tag_L1) == N_mem_L1[(int(index_L1,2),1)]:
					#si es exclusive
					if N_mem_L1[(int(index_L1,2),2)] == 01:
						#se guarda el dato y se cambian los estados de las 2 copias a S = 10
						mem_L1[(int(index_L1,2),1)] = float(tag_L1);
						mem_L1[(int(index_L1,2),2)] = 10;
						N_mem_L1[(int(index_L1,2),2)] = 10;
						cacheL2[(int(index_L2,2),2)] == 10;
						
					#si es modified:	
					elif N_mem_L1[(int(index_L1,2),2)] == 00:
						mem_L1[(int(index_L1,2),1)] = float(tag_L1)
						mem_L1[(int(index_L1,2),2)] = 10
						N_mem_L1[(int(index_L1,2),2)] = 10
						cacheL2[(int(index_L2,2),2)] == 10;
						#se cambia el estado a shared (se escribe primero el dato en L2 y luego en el otro cache)
									
		
	elif accion == 'S':
			#hit
			if float(tag_L1) == mem_L1[(int(index_L1,2),1)]:
				#if mem_L1[(int(index_L1,2),2)] == 00:
					#se mantiene estado
				if mem_L1[(int(index_L1,2),2)] == 01: #si es exclusivo pasa a ser modified (y la copia en L2  se invalida)
					mem_L1[(int(index_L1,2),2)] = 00
					cacheL2[(int(index_L2,2),2)] == 11;
					
					
				elif mem_L1[(int(index_L1,2),2)] == 10: #si es shared pasa a ser modified y la otra copia pasa a ser Invalid
					mem_L1[(int(index_L1,2),2)] = 00
					N_mem_L1[(int(index_L1,2),2)] = 11
					cacheL2[(int(index_L2,2),2)] == 11
			#miss
			else:
				if float(tag_L1) != N_mem_L1[(int(index_L1,2),1)]: #si no hay mas copias
					if float(tag_L2) == cacheL2[(int(index_L2,2),1)]: #si tiene la info deseada en el nivel L2 se toma de ahi
						mem_L1[(int(index_L1,2),1)] = float(tag_L1)
						mem_L1[(int(index_L1,2),2)] = 00
					else: #de lo contrario primero se pone en el L2 de memoria principal
						cacheL2[(int(index_L2,2),1)] = float(tag_L2)
						mem_L1[(int(index_L1,2),1)] = float(tag_L1)
						mem_L1[(int(index_L1,2),2)] = 00
						cacheL2[(int(index_L2,2),2)] == 11
				#si hay copias:
				elif float(tag_L1) == N_mem_L1[(int(index_L1,2),1)]:
					if N_mem_L1[(int(index_L1,2),2)] == 00:
						mem_L1[(int(index_L1,2),2)] = 00
						N_mem_L1[(int(index_L1,2),2)] = 11
						cacheL2[(int(index_L2,2),2)] == 11
		
					elif N_mem_L1[(int(index_L1,2),2)] == 01 or N_mem_L1[(int(index_L1,2),2)] == 10:
						mem_L1[(int(index_L1,2),2)] = 00
						N_mem_L1[(int(index_L1,2),2)] = 11
						cacheL2[(int(index_L2,2),2)] == 11
						
	if a >= 49642108:		
		print 'Estado cache activo: ' 
		print mem_L1[(int(index_L1,2),2)] 
		print 'Estado cache inactivo: '
		print N_mem_L1[(int(index_L1,2),2)]
		print ' '
		
	
	#cambia el procesador en ejecucion por cada ciclo de for
	T = CPU_active
	CPU_active = CPU_inactive 
	CPU_inactive = T

	a = a+1
	

f.close()
		






