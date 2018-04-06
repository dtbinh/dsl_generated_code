#!/usr/bin/env python
from state import State 
from transition import Transition 
from condition import Condition 
import rules as sim


class StateMachine:
 states=None
 initial_state=None
 last_state=None
 current_state=None
 current=None
 count=1
 def __init__(self,current):
	self.states=[]
 	self.current=current
 	self.build()
	
 def create_initial_state(self,name, role, action_method,condition):
	state=State(name,role,action_method,self.current,condition)
	self.initial_state=state
	self.last_state=state
	self.current_state=self.initial_state
	#print "state ",self.count,state.name
	self.count=self.count+1
	self.states.append(state)
	return self
 	
 def create_state(self,name, role, action_method,condition):
	state=State(name,role,action_method,self.current,condition)
	self.last_state.next=state
	self.last_state=state
	#print "state ",self.count,state.name
	self.count=self.count+1
	self.states.append(state)
	return self
 
 def receive_message(self,new_state):
	 if self.current_state.next!=None:
	 	self.update_state(new_state,self.current_state.next)

 def update_state(self,new_state,current_state):
	if current_state==None:
		return
	elif current_state.name==new_state.name:
		print "updating state"
		self.current_state=new_state
		
	elif(current_state.next!=None): self.update_state(new_state,current_state.next)
		
 def execute(self, state):
	#if state.next==None:
	#	return
	if state.role==self.current.role:
		print "I am in state machine", state.role, self.current.role
		state.execute()
		if self.current_state.next!=None and state.complete==True:
			self.current_state=self.current_state.next
	
		
	
 def send_message(self):
	return self.current_state

 def print_states(self,state):
	print "current state= ",state.name
	if state.next==None:
		return
	self.print_states(state.next)
 
 def build(self):
      self.create_initial_state("s1","fire_locator",sim.find_fire,Condition(False,True,10)).create_state("s2","fire_locator",sim.propagate_fire_position,Condition(False,True,10)).create_state("s3","fire_fighters",sim.go_to_fire_location,Condition(False,True,10)).create_state("s4","fire_locator",sim.tend_away_from_fire,Condition(False,True,10)).create_state("s5","fire_fighters",sim.turn_down_fire,Condition(False,True,10))
      

      #self.print_states(self.initial_state);
      #for state in self.states:
      #	state.getNext()
	
