import pygame
import math
import game_mouse
import game
import ball
import paddle

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

        if pygame.K_a in keys:
            print("a key pressed")
            pongball = self.game.getBall()
            pongball.move()
        if 1 in newbuttons:
            pass
        self.game.game_logic(keys, newkeys, buttons, newbuttons, mouse_position)

        if pygame.K_UP in keys:
            print("up key pressed")
            pongpaddle = self.game.getPaddle()
            pongpaddle.moveUP()

        if pygame.K_DOWN in keys:
            print ("down key pressed")
            pongpaddle = self.game.getPaddle()
            pongpaddle.moveDOWN()
        
        if paddle.CollisionPaddleCheck(x,y) == True:
            self.ball.move()
        return


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

    def collision(self):
        pongball = self.game.getBall()
        pongpaddle = self.game.getPaddle()
        if pongball.getX() + pongball.getRadius() == pongpaddle.getX() + pongpaddle.getWidth():
            score(self.Upoint)

        if pongball.getX() + pongball.getRadius() == 0:
            score(self.Cpoint)

def main():
    screen_width = 600
    screen_height = 500
    frames_per_second = 20
    game = PygameStarter(screen_width, screen_height, frames_per_second)
    game.main_loop()
    if game.Cpoint == game.winner:
        print ('Computer Wins!')
        game.EndGame(game.Cpoint)
    if game.Upoint == game.winner:
        print ('You Win!')
        game.EndGame(game.Upoint)
    return
    
if __name__ == "__main__":
    main()

