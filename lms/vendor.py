#imports

from library import Library as librr
# Vendor class
class Vendor:
    """ this is the Vendors class """
    def __init__(self):
        """ this are the attributes of the Vendor class """
        self. book_names = ["The Great Gatsby", "Beloved", "Invisible Man", "On The road", "On the road", "Bigger" ] #placeholders
        self.book_price = 0
        self.book_type = ""
    
    def search(self):
        """ This searches for books """
        self.book_name = input("Enter a book you want to search: ")
        if self.book_name in self.book_names:
            print("{} is available".format(self.book_name))
        else:
            print("{} is not available".format(self.book_name))
            print("This are the available books: ")
            for self.books in self.book_names:
                print("-> {}".format(self.books))

    def supply_book(self):
        """ This shows the books that need to be supplied as requested by patron"""
        pass

    def payment_details(self):
        """ this shows the payment details where the funds will go """
        pass
    

