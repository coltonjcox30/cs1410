import pygame

from text import Text

class Star:

    def __init__(self, width, height):
        self.mWidth = width
        self.mHeight = height
        self.mColor = (255, 255, 255)
        self.mText = Text("", width/2, 425)
        return

    def draw(self, surface):
        points = [ (415,250), (450,250), (475,200),
                   (500,250), (535,250), (500,290),
                   (535,350), (475,315) ,(415,350), (450,290)]
        pygame.draw.polygon(surface, self.mColor, points, 0)
        self.mText.draw(surface)
        return
