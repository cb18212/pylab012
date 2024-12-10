import turtle

import vector


class Body:

	def __init__(self, mass: float, size: float, position: vector.Vector2, name = "body", color="green"):
		self.name = name
		self.mass = mass
		self.size = size
		self.position = position
		self.t = turtle.Turtle("circle")
		self.t.speed(100000)
		self.t.color(color)
		self.t.penup()
		self.t.goto(self.position.x, self.position.y)
		self.t.pendown()
	
	def __str__(self):
		return f"name: {self.name}, mass: {self.mass}, size: {self.size}, position: {self.position}"
	
	def update(self, dt):
		self.t.goto(self.position.x, self.position.y)