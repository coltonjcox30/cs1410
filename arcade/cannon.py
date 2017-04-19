__author__ = 'ccox'
import pygame
import math

class Cannon:
	def __init__(self,width, height, color, point):
		self.mwidth = 30
		self.mheight = 10
		self.color = (255,50,50)
		self.point = 0
		self.area = self.mwidth * self.mheight
		self.x = 450
		self.y = 450
		self.dy = 15
		self.screenwidth = width
		self.screenheight = height

	def __str__(self):
		return 'Cannon('+str(self.mwidth)+', '+str(self.mheight)+')'

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

	#def CollisionPaddleCheck(self,x,y):
	#	if x > self.x and x < self.x + self.mwidth:
	#		if y > self.y and y < self.y + self.mheight:
	#			return True
	#	return False

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

		self.y -= self.dy

		if self.y <= 0:
			self.y = 0				#y = 450 x = 450 w = 30 h = 10 dy = 15

	def moveDOWN(self):
		self.y += self.dy

		if self.y >= self.screenheight:
			self.y = self.screenheight - self.mheight


