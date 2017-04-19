import pygame
class picture:
    def __init__(self, string, x, y):
        self.mX = x
        self.mY = y
        self.mString = string
        self.mColor = (0, 0, 0)
        font_height = 24
        self.mFont = pygame.font.SysFont("Courier New", font_height)
        return
 
    def draw(self, surface):
        pic_object = self.mFont.render(self.mString, False, self.mColor)
        pic_rect = text_object.get_rect()
        pic_rect.center = (self.mX, self.mY)
        surface.blit(text_object, text_rect)
        return


class Sky:
    def __init__(self, width, height):
        self.mWidth = width
        self.mHeight = height
        self.mColor = (135, 206, 235)
        self.mText = Text("Sky", width/2, height/2)
        return
 
    def draw(self, surface):
        rect = pygame.Rect(0, 0, self.mWidth, self.mHeight)
        pygame.draw.rect(surface, self.mColor, rect, 0)
        self.mText.draw(surface)
        return

class Sun:

    def __init__(self, x, y, r):
        self.mX = x
        self.mY = y
        self.mRadius = r
        self.mColor = (255, 150, 3)
        self.mText = Text("Sun", x, y)
        return

    def setColor(self, r, g, b):
        self.mColor = (int(r), int(g), int(b))
        return
    
    def draw(self, surface):
        center = (self.mX, self.mY)
        pygame.draw.circle(surface, self.mColor, center, self.mRadius, 0)
        self.mText.draw(surface)
        return
    
class Mountain:
    
    def __init__(self, width, height):
        self.mWidth = width
        self.mHeight = height
        self.mColor = (224, 162, 245)
        self.mText = Text("Mountain", width/2, 425)
        return
    
    def draw(self, surface):
        points = [ (0,500), (0,350), (125,225),
                   (350,375), (475,300), (600,425),
                   (600,500) ]
        pygame.draw.polygon(surface, self.mColor, points, 0)
        self.mText.draw(surface)
        return

class Cloud:

    def __init__(self, x, y, width, height):
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height
        self.mColor = (237, 107, 181)
        self.mText = Text("Cloud", x + width/2, y + height/2)
        return
    
    def draw(self, surface):
        rect = pygame.Rect(self.mX, self.mY, self.mWidth, self.mHeight)
        pygame.draw.ellipse(surface, self.mColor, rect, 0)
        self.mText.draw(surface)
        return
class BigBird:

    def __init__(self, x, y):
        self.mX = x
        self.mY = y
        self.mColor = (0, 0, 0)
        self.mThick = 3
        #self.mText = Text("Big Bird", x, y)
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
import math

class SmallBird:

    def __init__(self, x, y):
        self.mX = x
        self.mY = y
        self.mColor = (0, 0, 0)
        self.mThick = 2
        #self.mText = Text("Small Bird", x, y)
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

class Picture:
 
    def __init__(self, width, height):
        self.mWidth = width
        self.mHeight = height
 
        self.mSky = Sky(width, height)
        self.mSun1 = Sun(400, 300, 75)
        self.mSun2 = Sun(500, 50, 55)
        self.mSun2.setColor(240, 70, 0)
        self.mMountain = Mountain(width, height)
        self.mCloud1 = Cloud(50, 175, 200, 100)
        self.mCloud2 = Cloud(350, 50, 125, 75)
        self.mBigBird = BigBird(525, 200)
        self.mSmallBird1 = SmallBird(150, 75)
        self.mSmallBird2 = SmallBird(175, 100)
        self.mSmallBird3 = SmallBird(100, 125)
        return

    def draw(self, surface):
        self.mSky.draw(surface)
        self.mSun1.draw(surface)
        self.mSun2.draw(surface)
        self.mMountain.draw(surface)
        self.mCloud1.draw(surface)
        self.mCloud2.draw(surface)
        self.mBigBird.draw(surface)
        self.mSmallBird1.draw(surface)
        self.mSmallBird2.draw(surface)
        self.mSmallBird3.draw(surface)
        return

import pygame.locals

class Game:
    def __init__(self, name, width, height, frames_per_second):
        self.width = width
        self.height = height
        self.frames_per_second = frames_per_second
        self.on = True

        self.screen = pygame.display.set_mode(
                # set the size
                (width, height),

                # use double-buffering for smooth animation
                pygame.locals.DOUBLEBUF |

                # apply alpha blending
                pygame.locals.SRCALPHA)

        # set the title of the window
        pygame.display.set_caption(name)

    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        raise NotImplementedError()

    def paint(self, surface):
        raise NotImplementedError()

    def main_loop(self):
        clock = pygame.time.Clock()
        keys = set()
        buttons = set()
        mouse_position = (1,1)

        while True:
            clock.tick(self.frames_per_second)

            newkeys = set()
            newbuttons = set()
            for e in pygame.event.get():
                # did the user try to close the window?
                if e.type == pygame.QUIT:
                    pygame.quit()
                    return

                # did the user just press the escape key?
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

                # track which mouse buttons are currently pressed
                if e.type == pygame.MOUSEBUTTONDOWN:
                    buttons.add(e.button)
                    newbuttons.add(e.button)
                    mouse_position = e.pos

                if e.type == pygame.MOUSEBUTTONUP:
                    buttons.discard(e.button)
                    mouse_position = e.pos

                if e.type == pygame.MOUSEMOTION:
                    mouse_position = e.pos
                
                # track which keys are currently set
                if e.type == pygame.KEYDOWN:
                    keys.add(e.key)
                    newkeys.add(e.key)
                if e.type == pygame.KEYUP:
                    keys.discard(e.key)

            if self.on:
                self.game_logic(keys, newkeys, buttons, newbuttons, mouse_position)
                self.paint(self.screen)

            pygame.display.flip()

class PygameSunset(game_mouse.Game):

    def __init__(self, width, height):

        game_mouse.Game.__init__(self, "Sunset",
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
