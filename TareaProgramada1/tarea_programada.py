#!/usr/bin/python

import math
import binascii

memoria = [['hola','lol','jeje'],[7,5,6]]
miss = 0
hit = 0
hola = 1

f=open('pruebamemoria','r')

for line in f:
	info = line;
	index = info[6:8]
	tag = info[0:6]
        wr = info[-2:]
        #valor = binascii.unhexlify(tag)
        
	#print valor
	print tag
	#print wr
        #if tag in memoria[0]:
	#	hit = hit+1
	#else:
	#	miss = miss+1;
	#	memoria[0][1]=tag;
		
f.close()	


print 'misses: %f, hits: %f' %(miss,hit)
