# Public => memberName
# protected => _memberName (single underscore)
# private => __memberName (double underscore) "not directly accessible outside the class"


class Car:
    def __init__(self):
        self.numberOfWheels = 4
        self._color = 'Black'
        self.__yearofManufacture = 1992  # internally saved as _Car__yearofManufacture


class BMW(Car):
    def __init__(self) -> None:
        super().__init__()
        print('Protected attribute color', self._color)


car = Car()
print('Public attribute number of wheels',
      car.numberOfWheels)

bmw = BMW()
print(f'color of BMW is protected attribute, {
      bmw._color}\nwheel of bmw is public attribute {bmw.numberOfWheels}, {car._Car__yearofManufacture}')
