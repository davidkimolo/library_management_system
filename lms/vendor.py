#imports
import json
from library import Library as librr

vendor_file = "files/vendor.json"
# Vendor class
class Vendor():
    """ this is the Vendors class """
    def __init__(self, vendor_name, vendor_location, vendor_id):
        """ this are the attributes of the Vendor class """
        self. book_names = "files/available_books.json" 
        self.book_price = 0
        self.book_type = ""
        self.vendor_name = vendor_name
        self.vendor_location = vendor_location
        self.vendor_id = vendor_id

    def search(self):
        """ This searches for books """
        self.book_name = input("Enter a book you want to search: ")
        self.book_name = self.book_name.lower()
        sorted_books = []
        with open(self.book_names) as all_available_books:
            all_the_books = json.load(all_available_books)
            for a_book in all_the_books:
                a_book = a_book.lower()
                sorted_books.append(a_book)
            if self.book_name.lower() in sorted_books:
                print("{} is available".format(self.book_name))
            else:
                print("{} is not available!".format(self.book_name))
                print("This are the available books: ")
                for self.books in all_the_books:
                    self.books = self.books.lower()
                    print("-> {}".format(self.books))

    def supply_book(self):
        """ This shows the books that need to be supplied as requested by patron"""
        self.library_location = input("Enter the library location: ")
        try:
            self.librarian_id = int(input("Enter the librarian ID: "))
        except ValueError:
            print("ValueError! Please enter a numerical value for Librarian ID")
        else:
            self.supply_to = librr(self.library_location, self.librarian_id)
            # to do check more conditions
            self.number_of_supply_books = int(input("How many books are you supplying: "))
            if self.number_of_supply_books <= len(self.book_names):
                print(f"{self.number_of_supply_books} have been send to {self.supply_to.location} location to the librarian with the ID {self.librarian_id}") 
            else:
                print(f"Please enter books that are not higher than {len(self.book_names)}")

    def payment_details(self):
        """ this shows the payment details where the funds will go """
        self.bank_name = input("Enter bank name: ")
        self.account_number = int(input("Enter account number: "))
        self.branch_location = input("Enter branch location: ")

        print("Payment will be made to")
        print(f"Account number:\t {self.account_number}")
        print(f"Bank name:\t {self.bank_name}")
        print(f"Bank branch:\t {self.branch_location}")
    

