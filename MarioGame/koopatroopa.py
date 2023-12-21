# This file contains the class of KoopaTroopas, child of enemies and grandchild of sprites
from enemies import Enemies


class KoopaTroopas(Enemies):
    def __init__(self, x, y, direction: int, u=48, v=32, w=-16, h=23, alive=True):
        # These parameters are handled by its parent
        super().__init__(x, y, u, v, w, h, alive, direction)


