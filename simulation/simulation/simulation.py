#!/usr/bin python

from simlib import emitter, bucket, udooGPIO

hit = 0
udoo = udooGPIO.UdooGPIO()

m1a = 16
m1b = 20
m2a = 23
m2b = 4
m3a = 11
m3b = 12
m4a = 13
m4b = 14
m5a = 15
m5b = 18

def setup():
	udoo.Serial(9600)
	udoo.pinMode(3, "OUTPUT")
	udoo.digitalWrite(3, "LOW")
	udoo.pinMode(m1a, "OUTPUT")
	udoo.pinMode(m1b, "OUTPUT")
	udoo.digitalWrite(m1a, "LOW")
	udoo.digitalWrite(m1b, "LOW")

def runMotor(a, b, direction, delay):
	if direction == "down":
		udoo.digitalWrite(a, "HIGH")
		udoo.digitalWrite(b, "LOW")
	elif direction == "up":
		udoo.digitalWrite(a, "LOW")
		udoo.digitalWrite(b, "HIGH")
	udoo.delay(delay)
		
def stopMotor(a, b):
	udoo.digitalWrite(a, "LOW")
	udoo.digitalWrite(b, "LOW")
	

# Simulation function
def startSim():
	global hit, s
	n = 5
	e = [None]*n
	b = [None]*n
	buckInitPos = 0
	simCount = 0
	for i in range(n):
		e[i] = emitter.Emitter(0)
		b[i] = bucket.Bucket(buckInitPos)

	while True:
		for i in range(n):
			collided = e[i].generateSystem()
			if collided == True:
				b[i].update()
				print "bitDrop HIT bucket#", i+1
				hit = i+1
				if hit == 1:
					udoo.SerialWrite('1;%')
					udoo.delay(0.1)
					udoo.digitalWrite(3, "HIGH")
					runMotor(m1a, m1b, "down", 0.01)
				elif hit == 2:
					udoo.SerialWrite('2;%')
					udoo.delay(0.1)
					udoo.digitalWrite(3, "HIGH")
					runMotor(m2a, m2b, "down", 0.01)
				elif hit == 3:
					udoo.SerialWrite('3;%')
					udoo.delay(0.1)
					udoo.digitalWrite(3, "HIGH")
					runMotor(m3a, m3b, "down", 0.01)
				elif hit == 4:
					udoo.SerialWrite('4;%')
					udoo.delay(0.1)
					udoo.digitalWrite(3, "HIGH")
					runMotor(m4a, m4b, "down", 0.01)
				elif hit == 5:
					udoo.SerialWrite('5;%')
					udoo.delay(0.1)
					udoo.digitalWrite(3, "HIGH")
					runMotor(m5a, m5b, "down", 0.01)

			udoo.SerialWrite('0;%')
			udoo.digitalWrite(3, "LOW")
			stopMotor(m1a, m1b)

if __name__ == "__main__":
	setup()
	startSim()
