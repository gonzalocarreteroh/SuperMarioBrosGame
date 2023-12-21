# The class is a child of Sprites
from sprites import Sprites


class Coins(Sprites):
    def __init__(self, x, y, appear: bool, u=48, v=104, w=16, h=16):
        # These parameters are handled by its parent
        super().__init__(x, y, u, v, w, h)
        self.appear = appear
        self.const = 1

    # Make the variable private and can not be changed
    @property
    def const(self):
        return self.__const

    @const.setter
    def const(self, const: int):
        self.__const = 1

    def move(self):
        self.x -= self.__const

    # Makes the coins get out of the screen
    def disappear(self):
        self.x = 1000
        self.y = 0
        self.u = 0
        self.v = 0
        self.w = 8
        self.h = 8
