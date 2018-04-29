#!/usr/bin/env python
from transition import Transition 
from random import randint

class State:
 name=None
 role=None
 event=None
 transition=None
 next=None
 current=None
 complete=False
 drone_id=None
 condition=None
 def __init__(self,name, role, action_method,current,condition):
	self.name=name
	self.role=role
	self.event=action_method
	self.current=current
	#self.create_Transition(condition)
        self.condition=condition
	self.drone_id=[]
 def get_Next(self):
	return next
 
 def set_Name(self, next):
	self.next=next

 def execute(self):
	#print "I am executing a state", self.current.role, self.role
	#print "I am executing a state...",self.current.tag
	#probability=randint(0, 100)
	#if probability<=10:
	#	result=True
	#else: result=False
	result=self.event(self.current)
	
	if result==True:
	   print "The result was true", result, self.name,self.current.tag
	   self.complete=True
	print self.current.tag, "I am in state current"
	#if self.current.role==self.role:
	#	return True #change check return value from method
	
	#print self.name
	#self.event(self.current)

 def create_Transition(self,condition):
	self.transition=Transition(self,condition,self.next)
 
 def getNext(self):
	if self.transition.condition.getConditionStatus()==True: #and self.current.role==self.next.role:
		return self.next
	#else: return self
	#print "I am trying to get next...",self.transition.condition.getConditionStatus()
	#print self.role, "current", self.current.role
	#checks to see if the role can get it       
	
	#if self.transition.condition.getConditionStatus()==True :#and self.current.role==self.role:
	#	print "condition has been satisfied", self.name
	#		print self.role, "current", self.current.role
	#	return self.next
	#return None
	
	
	

 


