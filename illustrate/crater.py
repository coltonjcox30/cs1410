import pygame

from text import Text

class Crater:

    def __init__(self, x, y, width, height):
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height
        self.mColor = (102,102,102)
        self.mText = Text("Crater", x + width/2, y + height/2)
        return

    def draw(self, surface):
        rect = pygame.Rect(self.mX, self.mY, self.mWidth, self.mHeight)
        pygame.draw.ellipse(surface, self.mColor, rect, 0)
        self.mText.draw(surface)
        return
