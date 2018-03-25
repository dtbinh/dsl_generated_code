#!/usr/bin/env python
from pvector import PVector
import numpy
import math
#import temperature_function as temp
#import plugin

def separation(current):	
	alt_d=8
	close_drones=find_neighbours_in_radius(current,30)
	if len(close_drones)==0:
		velocity=PVector(current.v_ned_d[0],current.v_ned_d[1])
		current.set_v_2D_alt_lya(velocity.return_as_vector(),-alt_d)
	else:
		dx=sub_all_x(close_drones,current)
		dx=dx/len(close_drones)	
		dy=sub_all_y(close_drones, current)
		dy=dy/len(close_drones)
		separation_vec=PVector(dx,dy)
		separation_vec.normalize()
		separation=separation_vec.return_as_vector()
		#current.set_v_2D_alt_lya(separation,-alt_d)
		return separation

def cohesion(current):
	alt_d=8
	position=PVector(current.xyz[0],current.xyz[1])
	close_drones=find_neighbours_in_radius(current,30)
	if len(close_drones)==0:
		velocity=PVector(current.v_ned_d[0],current.v_ned_d[1])
		current.set_v_2D_alt_lya(velocity.return_as_vector(),-alt_d)
	else:
		dx=sum_all_x(close_drones,current)
		dx=dx/len(close_drones)	
		dy=sum_all_y(close_drones, current)
		dy=dy/len(close_drones)
		cohesion_vec=PVector(dx,dy)
		cohesion_vec.subVector(position)
		cohesion_vec.normalize()
		cohesion=cohesion_vec.return_as_vector()
		return cohesion
		#current.set_v_2D_alt_lya(cohesion,-alt_d)

def velavg(current):
	alt_d=8
	close_drones=find_neighbours_in_radius(current,30)
	if len(close_drones)==0:
		velocity=PVector(current.v_ned_d[0],current.v_ned_d[1])
		current.set_v_2D_alt_lya(velocity.return_as_vector(),-alt_d)
	else:
		dx=sum_all_vel_x(close_drones,current)
		dx=dx/len(close_drones)	
		dy=sum_all_vel_y(close_drones, current)
		dy=dy/len(close_drones)
		velavg_vec=PVector(dx,dy)
		velavg_vec.normalize()
		velavg=velavg_vec.return_as_vector()
		#current.set_v_2D_alt_lya(velavg,-alt_d)
		return velavg

def flocking(current):
	alt_d=8
	flocking=separation(current)+cohesion(current)+velavg(current)
	desiredVel=PVector(flocking[0],flocking[1])
       
	
    	if(desiredVel.magnitude()>2):
		desiredVel.normalize()
		desiredVel.mulScalar(2)
    	flocking_vec=desiredVel.return_as_vector()
    	current.set_v_2D_alt_lya(flocking_vec,-alt_d)

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
	
			
