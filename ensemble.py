import plugin

class Ensemble:
 ensemble=None
 agents=None
 name=None
 drone_id=None
 def __init__(self,agents,name):
	self.agents=agents
	self.ensemble=[]
	self.drone_id=[]	
 	
 def register_member(self,drone):
	for d in self.ensemble:
		if drone.tag==d.tag:
			return
	if (drone.temperature_sensor==True):
		self.ensemble.append(drone)
	if (drone.water_cargo==True):
		self.ensemble.append(drone)	
 def delete_member(self): #delete after timeout
        print "hola"
 def synchronize_state(self,current):
	  self.register_member(current)
	  print "synchronizing...........",current.tag
          n_list=plugin.get_neighbour(current,self.agents,50)
	  #print len(n_list), "printing len of n_list"
	  for uav in n_list:
		self.register_member(uav)	  
	  for drone in self.ensemble:	
		#make them execute their state
		if drone.tag!=current.tag:
			current.stat_m.receive_message(drone.stat_m.send_message()) #current receives from everyone in the ensemble
			drone.stat_m.receive_message(current.stat_m.send_message()) #current sends state to everyone in the ensemble
	  #if current.role==current.stat_m.send_message().role:
          current.stat_m.execute(current.stat_m.send_message())
	  for drone in self.ensemble:	
	  	if self.get_state_from_other(drone)==True and drone.stat_m.send_message().name==current.stat_m.send_message().name:			
			count=self.check_others_state(current,drone,current.stat_m.send_message())		
	  		print "I am increasing the counter",count
	  
 def check_others_state(self,current,drone,state):
	if current.role==drone.role: #and current.stat_m.send_message()==drone.stat_m.send_message:
		print "I am in if inside check"
		for d in state.drone_id:
			if d==drone.tag:
				return len(state.drone_id)
		state.drone_id.append(drone.tag)
	#print "len of drone list: ",  len(self.drone_id)
	return len(state.drone_id)
 
 def get_state_from_other(self,drone):
	return drone.stat_m.send_message().complete
 def state_changed(self,drone):
	drone.ensemble.count=0
	del drone.ensemble.drone_id[:]
 
	
 
			
 
	
	
	
