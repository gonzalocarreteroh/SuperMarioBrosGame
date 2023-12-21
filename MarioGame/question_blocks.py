# The class is a child of Sprites
from sprites import Sprites


# Class for question blocks
class QuestionBlocks(Sprites):
    def __init__(self, x, y, u=16, v=0, w=16, h=16):
        # These parameters are handled by its parent
        super().__init__(x, y, u, v, w, h)
        self.const = 1

# Make the variable private and can not be changed
    @property
    def const(self):
        return self.__const


    @const.setter
    def const(self, const: int):
        self.__const = 1

# This method make the object move one pyxel every frame if the method is called
    def move(self):
        self.x -= self.__const

