#
# Draw picture
#

import pygame
import math
import game_mouse
from picture import Picture

class PygameSunset(game_mouse.Game):

    def __init__(self, width, height):

        game_mouse.Game.__init__(self, "planet",
                                 width,
                                 height,
                                 10)
        
        self.font_height = 12
        self.font = pygame.font.SysFont("Courier New", self.font_height)
        self.mPicture = Picture(width, height)
        return
        
        
    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        x = mouse_position[0]
        y = mouse_position[1]

        if pygame.K_a in newkeys:
            print("a key pressed")
        
        if 1 in newbuttons:
            print("button clicked")

        return
    
    def paint(self, surface):
        self.mPicture.draw(surface)
        return

def main():
    pygame.font.init()
    game = PygameSunset(600, 500)
    game.main_loop()
    
if __name__ == "__main__":
    main()

