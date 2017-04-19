import ball
import pygame
import paddle


class Game:
	def __init__(self, width, height):
		self.width = width
		self.height = height

		self.ball = ball.Ball(self.width/2,self.height/2,self.width,self.height)
		
		self.paddle = paddle.Paddle(self.width,self.height,self.width/2,self.height/2)

	def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
		x = mouse_position[0]
		y = mouse_position[1]
		self.ball.move()

	def getBall(self):
		return self.ball

	def getPaddle(self):
		return self.paddle

	def paint(self, surface):
		self.ball.paint(surface)
		self.paddle.paint(surface)
