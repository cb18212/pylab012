import body
from vector import Vector2
import planet
from copy import *

class SolarSystem():

	G = (6.67430*pow(10,-11))

	def __init__(self, sun_mass, sun_size, color="yellow"):
		self.planets = []
		self.sun = body.Body(sun_mass, sun_size, Vector2(0,0), name="sun", color=color)

	def add_planet(self, planet):
		self.planets.append(planet)
	
	def get_planets(self):
		return copy(self.planets)
	
	def get_gravity_force(self, p):
		diff = (self.sun.position - p.position)
		force = (SolarSystem.G * self.sun.mass * p.mass)
		return diff.normalized() * (pow(diff.length(), 2)) * force

	def run(self, dt):
		for sol_body in self.planets:
			if isinstance(sol_body, planet.Planet):
				sol_body.apply_force(self.get_gravity_force(sol_body) * dt)
				sol_body.update(dt)