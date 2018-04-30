import plugin
import math

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
	  n_list=[]
	  self.register_member(current)
	  print "synchronizing...........",current.tag
	  for d in self.agents:
		if d.heartbeat(current,100)== True:
			n_list.append(d);
          #print (n_list), "printing len of n_list"
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
	 
	  print "------------------------------------MERGING-----------------------------------------------------------------------"
	  
	  for other in n_list:
		if other.tag!=current.tag:
			
			if len(other.var)==0 and len(current.var)!=0:
				print "I am in case 1"
				other.shared_variable(current.var)

			if len(other.var)!=0 and len(current.var)==0:
				print "I am in case 2"
				current.shared_variable(other.var)

			if len(other.var)!=0 and len(current.var)!=0:
				print "I am in case 3"
			        self.merge(current.var,other.var)

	  n_list[:] = []

 
 def merge(self,fire,other_fire):
 	for old in fire:
		for new in other_fire:
			self.set_union(fire,old,new)
 def set_union(self,fire,old,new):
	if self.distance(old,new)>1 and self.not_found(fire,new,1)==True:
		fire.append(new)

 def distance(self,old,new):
	distance=math.sqrt(pow((old[0] - new[0]), 2) + pow((old[1] - new[1]), 2))#+ pow((z1 - z2), 2))
 	return distance
 def not_found(self,fire,new,radius):
		for point in fire:
			if abs(point[0]-new[0])<=radius and abs(point[1]-new[1])<=radius:
				return False
		return True
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
 
	
 
			
 
	
	
	
