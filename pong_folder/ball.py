import random
import pygame
import math

class Ball:
	def __init__(self, x, y, width, height):
		self.radius = 10
		self.x = x
		self.y = y
		self.color = (255,50,50)
		
		self.dx = 15
		self.dy = 15
		self.screenwidth = width
		self.screenheight = height

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def getRadius(self):
		return self.radius

	def reverse(self):
		self.dx *= -1
		self.dy *= -1


	def contains(self, ball):
		x0 = self.x
		y0 = self.y
		R0 = self.radius
		x1 = ball.x
		y1 = ball.y
		R1 = ball.radius
		check = abs(R0-R1) <= math.sqrt((x0-x1)**2+(y0-y1)**2) <= (R0+R1)
		return check


	def move(self):
		self.x += self.dx
		if self.x > self.screenwidth-self.radius or self.x < 0+self.radius:
			self.dx = -1*self.dx

		self.y += self.dy
		if self.y > self.screenheight-self.radius or self.y < 0+self.radius:
			self.dy = -1*self.dy


	def paint(self, surface):
		pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

	def reset(self):
		self.dx = random.randrange(10)
		self.dy = random.randrange(10)
		self.x = 300
		self.y = 250