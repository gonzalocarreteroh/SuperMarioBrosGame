# Class child of Sprites
from sprites import Sprites


# Class for the mushrooms
class Mushroom(Sprites):
    def __init__(self, x, y, alive, direction: int, u=0, v=32, w=16, h=16):
        # These variables are taken care off by the mother
        super().__init__(x, y, u, v, w, h)
        self.alive = alive
        self.direction = direction

    # This method allow to move the object one pyxel from frame if the method is called
    def move(self):
        if self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.x -= 1

    # This method comprove the collsion from the left and return a True if happen else,return a False
    def left_collision(self, pipes, breakable, question):
        for i in range(len(pipes)):
            if self.x == pipes[i].x + 30 and self.y > pipes[i].y - 17:
                return True
        for j in range(len(breakable)):
            if self.x == breakable[j].x + 16 and \
                    (breakable[j].y + 16 > self.y >= breakable[j].y - 16):
                return True
        for j in range(len(question)):
            if self.x == question[j].x + 16 and \
                    (question[j].y + 16 > self.y >= question[j].y - 16):
                return True
        return False

    # This method comprove the collsion from the right and return a True if happen else,return a False
    def right_collision(self, pipes, breakable, question):
        for i in range(len(pipes)):
            if self.x + 12 == pipes[i].x and self.y > pipes[i].y - 17:
                return True
        for j in range(len(breakable)):
            if self.x + 12 == breakable[j].x and (
                    breakable[j].y + 16 > self.y > breakable[j].y - 16):
                return True
        for j in range(len(question)):
            if self.x + 12 == question[j].x and (
                    question[j].y + 16 > self.y > question[j].y - 16):
                return True
        return False

    # This method make the object disappear from the screen and turn it to the color of the sky
    def disappear(self):
        self.x = 0
        self.y = 0
        self.u = 0
        self.v = 0
        self.w = 0
        self.h = 0

