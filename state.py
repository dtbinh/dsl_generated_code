#!/usr/bin/env python
class State:
 name=None
 role=None
 action=None
 next=None
 def __init__(self,name, role, action_method):
	self.name=name
	self.role=role
	self.action=action_method
 	
 def get_Next(self):
	return next
 
 def set_Name(self, next):
	self.next=next

 


