import pygame

#from text import Text

class Crack:

    def __init__(self, x, y):
        self.mX = x
        self.mY = y
        self.mColor = (0, 0, 0)
        self.mThick = 1
        #self.mText = Text("crack", x, y)
        return

    def draw(self, surface):
        p1 = (self.mX-50, self.mY)
        p2 = (self.mX-25, self.mY-25)
        p3 = (self.mX, self.mY)
        p4 = (self.mX+25, self.mY-25)
        p5 = (self.mX+50, self.mY)
        pygame.draw.line(surface, self.mColor,
                         p1, p2, self.mThick)
        pygame.draw.line(surface, self.mColor,
                         p2, p3, self.mThick)
        pygame.draw.line(surface, self.mColor,
                         p3, p4, self.mThick)
        pygame.draw.line(surface, self.mColor,
                         p4, p5, self.mThick)
        #self.mText.draw(surface)
        return
