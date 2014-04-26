#!/usr/bin/python
# -*-coding: utf-8 -*-

import datetime

PAGES = []

print "Started at ", datetime.datetime.now(), "\n----------------------\n"
import re

id_to_url_dict = {}

c1 = 0

def process_stub(stub):
	#print("In pricess_stub" + stub)
	import re
	matchObj = re.match( r'.*<title>(.*)</title>.*<id>(.*)</id>.*<revision>.*<text.*>(.*?)</text>.*', stub, re.M)
	if matchObj:
		#print "matchObj.group(1) : ", matchObj.group(1)
		#print "matchObj.group(2) : ", matchObj.group(2)
		global c1
		c1 = c1 + 1

		page = matchObj.group(1)
		id = matchObj.group(2)
		#print "id = ", id
		
		#id_to_url_dict[page] = id	
		#id_to_url_dict[id] =  page	
		PAGES.append(page)

	else:
	   print "No match!!"


#data = tuple(open("/home/Kuldeep/cs255/final/sample-enwiki-4.xml", 'r')) 


#print(data[0])
#print(data[1])

c = 0
stub = ''
start_page_flag = False
end_page_flag = False


with open('wiki3k') as data:
	for l in data:
		#print l
		if start_page_flag: 
			if '</page>' not in l:
				l = l.replace("\n", "")
				stub += l
			else:
				start_page_flag = False
				process_stub(stub)
				#if c > 500:
				#	break

		elif not start_page_flag and '<page>' in l:
			#print("success" + str(c))
			#print l
			c += 1
			stub = ''
			start_page_flag = True

print "\nTotal pages processed = ", c1 


PAGES.sort()
print PAGES
print "----------------------------------"
print "Ended at ", datetime.datetime.now(), "\n----------------------\n"

#write to a file
import json

with open('PAGES.json', 'w') as f:
    json.dump(PAGES, f)

#LOAD hash-maps using JSON files
import json
import yaml

#LOAD O_C hash-map
with open('PAGES.json') as f:
    PG = yaml.load(f)
print "PAGES loaded !!"

print PG
print PG[10]

#f1.close()



