# This file contains the class of Goombas and is a child of enemies and grandchild of sprites
from enemies import Enemies


class Goombas(Enemies):
    def __init__(self, x, y, direction: int, u=32, v=48, w=16, h=16, alive=True):
        # This parameters are taken care off by the mother
        super().__init__(x, y, u, v, w, h, alive, direction)




