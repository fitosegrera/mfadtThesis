#!/usr/bin python

class Bucket:
	def __init__(self, y):
		self.y = y
		self.q = 0

	def update(self):
		self.y += 1