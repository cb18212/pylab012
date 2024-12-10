import math


class Vector2:
	def __init__(self, x,y):
		self.x = x
		self.y = y

	def __add__(self, other):
		return Vector2(self.x + other.x, self.y+other.y)

	def __sub__(self, other):
		return self + (other * -1)

	def __mul__(self, other):
		if (isinstance(other, int) or isinstance(other, float)):
			return Vector2(self.x*other, self.y*other)
		else:
			return Vector2(self.x * other.x, self.y * other.y)

	def __truediv__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			return Vector2(self.x / other, self.y / other)
		else:
			return Vector2(self.x / other.x, self.y / other.y)

	def __abs__(self):
		return Vector2(abs(self.x), abs(self.y))

	def normalized(self):
		return self / self.length()

	def sign(self):
		res = []
		for i in [self.x, self.y]:
			if i == 0:
				res.append(0)
			else:
				res.append(abs(i)/i)
		return Vector2(res[0], res[1])

	def length(self):
		return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

	def __str__(self):
		return f"Vector2({self.x}, {self.y})"
