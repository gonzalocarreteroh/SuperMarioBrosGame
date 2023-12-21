# The class is a child of Sprites
from sprites import Sprites


# Class for the castle in the end of the game
class Castle(Sprites):
    def __init__(self, x, y, u=80, v=136, w=64, h=64):
        # These parameters are taken care of by the mother
        super().__init__(x, y, u, v, w, h)
        self.const = 1

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


