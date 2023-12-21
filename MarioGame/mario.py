# This file contains the class for Mario, a child of sprites
import pyxel
from sprites import Sprites


class Mario(Sprites):
    def __init__(self, x, y, u, v, in_floor: bool, direc: int, big: bool, w=16, h=16):
        # These parameters are taken care of by the mother
        super().__init__(x, y, u, v, w, h)
        self.in_floor = in_floor
        self.direc = direc
        self.big = big
        self.vy = 10
        self.skincount = 0
        self.m = 168
        self.itsluigi = False

    # Moves Mario one pyxel to the right
    def move_right(self):
        self.x += 1

    # Moves Mario one pyxel to the left
    def move_left(self):
        self.x -= 1

    # Checks collisions on the left between Mario and and the objects
    def left_collision(self, pipes, breakable, question):
        for i in range(len(pipes)):
            if self.x == pipes[i].x + 30 and self.y > pipes[i].y - 17:
                return True
        for j in range(len(breakable)):
            if self.x == breakable[j].x + 16 and \
                    (breakable[j].y + 16 > self.y > breakable[j].y - 16):
                return True
        for j in range(len(question)):
            if self.x == question[j].x + 16 and \
                    (question[j].y + 16 > self.y >= question[j].y - 16):
                return True
        return False

    # Checks collisions on the right between Mario and and the objects
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

    # Checks collisions between Mario and and the objects if the objects are moving back
    def moving_collision(self, pipes, breakable, question):
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

    # Moves Mario down
    def move_down(self):
        self.y += 1

    # To make Mario jump
    def jump(self):
        self.y -= self.vy

    # Takes care of the animation of Mario while moving
    def animation(self):
        self.skincount += 1
        if self.skincount == 5:
            self.u = 0
            self.v = self.m
        elif self.skincount == 10:
            self.u = 16
            self.v = self.m
        elif self.skincount == 15:
            self.u = 32
            self.v = self.m
            self.skincount = 0

    # Takes care of the animation of Mario while moving up
    def animationup(self):
        self.u = 48
        self.v = self.m

    # Takes care of the animation of Mario while moving down
    def animationdown(self):
        self.u = 64
        self.v = self.m

    # Takes care of the animation of Mario when stopped
    def animationnormal(self):
        self.u = 0
        self.v = self.m

    # Takes care of the skin of  Luigi
    def changeskinluigi(self):
        self.m = 152
        self.itsluigi = True

    # Takes care of the skin of  Mario
    def changeskinmario(self):
        self.m = 168
        self.itsluigi = False

    # Takes care of the skin of big player for Luigi
    def changembig(self):
        if self.big:
            if self.itsluigi:
                self.m = 184
            else:
                self.m = 200
        else:
            if self.itsluigi:
                self.m = 152
            else:
                self.m = 168

    # To end the game at the end of the map
    def finishmario(self, castlex):
        if self.x >= castlex + 16:
            pyxel.quit()

    # Checks collision with the plant
    def collisioncarn(self, xcarn, ycarn):
        if xcarn + 14 >= self.x >= xcarn - 14:
            if ycarn + 14 >= self.y >= ycarn - 14:
                return True
