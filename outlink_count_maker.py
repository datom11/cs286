#!/usr/bin/python
# -*-coding: utf-8 -*-

import json
import time

page_to_id_map = {}
page_to_idCount_map = {}

with open('N_O_L.json') as f:
    page_to_id_map = json.load(f)

print "\nN_O_L LOADED !!!\n"

N = len(page_to_id_map.keys())

#print page_to_id_map.keys()[10]

#count = 0

for k,v in page_to_id_map.items():
	if len(v) == 0:
		page_to_idCount_map[k] = N
	else:
		page_to_idCount_map[k] = len(v)

#print "value in page to count dictionary is\n"

'''
for k,v in page_to_idCount_map.items():
	print k
	print v
'''


#now you have the hashmap in page_to_idCount_map

#writing the dictionary to idCount file
with open('O_C.json','w') as f:  
	json.dump(page_to_idCount_map, f)




