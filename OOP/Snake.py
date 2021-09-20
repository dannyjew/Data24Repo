from Reptile import *

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.venom = None
        self.suprise_attack()


    def suprise_attack(self):
        print("Gotcha!!!!!")

sally = Snake()
Steve = Snake()
