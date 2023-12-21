# This file contains a class that is child of sprites and mother of goombas and koopatropas
from sprites import Sprites


# Class for the enemies
class Enemies(Sprites):
    def __init__(self, x, y, u, v, w, h, alive, direction: int):
        # These parameters are taken care off by the mother
        super().__init__(x, y, u, v, w, h)
        self.alive = alive
        self.direction = direction

# this method make the object move in one direction if the method is called and the direction
# depend to the value of direction.

    def move(self):
        if self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.x -= 1
        elif self.direction==0:
            self.x=self.x

# This method make the object disappear from the screen and turn it to the color of the sky
    def disappear(self):
        self.x= 100000
        self.y = 0
        self.u = 0
        self.v = 0
        self.w = 8
        self.h = 8







