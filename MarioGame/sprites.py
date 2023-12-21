# This file contains the mother class of every other class except App, Constants and Head
import pyxel


# This class takes the necessary attributes to draw the image
class Sprites:
    def __init__(self, x, y, u, v, w, h, colkey=12):
        self.x = x
        self.y = y
        self.u = u
        self.h = h
        self.w = w
        self.v = v
        self.colkey = colkey

    def draw(self):
        # Draws the sprite
        pyxel.blt(self.x, self.y, 0, self.u, self.v, self.w, self.h, self.colkey)

    def gravity(self):
        # For all objects there is a force of gravity
        self.y += 1
