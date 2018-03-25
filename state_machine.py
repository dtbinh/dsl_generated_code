#!/usr/bin/env python
from state import State 
class StateMachine:
 initial_state=None
 last_state=None
 current_state=None
 count=0
 def __init__(self,init):
 	self.initial_state=init
	self.last_state=init
 
 def create_state(self,name, role, action_method):
        state=State(name,role,action_method)
	self.last_state.next=state
	self.last_state=state
	print "state ",self.count,state.name
	self.count=self.count+1
	return self
 def set_current_state(self,new_state, state):
       if state.next==None:
		return
       elif new_state.name==state.name:
	    current_state=state.name
		 
       else: 
	    set_current_state(self,new_state,state.next)

 def build(self):
	self.create_state("hola","hola","hola").create_state("hola1","hola","hola")

 	

