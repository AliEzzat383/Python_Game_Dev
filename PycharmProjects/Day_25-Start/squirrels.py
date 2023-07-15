COLOR_LIST = ["gray", "cinnamon", "black"]


class Squirrel:
    def __init__(self):
        self.list = []
        self.create_list()

    def create_list(self):
        """appends empty squirrel list with three main color objects"""
        for color in COLOR_LIST:
            self.list.append(Color(color))


class Color:
    def __init__(self, name=""):
        self.name = name
        self.count = 0

    def compare(self, input_str):
        """Compares name to input string"""
        input_str = str(input_str).lower()
        if self.name == input_str:
            self.increment()
        else:
            pass

    def increment(self):
        """ increments count"""
        self.count += 1

