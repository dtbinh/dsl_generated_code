#!/usr/bin/env python
from pvector import PVector
import numpy
import math
import temperature_function as temp
#import plugin
import time
from random import randint	
def sub_all_x(close_drones, current):
	dx=0
	for other in close_drones:
		dx-=current.xyz[0]-other.xyz[0]
	return dx
						
def sub_all_y(close_drones, current):
	dy=0
	for other in close_drones:
		dy-=current.xyz[1]-other.xyz[1]
	return dy
def sum_all_x(close_drones, current):
	dx=0
	for other in close_drones:
		dx+=other.xyz[0]
	return dx
						
def sum_all_y(close_drones, current):
	dy=0
	for other in close_drones:
		dy+=other.xyz[1]
	return dy
		
def sum_all_vel_x(close_drones, current):
	dx=0
	for other in close_drones:
		dx+=other.v_ned_d[0]
	return dx
						
def sum_all_vel_y(close_drones, current):
	dy=0
	for other in close_drones:
		dy+=other.v_ned_d[1]
	return dy
		
def find_neighbours_in_radius(current,radius):
	agents=current.group.all_drones
	neibourgh=[]
	for it in agents:
		if euclidean_distance(it.xyz,current.xyz)<=radius and it.role==current.role:
			neibourgh.append(it)
	return neibourgh
		
def euclidean_distance(a,b):
	distance=math.sqrt(pow((a[0] - b[0]), 2) + pow((a[1] - b[1]), 2))
	return distance
def stay_in_border(position):
	v=PVector(0,0)
	Xmin=13
	Xmax=13
	Ymin=13
	Ymax=13
	constant=100
	if position.x <= Xmin:
		v.x = constant
	elif position.x >= Xmax:
		v.x = -constant
		
	if position.y <= Ymin :
		v.y = constant
	elif position.y >= Ymax :
		v.y = -constant
		
	return v.return_as_vector()
def separation (current):
	alt_d=8
	position=PVector(current.xyz[0],current.xyz[1])
	close_drones=find_neighbours_in_radius(current,100)
	if len(close_drones)==0:
		empty=PVector(0,0)
		velocity=PVector(current.v_ned_d[0],current.v_ned_d[1])
		current.set_v_2D_alt_lya(velocity.return_as_vector(),-alt_d)
		return empty.return_as_vector()
	dx=sub_all_x(close_drones,current)
	dx=(dx/len(close_drones))
	dy=sub_all_y(close_drones,current)
	dy=(dy/len(close_drones))
	sep_vector=PVector(dx,dy)
	sep_vector.normalize()
	return 	sep_vector.return_as_vector()

def cohesion (current):
	alt_d=8
	position=PVector(current.xyz[0],current.xyz[1])
	close_drones=find_neighbours_in_radius(current,100)
	if len(close_drones)==0:
		empty=PVector(0,0)
		velocity=PVector(current.v_ned_d[0],current.v_ned_d[1])
		current.set_v_2D_alt_lya(velocity.return_as_vector(),-alt_d)
		return empty.return_as_vector()
	sx=sum_all_x(close_drones,current)
	sx=(sx/len(close_drones))
	sy=sum_all_y(close_drones,current)
	sy=(sy/len(close_drones))
	cohesion_vec=PVector((sx-position.x),(sy-position.y))
	cohesion_vec.normalize()
	return 	cohesion_vec.return_as_vector()

def velavg (current):
	alt_d=8
	position=PVector(current.xyz[0],current.xyz[1])
	close_drones=find_neighbours_in_radius(current,100)
	if len(close_drones)==0:
		empty=PVector(0,0)
		velocity=PVector(current.v_ned_d[0],current.v_ned_d[1])
		current.set_v_2D_alt_lya(velocity.return_as_vector(),-alt_d)
		return empty.return_as_vector()
	velx=sum_all_vel_x(close_drones,current)
	velx=(velx/len(close_drones))
	vely=sum_all_vel_x(close_drones,current)
	vely=(vely/len(close_drones))
	vel_vector=PVector(velx,vely)
	vel_vector.normalize()
	return 	vel_vector.return_as_vector()
def flocking (current):
	print "flocking" 
	flocking_vec=((separation(current)+cohesion(current))+velavg(current))
	alt_d=8
	print flocking_vec, "flocking vector"
	#current.set_v_2D_alt_lya(flocking_vec,-alt_d)
	return flocking_vec
def find_fire (current):
	print "find_fire", current.tag
	alt_d=8
	if not(current.temperature_sensor==True):
			return False
	flocking_vec=flocking(current)
	value=temp.temperature_sensor(current.xyz[0],current.xyz[1],0.0,0.0)
	#print "value", value	
	if value > 800:
		print current.tag, "I am really hot!"
		point=current.xyz
		current.set_xyz_ned_lya(current.xyz)
		return True
	else: current.set_v_2D_alt_lya(flocking_vec,-alt_d)
def propagate_fire_position (current): #more like wait
	print "propagate_fire_position", current.tag
	if not(current.temperature_sensor==True):
		#current.set_xyz_ned_lya(current.xyz)
		return False
	current.set_xyz_ned_lya(current.xyz)
	probability=randint(0, 100)
	if probability<=2:
		return True
		
def tend_away_from_fire (current):
	print "tend_away_from_fire",current.tag
	if not(current.temperature_sensor==True):
		current.set_xyz_ned_lya(current.xyz)
		return False
	alt_d=8
	flocking_vec=flocking(current)
	target=PVector(0,0) #substitute with fire point
	position=PVector(current.xyz[0],current.xyz[1])
	target.subVector(position)
	target.divScalar(1)
	target.normalize()
	target=target.return_as_vector()
	target_fire=flocking_vec+(-1*target)+stay_in_border(position)
	current.set_v_2D_alt_lya(target_fire,-alt_d)
	return False
	
def go_to_fire_location(current):
	print " I am in fire location", current.tag
	if not(current.water_cargo==True):
		current.set_xyz_ned_lya(current.xyz)
		print "I am in not",current.tag
		return False
	print "I am entering this branch"
	alt_d=8
	flocking_vec=flocking(current)
	target=PVector(0,0) #substitute with fire point
	position=PVector(current.xyz[0],current.xyz[1])
	target.subVector(position)
	target.divScalar(10)
	target.normalize()
	target=target.return_as_vector()
	target_fire=flocking_vec+target
	current.set_v_2D_alt_lya(target_fire,-alt_d)
	diff=position.return_as_vector()-target
	print diff, "printing difference between the two"
	if diff[0]<=1 and diff[1]<=1:
		return True
	else: return False
	
def turn_down_fire (current):
	print "turn_down_fire" 
	if not(current.water_cargo==True):
			return False
	return False
def assign_role(current):
	if (current.temperature_sensor==True):
		current.role="fire_locator"
	if (current.water_cargo==True):
		current.role="fire_fighters"
def run_simulation(agents):
	print len(agents), "len agents"
	
