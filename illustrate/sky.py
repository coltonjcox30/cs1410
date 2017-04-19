import pygame

from text import Text

class Sky:

    def __init__(self, width, height):
        self.mWidth = width
        self.mHeight = height
        self.mColor = (0,0, 10)
        self.mText = Text("Sky", width/2, height/2)
        return

    def draw(self, surface):
        rect = pygame.Rect(0, 0, self.mWidth, self.mHeight)
        pygame.draw.rect(surface, self.mColor, rect, 0)
        self.mText.draw(surface)
        return
