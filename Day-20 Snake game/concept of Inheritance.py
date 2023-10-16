class Animal:

    def __init__(self):
        self.eyes = 2

    def breath(self):
        print('inhale, exhale')


class Fish(Animal):

    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print('under water')

class Whale(Fish):

    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print('have lungs')

class Human(Animal):

    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print('using nose')


nemo = Fish()
print(nemo.eyes)
nemo.breath()


human = Human()
human.breath()

timi = Whale()
timi.breath()
print(timi.eyes)
