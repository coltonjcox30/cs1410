import pygame

from text import Text

class Planet:

    def __init__(self, x, y, r):
        self.mX = x
        self.mY = y
        self.mRadius = r
        self.mColor = (102,102,102)
        self.mText = Text("Planet", x, y)
        return

    def setColor(self, r, g, b):
        self.mColor = (int(r), int(g), int(b))
        return
        
    def draw(self, surface):
        center = (self.mX, self.mY)
        pygame.draw.circle(surface, self.mColor, center, self.mRadius, 0)
        self.mText.draw(surface)
        return
