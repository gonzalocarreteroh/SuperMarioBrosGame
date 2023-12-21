# This class is a child of Enemies and grandchild of Sprites
from enemies import Enemies


# Class for the plant
class Carnivorous(Enemies):
    def __init__(self, x, y, direction: int, u=0, v=216, w=16, h=16, alive=True):
        # These parameters are handled by its parent
        super().__init__(x, y, u, v, w, h, alive, direction)
        self.sube=True
        self.baja=False

    # this method make the object move one pyxel every frame if the method is called

    def move(self):
        self.x -= 1

    # this method make the object move one pyxel every frame in the Y axis if the method is called
    # and control that the object up and down in a determinates coordinates

    def constantmove(self, pipes):
        if self.y == pipes[0].y - 16:
            self.sube=False
            self.baja=True
        elif self.y== pipes[0].y + 16:
            self.sube=True
            self.baja=False
        if self.sube:
            self.y-=1
        elif self.baja:
            self.y+=1
