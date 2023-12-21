# Class child of Sprites
from sprites import Sprites


# Class for the pipes
class Pipes(Sprites):
    def __init__(self, x, y, u=32, v=0, w=32, h=32):
    # This parameters are taken care off by the mother
        super().__init__(x, y, u, v, w, h)
    # Variable constant to the movement
        self.const = 1

    # Make the variable private and can not be changed

    @property
    def const(self):
        return self.__const

    @const.setter
    def const(self,const: int):
        self.__const = 1

    # This method make the object move one pyxel every frame if the method is called
    def move(self):
        self.x -= self.__const

