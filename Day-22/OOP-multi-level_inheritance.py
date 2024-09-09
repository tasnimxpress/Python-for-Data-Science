# multilevel inheritance
# grandparents < parents < children

'''
1. Animal (Base Class)
2. Mammal (Intermediate Class, Derived from Animal)
3. Human (Derived Class, Derived from Mammal)
'''


class Animal:
    def __init__(self):
        self.BreathingElement = 'Oxygen'
        self.Movement = True

    def breath(self):
        print(f'All animals breath in {self.BreathingElement}')


class Mammals(Animal):
    def __init__(self):
        super().__init__()
        self.blood = 'Warm-blooded'
        self.breathingOrgan = 'mouths or noses'
        self.bodyhas = 'hair or fur'
        self.hearttype = 'Four-chambered heart'

    def nurse_young(self):
        print('We care our children.')

    def breathingSystem(self):
        print(f'We breath in {self.BreathingElement} using our {
              self.breathingOrgan}')


class Human(Mammals):
    def __init__(self):
        super().__init__()
        self.movingOrgan = 'Leg'
        self.num_leg = 2
        self.num_eye = 2
        self.breathingOrgan = 'nose'

    def speak(self):
        print('We speak')

    def characteristics(self):
        print(f"We move using our {self.movingOrgan},\nWe have {self.num_leg} {self.movingOrgan},\nwe breath in {
              self.BreathingElement} using our {self.breathingOrgan},\nWe have {self.hearttype}")


animal = Animal()
animal.breath()

mammal = Mammals()
mammal.nurse_young()
mammal.breathingSystem()


human = Human()
human.characteristics()
