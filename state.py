#!/usr/bin/env python
class State:
 name=None
 role=None
 action=None
 next=None
 current=None
 def __init__(self,name, role, action_method,current):
	self.name=name
	self.role=role
	self.action=action_method
	self.current=current
 	
 def get_Next(self):
	return next
 
 def set_Name(self, next):
	self.next=next

 def execute(self):
	print "I am executing a state..."
	print self.name
	self.action(self.current)

 


