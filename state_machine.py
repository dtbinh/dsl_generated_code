#!/usr/bin/env python
from state import State 
import rules as sim
class StateMachine:
 states=[]
 initial_state=None
 last_state=None
 current_state=None
 count=1
 current=None
 def __init__(self,current):
	self.current=current
        self.build(self.current)

 def create_initial_state(self,name, role, action_method):
	state=State(name,role,action_method,self.current)
 	self.initial_state=state
 	self.last_state=state
 	print "state ",self.count,state.name
 	self.count=self.count+1
	self.states.append(state)
 	return self
 	
 def create_state(self,name, role, action_method):
	state=State(name,role,action_method,self.current)
	self.last_state.next=state
	self.last_state=state
	print "state ",self.count,state.name
	self.count=self.count+1
	self.states.append(state)
	return self
 def set_current_state(self,new_state, state):
       if state.next==None:
		return
       elif new_state.name==state.name:
	    current_state=state.name
		 
       else: 
	    set_current_state(self,new_state,state.next)
 def build(self,current):
      self.create_initial_state("s1","fire_locator",sim.find_fire).create_state("s2","fire_locator",sim.propagate_fire_position).create_state("s3","fire_fighters",sim.go_to_fire_location).create_state("s4","fire_locator",sim.tend_away_from_fire).create_state("s5","fire_fighters",sim.turn_down_fire)
      for state in self.states:
      	state.execute()
