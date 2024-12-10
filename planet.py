import turtle

import body
import vector
from vector import Vector2


class Planet(body.Body):
	def __init__(self, mass: float, size: float, position: vector.Vector2, vel: vector.Vector2, name = "body", color="green"):
		super().__init__(mass, size, position, name=name, color=color)
		self.vel = vel

	def __str__(self):
		return f"name: {self.name}, mass: {self.mass}, size: {self.size}, position: {self.position}, velocity: {self.vel}"

	def apply_force(self, force: Vector2):
		self.vel += force / self.mass

	def update(self, dt):
		self.position += self.vel * dt
		super().update(dt)
		#print(self)