import pygame
import math

#from text import Text

class Hill:

    def __init__(self, x, y):
        self.mX = x
        self.mY = y
        self.mColor = (0, 0, 0)
        self.mThick = 7
        #self.mText = Text("hill", x, y)
        return

    def draw(self, surface):
        rect1 = pygame.Rect(self.mX-25, self.mY, 25, 25)
        rect2 = pygame.Rect(self.mX, self.mY, 25, 25)
        pygame.draw.arc(surface, self.mColor, rect1, 0., math.pi,
                        self.mThick)
        pygame.draw.arc(surface, self.mColor, rect2, 0., math.pi,
                        self.mThick)
        #self.mText.draw(surface)
        return
