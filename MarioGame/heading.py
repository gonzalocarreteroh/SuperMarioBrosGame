import pyxel


# Class for the heading in the game
class Head:
    def __init__(self):
        self.frames = 1000
        self.points = 0
        self.lives = 3
        self.coin=0

    # This method control and show the lives that have MArio,he always start with 3 lives
    def livesmario(self):
        s = "Lives {:}".format(self.lives)
        return pyxel.text(50, 10, s, 7)

    # This methed control the time that remain and prepare it to show it in the screen
    def timecounter(self):
        if pyxel.frame_count % 15 == 0:
            self.frames -= 1
        if self.frames == 0:
            self.lives -= 1
            self.x = 0
            self.y = 216
            self.xboard = 0
            self.frames = 1000
        t = "Time{:}".format(self.frames)
        return pyxel.text(200, 10, t, 7)

    # This method control the points that have Mario And prepare to show it
    def pointscounter(self):
        p = "Points{:}".format(self.points)
        return pyxel.text(150, 10, p, 7)

    # This method control the coins that have Mario And prepare to show it
    def coinscounter(self):
        coin = "Coins:{:}".format(self.coin)
        return pyxel.text(100,10,coin,7)

    # This method makes that the world restart,right now,in the beta,it doesn´t work
    """
    def reset(self,x,y,xboard):
        self.x = x
        self.y = y
        self.xboard = xboard
        if self.frames == 0:
            self.lives -= 1
            self.frames = 100
            self.x = 0
            self.xboard = 0
            self.y = 0
        return self.x and self.y and self.xboard
    """
