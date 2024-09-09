# Polymorphism
# overloading

class Square:
    def __init__(self, lengthOfSide):
        self.side = lengthOfSide

    def __add__(n1, n2):
        return ((n1.side * 4) + (n2.side * 4))


square1 = Square(5)
square2 = Square(10)


print(f'sum {square1 + square2}')
