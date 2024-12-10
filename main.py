from time import sleep

import vector
from planet import Planet
from solar_system import SolarSystem
from vector import Vector2
from turtle import *


sol_sys = SolarSystem(10000000, 5000)
sol_sys.add_planet(Planet(47.5, 100, Vector2(5, 200), Vector2(25,1), name="earth", color="green"))
sol_sys.add_planet(Planet(40.5, 200, Vector2(10.0,125), Vector2(62, 0.1), name="mars", color="red"))
step_size = 10
update_delay = 0.01
while True:
	sol_sys.run(step_size * update_delay)
	sleep(update_delay)