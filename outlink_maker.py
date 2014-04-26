#!/usr/bin/python
# -*-coding: utf-8 -*-

import re
import datetime

print "\n--------------------------------\nScript started at ", str(datetime.datetime.now())
st = datetime.datetime.now()
outlink = {}

#LOAD hash-maps using JSON files
import json
import yaml

#LOAD O_C hash-map
with open('PAGES.json') as f:
    PAGES = yaml.load(f)
print "PAGES loaded !!"



fh = open("OUT_LINKS.csv", 'w')

N = 0

def process_stub(stub):
	#print("In pricess_stub" + stub)
	import re
	if (re.match(r'.*<ns>0</ns>', stub, re.M)):
		matchObj = re.match( r'.*<title>(.*)</title>.*<id>(.*)</id>.*<revision>.*<text.*>(.*?)</text>.*', stub, re.M)
		#matchObj = re.match( r'.*<title>(.*)</title>.*', stub, re.M)
		#matchObj = re.match( r'.*<text.*>(.*)</text>.*', stub, re.M)
		if matchObj:

			global N
			N = N + 1

			print "processing page no ", N

			#print "matchObj.group(1) : ", matchObj.group(1)
			#print "matchObj.group(2) : ", matchObj.group(2)
			#print "matchObj.group(3) : ", matchObj.group(3)

			#print "\n\n"
			page = matchObj.group(1)
			id = matchObj.group(2)
			text =  matchObj.group(3)

			#find outlinks pages
			matches = re.findall('\[\[(.*?)\]\]', text, re.DOTALL)
			#print(matches)
			out_cnt = len(matches)
			
			#print "\n len = ", out_cnt

			#load the count and links in relevant hash
			#outlink[page] = []

			record = ''
			
			record = str(PAGES.index(page) + 1) + ":"
			
			for l in matches:


				if (re.match(r'^#.*', l, re.M) or (page == l)):	
					#print "\ncaugh the redirect to self"
					continue

				if (re.match(r'.+#.+', l, re.M)):
					temp_obj = re.match(r'(.*)#.+', l, re.M)
					#print "caught the new page - ", temp_obj.group(1)
					#outlink[page].append(temp_obj.group(1))
					record = record + str(PAGES.index(temp_obj.group(1)) + 1) + ","

				elif (re.match(r'^File.*', l, re.M)):
					if (re.match(r'.*\[\[.*', l, re.M)):
						temp_obj = re.match(r'.*\[\[(.*)', l, re.M)
						#print "caught the image page - ", temp_obj.group(1)
						#outlink[page].append(temp_obj.group(1))
						record = record + str(PAGES.index(temp_obj.group(1)) + 1) + ","
					else:
						continue
				
				elif (re.match(r'.*\|.*', l, re.M)):
					#outlink[page].append(l.split("|")[0])
					record = record + str(PAGES.index(l.split("|")[0]) + 1) + ","

				else:
					#outlink[page].append(l)
					record = record + str(PAGES.index(l) + 1) + ","

			record = record[:-2]
			fh.write(record + "\n")

	'''
			#replace ==see also== section with blank

			text = re.sub(r'==Examples==', "", text)
			text = re.sub(r'==See also==', "", text)
			text = re.sub(r'==References==', "", text)

			#remove citation

			text = re.sub(r'&lt;ref&gt.*&lt;/ref&gt;', "", text)




			#remove BOLD & HREF syntax of wiki 
			text = re.sub(r'(\[\[|\]\]|\'\'\'|\'\')', "", text)

			#print "\n\n"
			#print text


			#remove the start date info
			text = re.sub(r'{{.*?}}', "", text)
			#print "\n\n"
			#print text


			#remove the QOTES
			text = re.sub(r'&quot;', "", text)
			#print "\n\n"
			#print text

			#remove the numberings
			text = re.sub(r'#', " ", text)
			#print "\n\n"
			#print text

			#remove indentation marks
			text = re.sub(r'(:|::)', " ", text)


			#replace * by space
			#print "\n\n"
			text = re.sub(r'(\*)', " ", text)
			#print text


			list_tokens = text.split()

			#print "tokns = ", len(list_tokens)


			for t in list_tokens:
				
				t = re.sub(r'[.,?!]+$',"", t)

				if t not in stop_words:			

					if t not in ri_dict:
						ri_dict[t] = []

					if id not in ri_dict[t]:
						ri_dict[t].append(id) 	


			#print "\n\nFollowing s the list\n\n"
			#print ri_dict


		else:
		   #print "No match!!"

'''


#Following is One time read of a file into a list
#WOrks for small files, but big files, we need 1by1 line read
#data = tuple(open("s1.xml", 'r')) 
#data = tuple(open("f50k", 'r')) 
#print(len(data))

c = 1
stub = ''
start_page_flag = False
end_page_flag = False



#FOLLOWING IS THE WAY TO READ 1BY1 LINE
with open('wiki3k') as data:
	for l in data:
		if start_page_flag: 
			if '</page>' not in l:
				l = l.replace("\n", "")
				stub += l
			else:
				start_page_flag = False
				#print stub
				process_stub(stub)
				#if c > 500:
				#	break

		elif not start_page_flag and '<page>' in l:
			#print("success" + str(c))
			#print l
			#print "count = ", c
			#c += 1
			stub = ''
			start_page_flag = True

print "\nTotal pages processed = ", N

#data = tuple(open("f50k", 'r')) 
#print(len(data))

'''
import json

with open('wiki_dict.json', 'w') as f:
    json.dump(ri_dict, f)

#f1.close()

#print "\n\n", outlink

import json

with open('O_L.json', 'w') as f:
    json.dump(outlink, f)

'''

fh.close()

en = datetime.datetime.now()


print "\n-------------------------------\nScript Ended at ", str(datetime.datetime.now())


print "\n TOTAL TIME = ", en - st
