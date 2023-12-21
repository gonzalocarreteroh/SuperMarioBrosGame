# The class is a child of Sprites
from sprites import Sprites


# Class for breakable blocks
class BreakableBlocks(Sprites):
    def __init__(self, x, y, has_coins: int, multicoins: bool, u=0, v=16, w=16, h=16):
        # Add new variables to the new object
        super().__init__(x, y, u, v, w, h)
        self.has_coins = has_coins
        self.multicoins = multicoins
        self.const = 1

    # Make the variable private and can not be changed
    @property
    def const(self):
        return self.__const

    @const.setter
    def const(self, const: int):
        self.__const = 1

    # This method makes to object move one pyxel every frame if the method is called
    def move(self):
        self.x -= self.__const

