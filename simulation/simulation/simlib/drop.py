#!/usr/bin python

class Drop:

	#Setup a drop emitter
	def __init__(self, y):
		self.r = 3
		self.y = 1
		self.speed = 1.2

	#update the speed of the particle by with its increment
	def update(self):
		self.y *= self.speed

	#Check if the drop reached the bottom of an obstacle
	def reachedBottom(self, limit, total):
		for i in range(total):
			if (self.y >= (limit + self.r*30)):
				return True
			else:
				return False