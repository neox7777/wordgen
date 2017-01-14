import os


def doNothing(object=None):
    pass


class notObject(object):
    pass


class Menu(notObject):
    def __init__(self, title, update=doNothing):
        self.title = title
        self.options = []
        self.indicator = ">>>"
        self.explicit()
        self.update = update

    def __setattr__(self, name, value):
        if isinstance(value, Menu) and name != "__parent__":
            value.__parent__ = self
        super(notObject, self).__setattr__(name, value)

    def addOptions(self, options):
        self.options += options

    def show(self):
        print(self.title)
        print("")
        for (key, option) in enumerate(self.options):
            print(str(key + 1) + ". " + option[self.NAME])
        print("")
        print(self.indicator),

    def input(self):
        try:
            option = int(input()) - 1
            return self.validate(option)
        except ValueError:
            return self.open

    def open(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.show()
        opt = self.input()
        print("")
        opt[self.FUNCTION](opt[self.NAME])
        os.system('cls' if os.name == 'nt' else 'clear')

    def validate(self, option):
        if option > -1 and option < len(self.options):
            return self.options[option]
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            return self.open

    def implicit(self):
        self.NAME = 0
        self.FUNCTION = 1

    def explicit(self):
        self.NAME = "name"
        self.FUNCTION = "function"

    def clearOptions(self):
        self.options = []
