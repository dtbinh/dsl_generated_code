#!/usr/bin/env python
from pvector import PVector
import numpy
import math
#import temperature_function as temp
#import plugin
	
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
	agents=current.group.neibourgh_list
	neibourgh=[]
	for it in agents:
		if euclidean_distance(it.xyz,current.xyz)<=radius:
			neibourgh.append(it)
	return neibourgh
		
def euclidean_distance(a,b):
	distance=math.sqrt(pow((a[0] - b[0]), 2) + pow((a[1] - b[1]), 2))
	return distance

def separation (current):
	alt_d=8
	position=PVector(current.xyz[0],current.xyz[1])
	close_drones=find_neighbours_in_radius(current,30)
	if len(close_drones)==0:
		velocity=PVector(current.v_ned_d[0],current.v_ned_d[1])
		current.set_v_2D_alt_lya(velocity.return_as_vector(),-alt_d)
		return 
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
	close_drones=find_neighbours_in_radius(current,30)
	if len(close_drones)==0:
		velocity=PVector(current.v_ned_d[0],current.v_ned_d[1])
		current.set_v_2D_alt_lya(velocity.return_as_vector(),-alt_d)
		return 
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
	close_drones=find_neighbours_in_radius(current,30)
	if len(close_drones)==0:
		velocity=PVector(current.v_ned_d[0],current.v_ned_d[1])
		current.set_v_2D_alt_lya(velocity.return_as_vector(),-alt_d)
		return 
	velx=sum_all_vel_x(close_drones,current)
	velx=(velx/len(close_drones))
	vely=sum_all_vel_x(close_drones,current)
	vely=(vely/len(close_drones))
	vel_vector=PVector(velx,vely)
	vel_vector.normalize()
	return 	vel_vector.return_as_vector()
def flocking (current):
	print flocking 
	flocking_vec=((separation(current)+cohesion(current))+velavg(current))
	alt_d=8
	current.set_v_2D_alt_lya(flocking_vec,-alt_d)
def find_fire (current):
	print find_fire 
	if not(current.temperature_sensor==True):
			return
def propagate_fire_position (current):
	print "propagate_fire_position" 
	if not(current.temperature_sensor==True):
			return
def tend_away_from_fire (current):
	print "tend_away_from_fire" 
	if not(current.temperature_sensor==True):
			return
def go_to_fire_location (current):
	print "go_to_fire_location" 
	if not(current.water_cargo==True):
			return
def turn_down_fire (current):
	print "turn_down_fire" 
	if not(current.water_cargo==True):
			return
