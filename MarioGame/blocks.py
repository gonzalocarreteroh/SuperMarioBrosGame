import pyxel
from sprites import Sprites


# Creates a new class that come from Sprites
class Blocks(Sprites):
    def __init__(self, x, y, u=32, v=104, w=16, h=16):
        # Add new variables to the new class
        super().__init__(x, y, u, v, w, h)
        self.const=1
    # Make thee variable private and can not be changed

    @property
    def const(self):
        return self.__const

    @const.setter
    def const(self, const: int):

        self.__const = 1

    # this method make the object move one pyxel every frame if the method is called

    def move(self):
        self.x -= self.__const

"""
import pyxel
from sprites import Sprites


class Blocks(Sprites):
    def __init__(self, x, y, u=32, v=104, w=16, h=16, colkey=12):
        super().__init__(x, y, u, v, w, h, colkey)
        self.const = 1

    @property
    def const(self):
        return self.__const

    @const.setter
    def const(self, const: int):
        self.__const = 1

    def move(self):
        self.x -= self.__const
"""



