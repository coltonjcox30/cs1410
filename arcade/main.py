import pygame
import math
import game_mouse
import game
import bullet
import cannon
import wall
# Starter code for PyGame applications

class PygameStarter(game_mouse.Game):

    def __init__(self,width, height, fps):

        game_mouse.Game.__init__(self, "Pygame Starter",
                                 width,
                                 height,
                                 fps)

        self.game = game.Game(width, height)
        self.Upoint = 0
        self.Cpoint = 0
        self.winner = 1
        return
        
    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        x = mouse_position[0]
        y = mouse_position[1]

        if pygame.K_SPACE in keys:
            Bullet = self.game.getBullet()
            #Bullet.reset()
            print('SHOTS FIRED!')

        if pygame.K_a in keys:
            print("a key pressed")
            C_bullet = self.game.getBullet()
            C_bullet.move()
        if 1 in newbuttons:
            pass
        self.game.game_logic(keys, newkeys, buttons, newbuttons, mouse_position)

        if pygame.K_UP in keys:
            print("up key pressed")
            C_bullet = self.game.getCannon()
            C_bullet.moveUP()

        if pygame.K_DOWN in keys:
            print ("down key pressed")
            C_bullet = self.game.getCannon()
            C_bullet.moveDOWN()



        return

        def GreatWall(self,x,y):
		w1 = (self.mwidth,self.mheight,x,0)

    #def EndGame(self,player):
        # freeze the ball & paddle
        # display text on screen (winner & points)
        # give user option to exit with quit()
        #   if pygame.K_q: quit()

    def paint(self, surface):
        surface.fill((0,0,0))
        self.game.paint(surface)
        return

    def score(self,player):
        player += 1

def main():
    screen_width = 600
    screen_height = 500
    frames_per_second = 20
    game = PygameStarter(screen_width, screen_height, frames_per_second)
    game.main_loop()
    return
    
if __name__ == "__main__":
    main()

