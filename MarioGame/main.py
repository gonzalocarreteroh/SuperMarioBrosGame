# Libraries
import pyxel
import random

# We import all the classes that we need to use in our main class, from their respective files
from mario import Mario
from goomba import Goombas
from koopatroopa import KoopaTroopas
from blocks import Blocks
from breakable_blocks import BreakableBlocks
from pipes import Pipes
from question_blocks import QuestionBlocks
from heading import Head
from coins import Coins
from mushroom import Mushroom
from carnivorous import Carnivorous
from castle import Castle
from constant import Constant


# This is the main class which will run the game
class App:
    def __init__(self):
        # Size of the screen
        pyxel.init(256, 256)
        # Load our resources from pyxel editor into the program
        pyxel.load("Resources/marioassets.pyxres")
        # The x of the background, that starts at 0
        self.xboard = 0
        # Object with all the constants that are repeated throughout the code
        self.constant1 = Constant()
        # Object for Mario, starts at x = 0 and y = in the floor
        self.mario1 = Mario(0, self.constant1.floor, 0, 168, False, 1, False)
        # List that includes all the objects of blocks that will form the first line of the floor
        self.floor1 = []
        # List that includes all the objects of blocks that will form the second line of the floor
        self.floor2 = []
        # The first block from fist line of floor is appended
        self.floor1.append(Blocks(0, 232))
        # 150 blocks of floor are created, 16 pixels from eachother (their width)
        for i in range(150):
            self.floor1.append(Blocks(self.floor1[-1].x + self.constant1.size16, self.floor1[-1].y))
        # The first block from second line of floor is appended
        self.floor2.append(Blocks(0, 248))
        # 150 blocks of floor are created, 16 pixels from eachother (their width)
        for i in range(150):
            self.floor2.append(Blocks(self.floor2[-1].x + self.constant1.size16, self.floor2[-1].y))
        # List with the x positions of the pipes
        self.list_pipes_x = [100, 200, 400, 600, 750]
        # List that will include all the pipe objects
        self.pipes = []
        # As many pipes as x coordinates in list_pipes_x are created, y = 200
        for i in range(len(self.list_pipes_x)):
            self.pipes.append(Pipes(self.list_pipes_x[i], 200))
        # Sames process as with pipes but with the breakable blocks
        self.list_breakable_x = [262, 308, 336, 352, 440, 456, 472, 488, 504, 520, 536, 552, 640, 656, 672, 688, 704, 656, 672, 688]
        # Another list for the y coordinates in case we want to change them
        self.list_breakable_y = [155, 155, 155, 155, 155, 155, 155, 155, 155, 155, 155, 155, 155, 155, 155, 155, 155, 78, 78, 78]
        self.breakable = []
        for i in range(len(self.list_breakable_x)):
            # False corresponds to indicate those blocks don't have more than one coin in them
            self.breakable.append(BreakableBlocks(self.list_breakable_x[i], self.list_breakable_y[i], 1, False))
        # Breakable block with 3 coins
        self.breakable[2].has_coins = 3
        self.breakable[2].multicoins = True
        # Same process as with pipes but to create coins in the air
        self.free_coins = []
        self.free_coins_x = [450, 475, 500, 525]
        for elem in self.free_coins_x:
            # True meaning they should be displayed, since they are out of a block
            self.free_coins.append(Coins(elem, 120, True))
        # Same process as pipes but with question blocks. We decided to create just one, but more can be added
        self.list_question_x = [280]
        self.question = []
        for i in range(len(self.list_question_x)):
            self.question.append(QuestionBlocks(self.list_question_x[i], 155))
        # The x coordinates of enemies depend on the pipes ones, but they appear in a random position between two of
        # them
        self.list_enemies_x = []
        # One less enemy than pipes
        for i in range(len(self.list_pipes_x) - 1):
            num = random.randint(20, 40)
            self.list_enemies_x.append(self.list_pipes_x[i] + num)
        self.enemies = []
        for i in range(len(self.list_enemies_x)):
            # Generates randomly the koopas (25% chance) and goombas (75% chance)
            num = random.randint(0, 3)
            if num == 0:
                # The two indicates their initial direction of movement
                self.enemies.append(KoopaTroopas(self.list_enemies_x[i] + 28, 209, 2))
            if num > 0:
                # The two indicates their initial direction of movement
                self.enemies.append(Goombas(self.list_enemies_x[i] + 28, 216, 2))
        # Makes jump more natural later on
        self.counter_tojump = 6
        # Object with all the heading information
        self.heading1 = Head()
        # The first coin is generated in a non visible spot, the object will change later
        self.coins = Coins(0, 300, False)
        # To make coins disappear after a short period of time, used later
        self.coin_counter = 0
        # The first mushroom is generated in a non visible spot, the object will change later
        self.mushroom = Mushroom(0, 139, False, 1)
        # Will help with animations later
        self.m = 0
        # Object for the castle at the end of the game
        self.castle1 = Castle(875, 168)
        # Extra enemy, a plant that appears in the first pipe
        self.carn1 = Carnivorous(self.pipes[0].x + 8, self.pipes[0].y - 8, 0)
        # Very important, runs the game
        pyxel.run(self.update, self.draw)

    def update(self):
        # Every question block has a mushroom inside that doesn't appear at the beginning
        if not self.mushroom.alive:
            for elem in self.question:
                self.mushroom.x = elem.x
        # If player presses the key L before moving, Luigi is selected instead of Mario
        if pyxel.btnp(pyxel.KEY_L) and self.xboard == 0 and self.mario1.x == 0:
            self.mario1.changeskinluigi()
        # If key M is pressed, it changes to Mario, that comes by default
        elif pyxel.btnp(pyxel.KEY_M) and self.xboard == 0 and self.mario1.x == 0:
            self.mario1.changeskinmario()
        # If Mario or Luigi are big, it changes the u and v of the pyxel editor
        self.mario1.changembig()
        # Does the moving animation of the player
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_RIGHT):
            self.mario1.animation()
        # Does the jumping animation of the player
        elif pyxel.btn(pyxel.KEY_UP):
            self.mario1.animationup()
        # Does the animation of the player going down faster
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.mario1.animationdown()
        # Goes to a normal sprite of player in case it is not moving
        elif not pyxel.btn(pyxel.KEY_DOWN) and not pyxel.btn(pyxel.KEY_UP) and not pyxel.btn(pyxel.KEY_LEFT) and \
                not pyxel.btn(pyxel.KEY_RIGHT):
            self.mario1.animationnormal()
        # Moves Mario to the left under some conditions
        if pyxel.btn(pyxel.KEY_LEFT): #or pyxel.btn(pyxel.GAMEPAD_1_LEFT):
            # Only if it doesn't try to go out of the screen from the left
            if self.mario1.x > 0:
                # Only if it is not having a collision on the left
                if not self.mario1.left_collision(self.pipes, self.breakable, self.question):
                    self.mario1.move_left()
        # Moves Mario to the right under some conditions
        if pyxel.btn(pyxel.KEY_RIGHT): #or pyxel.btn(pyxel.GAMEPAD_1_RIGHT):
            # Only if it is not having a collision on the right
            if not self.mario1.right_collision(self.pipes, self.breakable, self.question):
                self.mario1.move_right()
            # If Mario reaches the half of the screen
            if self.mario1.x >= self.constant1.half_screen:
                # It doesn't go further to the right
                self.mario1.x = self.constant1.half_screen
                # If Mario is not having a collision while in the middle of the screen
                if not self.mario1.moving_collision(self.pipes, self.breakable, self.question):
                    # The screen moves to the left
                    self.xboard = min(self.xboard + 0.3, pyxel.width - 16)
                    # When the screen is moving, all the objects also move to the left
                    for i in range(len(self.floor1)):
                        self.floor1[i].move()
                    for j in range(len(self.floor2)):
                        self.floor2[j].move()
                    for elem in self.pipes:
                        elem.move()
                    for elem in self.enemies:
                        elem.x -= 1
                    for elem in self.breakable:
                        elem.move()
                    for elem in self.question:
                        elem.move()
                    self.coins.move()
                    if self.mushroom.alive:
                        self.mushroom.x -= 1
                    self.castle1.move()
                    self.carn1.move()
                    for elem in self.free_coins:
                        elem.move()
        # Recharges the ability to jump
        if self.mario1.in_floor:
            self.counter_tojump = 6
        if pyxel.btn(pyxel.KEY_UP):
            # If this counter is modified by any of the collisions bellow it will not jump
            counter = 0
            self.counter_tojump -= 1
            # Collisions checked for breakable blocks
            for i in range(len(self.breakable)):
                if self.mario1.x + self.constant1.size12 > self.breakable[i].x and \
                        self.mario1.x < self.breakable[i].x + self.constant1.size16\
                        and (self.breakable[i].y + self.constant1.size16 >= self.mario1.y and
                             self.mario1.y + self.constant1.size12 > self.breakable[i].y):
                    counter += 1
            # Collisions checked for question blocks
            for i in range(len(self.question)):
                if self.mario1.x + self.constant1.size12 > self.question[i].x and \
                        self.mario1.x < self.question[i].x + self.constant1.size16\
                        and (self.question[i].y + self.constant1.size16 >= self.mario1.y and
                             self.mario1.y + self.constant1.size12 > self.question[i].y):
                    counter += 1
            # If not collisioning and there is still jump power, Mario jumps
            if counter == 0 and self.counter_tojump > 0:
                self.mario1.jump()
        # Mario goes down faster under one condition
        if pyxel.btn(pyxel.KEY_DOWN):
            # Mario is above the floor
            if self.mario1.y < self.constant1.floor:
                self.mario1.move_down()
            if self.mario1.y == self.constant1.floor:
                self.mario1.in_floor = True
        # If Mario above the floor, it checks for collisions to see if it should apply the gravity or not
        if self.mario1.y < self.constant1.floor:
            counter = 0
            # Collisions checked for pipes
            for i in range(len(self.pipes)):
                if self.mario1.x + self.constant1.size12 > self.pipes[i].x and self.mario1.x < self.pipes[i].x + 30\
                        and self.mario1.y >= self.pipes[i].y - self.constant1.size16:
                    counter += 1
                    # Considers that Mario is touching something bellow
                    self.mario1.in_floor = True
            # Collisions checked for breakable blocks
            for j in range(len(self.breakable)):
                if self.mario1.x + self.constant1.size12 > self.breakable[j].x and \
                        self.mario1.x < self.breakable[j].x + self.constant1.size16\
                        and (self.breakable[j].y + 15 > self.mario1.y >= self.breakable[j].y - self.constant1.size16):
                    counter += 1
                    self.mario1.in_floor = True
            # Collisions checked for question blocks
            for j in range(len(self.question)):
                if self.mario1.x + self.constant1.size12 > self.question[j].x and \
                        self.mario1.x < self.question[j].x + self.constant1.size16\
                        and (self.question[j].y + 15 > self.mario1.y >= self.question[j].y - self.constant1.size16):
                    counter += 1
                    self.mario1.in_floor = True
            # If no collision gravity is applied
            if counter == 0:
                self.mario1.gravity()
                self.mario1.in_floor = False
            if self.mario1.y == self.constant1.floor:
                self.mario1.in_floor = True
        # Checks the position of the enemies
        for j in range(len(self.enemies)):
            # If an enemy hits the left of a pipe
            if self.enemies[j].x == self.pipes[j + 1].x - self.constant1.size12:
                # It changes the direction of movement to the left
                self.enemies[j].direction = 2
                # The sprite is turned, only visible for koopas since they are not symmetric
                self.enemies[j].w *= -1
            # If an enemy hits the right of a pipe
            if self.enemies[j].x == self.pipes[j].x + 30:
                # It changes the direction of movement to the right
                self.enemies[j].direction = 1
                # The sprite is turned, only visible for koopas since they are not symmetric
                self.enemies[j].w *= -1
        # Collisions of Mario with enemies
        for i in range(len(self.enemies)):
            # If Mario hits the left of an enemy
            if self.mario1.x + self.constant1.size12 == self.enemies[i].x and (self.mario1.y > self.enemies[i].y - 2):
                # If Mario is big it becomes small
                if self.mario1.big:
                    self.mario1.big = False
                # If Mario is was small already,
                else:
                    # A life is taken out of the heading
                    self.heading1.lives -= 1
                    # Mario moves to the start of the screen
                    self.mario1.x = 0
                    # The background goes to the starting x too
                    self.xboard = 0
            # If Mario hits the right of an enemy, same process as before
            elif self.mario1.x == self.enemies[i].x + self.constant1.size12 and (self.mario1.y > self.enemies[i].y - 2):
                if self.mario1.big:
                    self.mario1.big = False
                else:
                    # A life is taken out of the heading
                    self.heading1.lives -= 1
                    # Mario moves to the start of the screen
                    self.mario1.x = 0
                    # The background goes to the starting x too
                    self.xboard = 0
            # If Mario hits the top of an enemy
            elif self.mario1.x + self.constant1.size12 > self.enemies[i].x and \
                    self.mario1.x < self.enemies[i].x + self.constant1.size16 \
                    and (self.enemies[i].y >= self.mario1.y + self.constant1.size12 >= self.enemies[i].y - 2):
                # Enemy stops being alive
                self.enemies[i].alive = False
                # 100 points added to the heading
                self.heading1.points += 100
            # Instead of the last lines of code, we tried to restart the game without success
            """
            if self.mario1.x + 12 == self.enemies[i].x and (self.mario1.y > self.enemies[i].y - 2):
                self.heading1.lives -= 1
                # self.heading1.reset(self.mario1.x, self.mario1.y, self.xboard)
            if self.mario1.x == self.enemies[i].x + 12 and (self.mario1.y > self.enemies[i].y - 2):
                self.heading1.lives -= 1
                # self.heading1.reset(self.mario1.x, self.mario1.y, self.xboard)
            if self.mario1.x + 12 > self.enemies[i].x and self.mario1.x < self.enemies[i].x + 16 \
                    and (self.enemies[i].y >= self.mario1.y + 12 >= self.enemies[i].y - 2):
                self.enemies[i].alive = False
                self.heading1.points += 100
            """
        # Enemies move constantly under one condition
        for elem in self.enemies:
            # That they are alive
            if elem.alive:
                elem.move()
            # If not they disappear
            else:
                elem.disappear()
        # Collisions of Mario with the breakable blocks, that are special
        for elem in self.breakable:
            # If Mario hits a breakable block from underneath
            if self.mario1.x + self.constant1.size12 > elem.x and self.mario1.x < elem.x + self.constant1.size16\
                        and (elem.y + self.constant1.size16 >= self.mario1.y and
                             self.mario1.y + self.constant1.size12 > elem.y):
                # If Mario is small
                if not self.mario1.big:
                    # If the breakable block has coins
                    if elem.has_coins > 0:
                        # The object of coins takes it's x and y depending on the one of the block and True means they
                        # should appear
                        self.coins = Coins(elem.x, elem.y - self.constant1.size16, True)
                        # The block has one less coin
                        elem.has_coins -= 1
                # If Mario is big
                if self.mario1.big:
                    # Same as before
                    if elem.has_coins > 0:
                        self.coins = Coins(elem.x, elem.y - self.constant1.size16, True)
                        elem.has_coins -= 1
                    # If the block has no more coins and it wasn't a block with multiple coins, Mario breaks it
                    if elem.has_coins == 0 and not elem.multicoins:
                        elem.x = 1000
                        elem.u = 0
                        elem.v = 0
                    # If the block has no more coins and it was a block with multiple coins
                    # the sprite of the block changes to an empty block
                    if elem.has_coins == 0 and elem.multicoins:
                        elem.u = 16
                        elem.v = 16
        # If a coin has appeared
        if self.coins.appear:
            # When this counter reaches 20, the heading increases one coin and the coin disappears
            self.coin_counter += 1
            if self.coin_counter >= 20:
                self.heading1.coin += 1
                self.coins.disappear()
                self.coins.appear = False

        if not self.coins.appear:
            self.coin_counter = 0
        # If Mario hits a question block from underneath
        for elem in self.question:
            if self.mario1.x + self.constant1.size12 > elem.x and self.mario1.x < elem.x + self.constant1.size16 \
                    and (elem.y + self.constant1.size16 >= self.mario1.y
                         and self.mario1.y + self.constant1.size12 > elem.y):
                # A mushroom appears
                self.mushroom.alive = True
                elem.u = 16
                elem.v = 16
        # If there is a mushroom on the screen
        if self.mushroom.alive:
            # Has gravity until it reaches the floor
            if self.mushroom.y < self.constant1.floor:
                self.mushroom.gravity()
            # It moves constantly
            self.mushroom.move()
            # If the mushroom has a collision with an object it changes direction of movement
            if self.mushroom.right_collision(self.pipes, self.breakable, self.question):
                self.mushroom.direction = 2
            if self.mushroom.left_collision(self.pipes, self.breakable, self.question):
                self.mushroom.direction = 1
            # Checks if Mario hits the left of the mushroom
            if self.mario1.x == self.mushroom.x + self.constant1.size16 and \
                    self.mushroom.y + self.constant1.size16 > self.mario1.y >= self.mushroom.y - self.constant1.size16:
                # If it does, Mario becomes big
                self.mario1.big = True
                # The mushroom disappears
                self.mushroom.disappear()
            # Right collision with mushroom same as before
            if self.mario1.x + self.constant1.size12 == self.mushroom.x and (
                        self.mushroom.y + self.constant1.size16 > self.mario1.y > self.mushroom.y - self.constant1.size16):
                self.mario1.big = True
                self.mushroom.disappear()
            # Checks if Mario hits the mushroom either up or down
            if self.mario1.x + self.constant1.size12 > self.mushroom.x and \
                    self.mario1.x < self.mushroom.x + self.constant1.size16 \
                    and (self.mushroom.y + 15 > self.mario1.y >= self.mushroom.y - self.constant1.size16):
                self.mario1.big = True
                self.mushroom.disappear()
        # Checks collisions of Mario with the coins in the air
        for elem in self.free_coins:
            counter = 0
            if self.mario1.x == elem.x + self.constant1.size16 and elem.y + self.constant1.size16 > self.mario1.y >= elem.y - self.constant1.size16:
                counter += 1
            if self.mario1.x + self.constant1.size12 == elem.x and (
                    elem.y + self.constant1.size16 > self.mario1.y > elem.y - self.constant1.size16):
                counter += 1
            if self.mario1.x + self.constant1.size12 > elem.x and self.mario1.x < elem.x + self.constant1.size16 \
                    and (elem.y + 15 > self.mario1.y >= elem.y - self.constant1.size16):
                counter += 1
            # If collision
            if counter != 0:
                # Coin disappears
                elem.disappear()
                # Coins in heading plus one
                self.heading1.coin += 1
        # Constant move of the plant in its pipe
        self.carn1.constantmove(self.pipes)
        # If Mario reaches the castle, the game quits
        self.mario1.finishmario(self.castle1.x)
        # Checks collisions of MArio with the plant
        if self.mario1.collisioncarn(self.carn1.x, self.carn1.y):
            # Mario goes back to the beginning of the screen
            self.mario1.x = 0
            self.mario1.y = 215
            # The board too
            self.xboard = 0
            # One less life
            self.heading1.lives -= 1
        # If no lives left, game quits
        if self.heading1.lives == 0:
            pyxel.quit()

    def draw(self):
        # Draws the background
        pyxel.bltm(0, 0, 0, self.xboard, 65, 50, 50)
        # Draws the castle
        self.castle1.draw()
        # Draws Mario
        self.mario1.draw()
        # Draws the first line of floor
        for i in self.floor1:
            i.draw()
        # Draws the second line of floor
        for j in self.floor2:
            j.draw()
        # Draws the plant
        self.carn1.draw()
        # Draws all the different objects and enemies
        for elem in self.pipes:
            elem.draw()
        for elem in self.breakable:
            elem.draw()
        for elem in self.enemies:
            elem.draw()
        for elem in self.question:
            elem.draw()
        # Draws the coins
        self.coins.draw()
        # Draws the mushroom if alive
        if self.mushroom.alive:
            self.mushroom.draw()
        # Draws the coins in the air
        for elem in self.free_coins:
            elem.draw()
        # Draws the different parts of the heading
        self.heading1.livesmario()
        self.heading1.pointscounter()
        self.heading1.timecounter()
        self.heading1.coinscounter()


# Executes the class App
App()





