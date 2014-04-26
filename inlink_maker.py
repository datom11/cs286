#!/usr/bin/python
# -*-coding: utf-8 -*-

import json
import time

page_to_id_map = {}
inbound_pages_map = {}

with open('N_O_L.json') as f:
    page_to_id_map = json.load(f)

print "\nN_O_L LOADED !!!\n"

#loading dictionary into memory
count = 0

'''
for k,v in page_to_id_map.items():
	
	if count == 0:
		print k
		print v[0]
		print v[1]
	count = count + 1            #printing only first value of value field
'''

i = 0
for k,v in page_to_id_map.items():	#will iterate over all the values
#	print "inside for"
#	if k == 15907:
#	print "when key=15907"
	while i < len(v):
		if v[i] in inbound_pages_map:
			if not k in inbound_pages_map[v[i]]:
				inbound_pages_map[v[i]].append (k)	
	        else:
			inbound_pages_map[v[i]]= []
			inbound_pages_map[v[i]].append (k)
		i = i + 1
	i = 0

print "outside loop"

#for k,v in inbound_pages_map.items():
#	print "hellooo"	
#	print k
#	print v  
	

with open('I_L.json','w') as f:  
	json.dump(inbound_pages_map, f)


