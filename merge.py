
#!/usr/bin/env python
from pvector import PVector
import numpy
import math
import temperature_function as temp
#import plugin
import time
from random import randint
#############################points vectors#################################################################################	
def max(first,second): ####more near in space	
	
def min(first,second): ####more far in space

def avg(first,second): ########average point#####
	one=PVector(first[0],first[1])
	second=PVector(second[0],second[1])
	one.mean(second)
	return one.return_as_vector()

def set_union(list_first,list_second): ######add two list together 
	union_set=[]
	union_set=list_first
	for i in list_first:
		for j in list_second:
			result=check(i,j)
			if result==False:
				union_set.append(j)
	return union_set
							
def check(first, second):
	x=i.x
	y=i.y
	x1=j.x
	y1=j.y
	if x-x1==0 and y-y1==0:
		return True
	else: return False

def merge_point(current_list,second,distance):
	
	if one.x-second.x==distance and one.y-second.y=distance:
		

def stack(size):

def queue(size):

def newest(first,second):


