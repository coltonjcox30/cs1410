__author__ = 'ccox'
import pygame
import math

class Paddle:
	def __init__(self,width, height, color, point):
		self.mwidth = 10
		self.mheight = 70
		self.color = (255,255,255)
		self.point = 0
		self.area = self.mwidth * self.mheight
		self.x = 25
		self.y = 25
		self.dy = 15
		self.screenwidth = width
		self.screenheight = height

	def __str__(self):
		return 'Paddle('+str(self.mwidth)+', '+str(self.mheight)+')'

	def __repr__(self):
		return self.__str__()


	def area(self):
		return self.mwidth * self.mheight

	def getX(self):
		return self.x

	def getWidth(self):
		return self.mwidth


	def perimeter(self):
		return self.mwidth*2 + self.mheight*2

	def scale(self, ratio):
		if ratio > 0:
			self.mwidth = self.mwidth * ratio
			self.mheight *= ratio

	def CollisionPaddleCheck(self,x,y):
		if x > self.x and x < self.x + self.mwidth:
			if y > self.y and y < self.y + self.mheight:
				return True
		return False

	def rotate(self):
		temp = self.mwidth
		self.mwidth = self.mheight
		self.mheight = temp

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
			self.y = self.y

		else:
			self.y -= self.dy

		if self.y > self.screenheight-self.area:
			self.dy = 1*self.dy

	def moveDOWN(self):
		if self.y + self.mheight >= self.screenheight:
			self.y = self.y

		else:
			self.y += self.dy

		if self.y < self.screenheight-self.area:
			self.dy = -1*self.dy


