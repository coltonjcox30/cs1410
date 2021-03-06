__author__ = 'ccox'
import pygame
import math
import random
import game
class Wall:
	def __init__(self,width, height, color, point):
		self.mwidth = 30
		self.mheight = 100
		self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
		self.point = 0
		self.area = self.mwidth * self.mheight
		self.x = x
		self.y = y
		self.dy = 15
		self.screenwidth = width
		self.screenheight = height

	def __str__(self):
		return 'Walls('+str(self.mwidth)+', '+str(self.mheight)+')'

	def __repr__(self):
		return self.__str__()

	def area(self):
		return self.mwidth * self.mheight

	def getX(self):
		return self.x

	def getWidth(self):
		return self.mwidth

	def getHeight(self):
		return self.mheight

	def perimeter(self):
		return self.mwidth*2 + self.mheight*2

	def scale(self, ratio):
		if ratio > 0:
			self.mwidth = self.mwidth * ratio
			self.mheight *= ratio

	def CollisionWallCheck(self,x,y):
		if x > self.x and x < self.x + self.mwidth:
			if y > self.y and y < self.y + self.mheight:
				return True
		return False

	def intersects(self, other):
		x1,y1 = self.point.getTuple()
		w1,h1 = self.mwidth, self.mheight

		x2,y2 = other.point.getTuple()
		w2,h2 = other.mwidth, other.mheight

		l = [(x2,y2), (x2+w2, y2), (x2, y2+h2), (x2+w2, y2+h2)]

		for x,y in l:
			if x >= x1 and x <= x1+w1 and y >= y1 and y <= y1+h1:
				return True
		return False

	def paint(self, surface):
		pygame.draw.rect(surface,self.color,(self.x,self.y,self.mwidth,self.mheight),self.point)

	def moveUP(self):
		if self.y < 0:
			self.y = self.y					#y = 450 x = 450 w = 30 h = 10 dy = 15

		else:
			self.y -= self.dy

		if self.y < self.screenheight-self.area:
			self.dy = 1*self.dy

	def moveDOWN(self):
		if self.y + self.mheight >= self.screenheight:
			self.y = self.y

		else:
			self.y += self.dy

		if self.y < self.screenheight-self.area:
			self.dy = -1*self.dy


