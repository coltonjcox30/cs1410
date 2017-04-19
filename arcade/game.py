import bullet
import pygame
import cannon
import wall

class Game:
	def __init__(self, width, height):
		self.width = width
		self.height = height

		self.bullet = bullet.Bullet(self.width/2,self.height/2,self.width,self.height)
		
		self.cannon = cannon.Cannon(self.width,self.height,self.width/2,self.height/2)

		self.wall = wall.Wall(self.width, self.height, self.width / 2, self.height / 2)

	def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
		x = mouse_position[0]
		y = mouse_position[1]
		self.bullet.move()
		self.CollisionWall()

		if pygame.K_SPACE in keys:
			self.bullet.shoot(self.cannon.x, self.cannon.y)

	def CollisionWall(self):
		wall = self.wall
		if self.bullet.contains(wall):
			print ('touch')

	def getBullet(self):
		return self.bullet

	def getCannon(self):
		return self.cannon

	def getWall(self):
		return self.wall

	def paint(self, surface):
		self.bullet.paint(surface)
		self.cannon.paint(surface)
		self.wall.paint(surface)