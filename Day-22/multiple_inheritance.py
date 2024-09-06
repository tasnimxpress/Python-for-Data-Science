# multiple inheritance
# first 2 class will be the base class for 3rd class


class OperatingSystem:
    def __init__(self):
        self.multitasking = True
        self.name = 'Unix OS'


class Apple:
    def __init__(self):
        self.Website = 'www.apple.com'
        self.name = 'Mac OS'


class Macbook(OperatingSystem, Apple):
    def __init__(self):
        OperatingSystem.__init__(self)
        Apple.__init__(self)

        if self.multitasking is True:
            print(f'This is a multitasking system based on {self.name}. Visit {
                  self.Website} to know more.')


# if both class has same attribute name, 2nd class will overwrite the first class attribut in output
macbook = Macbook()
