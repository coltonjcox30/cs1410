import pygame

from sky import Sky
from planet import Planet
from mountain import Mountain
from crater import Crater
from crack import Crack
from hill import Hill
from star import Star

class Picture:
    def __init__(self, width, height):
        self.mWidth = width
        self.mHeight = height
        self.mSky = Sky(width, height)
        self.mPlanet1 = Planet(200, 210, 215)
        self.mPlanet1.setColor(204, 204, 204)
        self.mMountain1 = Mountain(width, height)
        self.mCrater1 = Crater(40, 130, 100, 100)
        self.mCrater2 = Crater(35, 120, 50, 50)
        self.mCrater3 = Crater(90,10,90,90)
        self.mCrater4 = Crater(250,90,100,100)	
        self.mCrack1 = Crack(290, 250)
        self.mCrack2 = Crack(285, 240)
        self.mHill1 = Hill(175, 400)
        self.mHill2 = Hill(300, 380)
        self.mHill3 = Hill(500, 450)
        self.mStar = Star(width, height)
        return

    def draw(self, surface):
        self.mSky.draw(surface)
        self.mPlanet1.draw(surface)
        self.mMountain1.draw(surface)
        self.mCrater1.draw(surface)
        self.mCrater2.draw(surface)
        self.mCrater3.draw(surface)
        self.mCrater4.draw(surface)
        self.mCrack1.draw(surface)
        self.mCrack2.draw(surface)
        self.mHill1.draw(surface)
        self.mHill2.draw(surface)
        self.mHill3.draw(surface)
        self.mStar.draw(surface)
        return
