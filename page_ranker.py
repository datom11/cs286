#!/usr/bin/python
# -*-coding: utf-8 -*-

import re
import datetime
from decimal import Decimal

a1 = 0.15
E = 0.00005
O_C = {}
I_L = {}

#LOAD hash-maps using JSON files
import json

#LOAD O_C hash-map 
with open('O_C.json') as f:
    O_C = json.load(f)
print "O_C loaded !!"

with open('I_L.json') as f:
    I_L = json.load(f)
print "I_L loaded !!!"


'''
O_C = {1:3, 2:2, 3:1, 4:2, 5:0}
I_L = { 1:[4], 2: [1], 3: [1, 2], 4: [1], 5: [2, 3, 4] }
'''

N = len(O_C.keys())

print N

#print O_C

#print I_L


A = {} #PageRank Vector 1
B = {} #PageRank Vector 2

#Initially pageranks are 1/N
for k in O_C.keys():
	A[k] = 1.0/N
	#A[k] = 0
	B[k] = 0

#A[1] = 1.0




j = 0
while True:
	#print "B4 : In iteration ", j + 1, " A = ", A, " and B = ", B
	print "iteraation = ", j
	for p in O_C.keys():
		#print "p = ", p
		sum = 0
		if p in I_L:
			for i in I_L[p]:
				sum = sum + A[i]/O_C[i]	

			B[p] = (1.0 - a1)/N + a1*sum 
			#print A

	#print "A4: In iteration ", j + 1, " A = ", A, " and B = ", B

        	
	sum1 = 0
	for t in A.keys():
		sum1 = sum1 + A[t]

	print "sum1 = ", sum1	
	sum2 = 0
	for t in B.keys():
		sum2 = sum2 + B[t]

	print "sum2 = ", sum2	
	#print "Diff = ", Decimal(abs(sum2 - sum1))
	#print "\n"
	if Decimal(abs(sum2 - sum1)) < E:
		print "Got it at iteration no ", j + 1
		break
	A = B.copy()
	j = j +1


#print "Final Pagerank = " , B


with open('PageRanks.json', 'w') as f:
    json.dump(B, f)

'''
f1 = open("PageRanks.dat", 'w')

B = sorted(B.items(), key = lambda t: t[1], reverse=True)

for v in B:
	t = v[1] * 1000
	f1.write(str(v[0]) + "=" + str(t) + "\n" )

f1.close() 
'''
