# single inheritance

# first class
class Apple:
    def __init__(self):
        self.manufacturer = 'Apple Inc.'
        self.contactWebsite = 'www.apple.com/contact'

    def contactDetails(self):
        print('contact us via', self.contactWebsite)


# second class
class Macbook(Apple):
    def __init__(self) -> None:
        super().__init__()
        self.yearOfManufacture = 2017

    def manufacturedetails(self):
        print(f'This macbook was manufactured in the year {
              self.yearOfManufacture} by {self.manufacturer}')


macbook = Macbook()
macbook.manufacturer
macbook.contactDetails()
macbook.manufacturedetails()
