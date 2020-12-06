from scene import *
from math import *

w = 220
h = 120


class MyPoint():
	x = 0
	y = 0
	color = (0,0,0)
	
	def __init__(self, x, y, color):
		self.x = x
		self.y = y
		self.color = color

points = []

points.append(MyPoint(40, 700, (1,0,0)))
points.append(MyPoint(1000, 700, (0,1,0)))
points.append(MyPoint(500, 20, (0,0,1)))
		
class MyScene(Scene):
	measurePoint = MyPoint(0, 0, (0,0,0)) 
	
	def setup(self):
		pass
		
	def touch_moved(self, touch):
		self.measurePoint.x = touch.location.x
		self.measurePoint.y = touch.location.y
		
	def update(self):
		fill(*self.measurePoint.color)
		rect(self.measurePoint.x-50, self.measurePoint.y-50, 100, 100)
		
		distance1 = math.hypot((points[0].x - self.measurePoint.x), (points[0].y - self.measurePoint.y))
		distance1 = 1 / distance1
		'print("Distance to point 1: " + str(distance1))'
		
		distance2 = math.hypot((points[1].x - self.measurePoint.x), (points[1].y - self.measurePoint.y))
		distance2 = 1 / distance2
		'print("Distance to point 2: " + str(distance2))'
		

		distance3 = math.hypot((points[2].x - self.measurePoint.x), (points[2].y - self.measurePoint.y))
		distance3 = 1 / distance3
		'print("Distance to point 3: " + str(distance3))'
		
		summedDistance = distance1 + distance2 + distance3
		finalColor = ((distance1 / points[0].color[0] / summedDistance), (distance2 / points[1].color[1] / summedDistance), (distance3 / points[2].color[2] / summedDistance))
		self.measurePoint.color = finalColor
		
		if (distance1 != 0) or (distance2 != 0) or (distance3 != 0):
			barva = distance1 / points[0].color[0] + distance2 / points[1].color[1] + distance3 / points[2].color[2]

		for point in points:
			fill(*point.color)
			rect(point.x-15, point.y-15, 15, 15)
		
run(MyScene())



