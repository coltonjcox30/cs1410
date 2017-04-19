import pygame

class Text:

    def __init__(self, string, x, y):
        self.mX = x
        self.mY = y
        self.mString = string
        self.mColor = (0, 0, 0)
        font_height = 24
        self.mFont = pygame.font.SysFont("Courier New", font_height)
        return

    def draw(self, surface):
        text_object = self.mFont.render(self.mString, False, self.mColor)
        text_rect = text_object.get_rect()
        text_rect.center = (self.mX, self.mY)
        surface.blit(text_object, text_rect)
        return
