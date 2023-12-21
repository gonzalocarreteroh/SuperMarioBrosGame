# Class for the constants
class Constant:
    def __init__(self):
        # Defien the variables in the class
        self.floor = 216
        self.size16 = 16
        self.size12 = 12
        self.velocity = 1
        self.half_screen = 120

    # Make thee variable private and can not be changed
    @property
    def floor(self):
        return self.__floor

    @floor.setter
    def floor(self, value):
        self.__floor = value

    # Make the variable private and can not be changed

    @property
    def size16(self):
        return self.__size16

    @size16.setter
    def size16(self, value):
        self.__size16 = value

    # Make thee variable private and can not be changed

    @property
    def size12(self):
        return self.__size12

    @size12.setter
    def size12(self, value):
        self.__size12 = value

    # Make thee variable private and can not be changed

    @property
    def half_screen(self):
        return self.__half_screen

    @half_screen.setter
    def half_screen(self, value):
        self.__half_screen = value

