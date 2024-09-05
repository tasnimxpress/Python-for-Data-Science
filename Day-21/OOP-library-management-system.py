# class = Library
# layer of abstraction - available books, lend a book, add a book
class Library:
    # instances
    def __init__(self, BookList):
        self.listOfBooks = BookList

    # methods
    def displayBook(self):
        print()
        print("Available Books in our library!\n")
        for book in self.listOfBooks:
            print(book)

    def lendBook(self, requested_book):
        if requested_book in self.listOfBooks:
            print(f'You have borrowed {requested_book}\n')
            self.listOfBooks.remove(requested_book)
        else:
            print(f"{requested_book} not available at this moment.\n")

    def addBook(self, returned_book):
        self.listOfBooks.append(returned_book)
        print('You have returned the book. Thank you.\n')


# class = Customer
# layer of abstraction - view available book, borrow a book, return a book
class Customer:
    def borrowBook(self):
        print(f"Enter the name you want to borrow: ")
        self.book = input().capitalize()
        return self.book

    def returnBook(self):
        print(f"Enter the book name you are returning: ")
        self.book = input().capitalize()
        return self.book


# creating menu
library = Library(['Economics', 'The creative code',
                  'Rework', 'Seneka', 'Art of war'])
customer = Customer()


# encapsulation
while True:
    print("\nEnter 1 to display the available book: ")
    print("Enter 2 to borrow a book: ")
    print("Enter 3 to return a book: ")
    print("Enter 4 to exit: ")

    user_choice = int(input())

    if user_choice == 1:
        library.displayBook()
    elif user_choice == 2:
        requested_book = customer.borrowBook()
        library.lendBook(requested_book)
    elif user_choice == 3:
        returned_book = customer.returnBook()
        library.addBook(returned_book)
    elif user_choice == 4:
        library_open = False
        quit()
