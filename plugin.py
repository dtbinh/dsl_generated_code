import random
import math
import numpy
def get_neighbour(current,drone_list,radius):
	position=current.xyz
	neighbours=[]
	for drone in drone_list:
		if drone.tag!=current.tag:
			neighbour=drone.xyz
			d=math.sqrt(pow((position[0] - neighbour[0]), 2) + pow((position[1] -neighbour[1]), 2))
			if d<radius:
				neighbours.append(drone)
        return neighbours
def get_drone_position(drone,percentage):
	 if random.randint(0,100)<=percentage:
		print "I am returning true"
		return drone.xyz
	 else: 
		print "I am returning false"
		return numpy.array([0.0,0.0])

	
def get_drone_velocity(drone,percentage):
	 if random.randint(0,100)<=percentage:
		print "I am returning true"
		return drone.v_ned
	 else: 
		print "I am returning false"
		return numpy.array([0.0,0.0])

def return_all_drones_temp(drone_list):
	temp=[]
	for d in drone_list:
		if d.temperature_sensor==True:
			temp.append(d)
	return temp	
			

def return_all_drones_water(drone_list):
	water=[]
	for d in drone_list:
		if d.water_cargo==True:
			water.append(d)
	return water
	
		
	
		
		
	
