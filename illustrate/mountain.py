import pygame

from text import Text

class Mountain:

    def __init__(self, width, height):
        self.mWidth = width
        self.mHeight = height
        self.mColor = (173, 216, 230)
        self.mText = Text("Mountain", width/2, 425)
        return

    def draw(self, surface):
        points = [ (0,500), (0,325), (120,250),
                   (350,375), (475,350), (600,425),
                   (600,500) ]
        pygame.draw.polygon(surface, self.mColor, points, 0)
        self.mText.draw(surface)
        return
