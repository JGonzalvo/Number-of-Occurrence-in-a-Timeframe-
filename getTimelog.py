import shutil
import os
from array import *

root=os.path.dirname(os.path.abspath(__file__))

f = open('timelog.txt')
TotalCase=0
CaseCtr = array('i', [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

for line in iter(f):
	temp=line
	x,temp=temp.split(" ")
	
	if(temp[1]==':'):
		temp=int(temp[0])
	else:
		temp=int(temp[:2])
	
	CaseCtr[temp]=CaseCtr[temp]+1
	
	TotalCase=TotalCase+1
	
f.close()

ctr = 0

fo = open("test.txt","w+")
for x in CaseCtr:
	temp=str(x)
	fo.write(temp + '\n')
	ctr=ctr+1
fo.close()

raw_input("Press Any Key To Continue")