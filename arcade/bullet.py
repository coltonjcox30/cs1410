import random
import pygame
import math
import cannon

class Bullet:
	def __init__(self, x, y, width, height):
		self.radius = 5
		self.x = x
		self.y = y
		self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
		
		self.dx = 0
		self.dy = 0
		self.screenwidth = width
		self.screenheight = height

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def getRadius(self):
		return self.radius

	def contains(self, wall):
		bx = self.x
		by = self.y
		br = self.radius

		wx = wall.x
		wy = wall.y
		ww = wall.mwidth
		wh = wall.mheight
		if bx - br > wx and bx - br < wx + ww and by > wy and by < wy + wh:

			return True

		else:
			return False

	def move(self):
		self.x += self.dx
		if self.x > self.screenwidth-self.radius or self.x < 0+self.radius:
			self.dx = -1*self.dx

		self.y += self.dy
		if self.y > self.screenheight-self.radius or self.y < 0+self.radius:
			self.dy = -1*self.dy


	def paint(self, surface):
		pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

	def shoot(self,x,y):
		self.dx = -20
		self.x = x
		self.y = y

	def reverse(self):
		self.dx *= -1
		self.dy *= -1
