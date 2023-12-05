import turtle
from turtle import *

G = 8
NUM_LOOPS = 4100
RO_X = 0
RO_Y= -85
VO_X = 485
VO_Y = 0

class GravSys():
	def __init__(self):
		self.bodies = []
		self.t = 0
		self.dt = 0.001

	def sim_loop(self):
		for _ in range(NUM_LOOPS):
			self.t += dt
			for body in self.bodies:
				body.step()

class Body(Turtle):
	def __init__(self, mass, start_loc, vel, gravsys, shape):
		super().__init__(shape = shape)
		self.gravsys = gravsys
		self.penup()
		self.mass = mass
		self.setpos(start_loc)
		self.vel = vel
		gravsys.bodies.append(self)
		#self.resizemode('user')
		#self.pendown()

		def acc(self):
			a = Vec(0,0)
			for body in self.gravsys.bodies:
				if body != self:
					r = body.pos() - self.pos()
					a += (G*body.mass / abs(r)**3) * r
			return a

		def step(self):
			dt = self.gravsys.dt
			a  = self.acc()
			self.vel = sel.vel + dt*a
			self.setpos(self.pos() + dt*self.vel)

			if self.gravsys.bodies.index(self) == 2:
				rotate_factor = 0.0006
				self.setheading((self.heading() - rotate_factor*self.xcor()))
				if self.xcor() < -20:
					self.shape('arrow')
					self.shapesize(0.5)
					self.setheading(105)

def main():
	screen = Screen()
	screen.setup(width = 1.0, height = 1.0)
	screen.bgcolor('black')
	screen.title('Apollo 8 Free return simulation')

	gravsys = GravSys()

	image_earth = 'earth_100_100.gif'
	screen.register_shape(image_earth)
	earth = Body(1000000, (0, -25), Vec(0, -2.5), gravsys, image_earth)
	earth.pencolor('white')
	earth.getscreen().tracer(n = 0, delay = 0)

	image_moon = 'moon_27_27.gif'
	screen.register_shape(image_moon)
	moon = Body(32000, (344, 42), Vec(-27, 147), gravsys, image_moon)
	earth.pencolor('gray')
	




