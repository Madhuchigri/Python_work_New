# Write a program to simulate the library and customer to borrow the book and return the book.

class Library:

    def __init__(self, listofbooks):
        self.availablebooks = listofbooks

    def displayavailablebooks(self):
        print("Available Books :")
        for book in self.availablebooks:
            print(book)

    def lendBook(self, requestedBook):
        if requestedBook in self.availablebooks:
            print("The Book is Borrowed successfully")
            self.availablebooks.remove(requestedBook)
        else:
            print("Sorry !!! the Book is not available")

    def addBook(self, returnedbook):
        print("Book is now added to the library.. thanks for returning")
        self.availablebooks.append(returnedbook)


class Customer:

    def requestBook(self):
        print("Enter the book you want to Borrow:")
        self.requestedBook = input()
        print("thanks for requesting a Book")
        return self.requestedBook

    def returnBook(self):
        print()
        print("Enter the BOOK's name you would like to return:")
        self.returnedbook = input()
        return self.returnedbook


library = Library(['Think like a monk', 'success','Secret','Power'])
customer =Customer()

## Menu starts Here
while 1:
    print("Enter 1 to Display the Available BOOKs in the library")
    print("Enter 2 to request the BOOK from the library")
    print("Enter 3 to return the BOOK to  the library")
    print("Enter 4 to exit")
    print()
    userchoice = int(input())
    if userchoice == 1:
        library.displayavailablebooks()
    elif userchoice == 2:
        requestedbook = customer.requestBook()
        library.lendBook(requestedbook)
    elif userchoice == 3:
        returnedbook = customer.returnBook()
        library.addBook(returnedbook)
    elif userchoice == 4:
        print("Thanks for Visiting...Bye !!!")
        quit()