# imports
import json
from library import Librarian as libr

available_librarian = "files/librarian.json"
patron_files = "files/patron.json"
requested_books = "files/requested_books.json"
librarian_files = "files/librarian.json"


# Patron class
class Patron:
    """ this is the Patron class """
    def __init__(self, name, email, patron_id):
        """ this are the patron class attributes """
        self.name = name
        self.email = email
        self.patron_id = patron_id

    def search(self):
        """ this will enable the patron search a book """
        print("What do you want to do?: ")
        print(f"You are logged in as '{self.name}' email: '{self.email}' ID: '{self.patron_id}'")
        self.patron_search = input(" press 's' to search for a book:  \n press 'n' to see how many book are there: ")
        self.patron_search = self.patron_search.lower()
        if self.patron_search == "s":
            with open (available_librarian) as the_availabale_librarian:
                the_librarian_details = json.load(the_availabale_librarian)
            if len(the_librarian_details) == 2:
                the_librarian_location = the_librarian_details[0]
                the_librarian_id = the_librarian_details[1]
                print(f"You are quering data from '{the_librarian_location}' of ID '{the_librarian_id}'.")

                self.librarian_location = the_librarian_location
                self.librarian_id = the_librarian_id

                self.patron_book = input("Enter the title of the book you want to search: ")
                self.patron_book_result = libr(self.librarian_location, self.librarian_id)
                self.patron_book_result.search_book(self.patron_book)
                self.patron_book_result
            else:
                print("Librarian missing, cannot continue!")

        elif self.patron_search == "n":
            # see how many books are there
            self.librarian_location = input("Enter librarian location: ")
            try:
                self.librarian_id = int(input("Enter librarian ID: "))
            except ValueError:
                print("Error! enter a numerical input")
            else:
                self.available_books = libr(self.librarian_location, self.librarian_id)
                print("This are the available books. total is ({})".format(len(self.available_books.availabale_books)))
                for available_book in self.available_books.availabale_books:
                    print(f"-> {available_book}")
        else:
            print("Please enter either 's' or 'n'")
        
    def request(self):
        """ this enables the patron to see book requests """
        with open (requested_books) as requested:
            all_requested = json.load(requested)
        try:
            self.book_number = int(input("Enter the number of books you want to request: "))
        except ValueError:
            print("Error! Please enter a numerical input.")
        else:
            book_count = 0
            all_requested_books = []
            while (book_count < self.book_number):
                self.book_request = input("Enter the book name you want to request: ")
                all_requested_books.append(self.book_request)
                # adding books to requested books
                with open (requested_books,"w") as add_books:
                    all_requested_books += all_requested
                    json.dump(all_requested_books, add_books)
                book_count += 1
                print("The book has been requested.")

            # loading the librarian data
            with open (librarian_files) as load_librarian:
                get_librarian = json.load(load_librarian)

            self.librarian_location = get_librarian[0]
            self.librarian_id = get_librarian[1]
            
            self.librarian_instance = libr(self.librarian_location, self.librarian_id)
            self.librarian_instance.requested_book.append(self.book_request)
            print(f"Your request for  {self.book_request} has been sent.")
    

    def pay_fine(self):
        """ this will make the patron be able to pay fines """
        self.librarian_location = input("Enter Librarian location: ")
        self.librarian_id = input("Enter librarian id: ")
        self.pay_owned_fine = libr(self.librarian_location, self.librarian_id)
        
        self.payment_answer = input(f" Are you sure you want to pay {self.pay_owned_fine.total_payments} ? 'y' | 'n' ")
        self.payment_answer = self.payment_answer.lower()
        
        if self.payment_answer == "y":
            self.payment_amount = int(input("Enter the amount you want to pay: "))
            if self.payment_amount <= self.pay_owned_fine.total_payments:
                self.balance = self.pay_owned_fine.total_payments - self.payment_amount
                print("Thank you for paying! Your balance is: {}".format(self.balance))
            if self.payment_amount > self.pay_owned_fine.total_payments:
                print(f"The amount you are paying can not be above: {self.pay_owned_fine.total_payments}") 
        else:
            print("Please pay your fines ")
 
# Patron_record child class 
class Patron_record(Patron):
    """ this is a child class of the parent Patron """
    def __init__(self, name, email, patron_id):
        super().__init__(name, email, patron_id)
        """ this are the attributes of the child class Pareon_record """
        self.patron_id = patron_id
        self.name  = name
        self.email = email
        self.book_type = ""
        self.date_of_membership = ""
        self.number_of_books_issued = 12
        self.maximum_number_limit = 100
        # To-do This should be entered by the necessary person
        self.phone_number = ["12345", "23456","34567"]
        self.phone_number_length = len(self.phone_number[0])
        self.fines_owed = ""

    def retrive_member(self, number):
        # Check the length of the phone number
        converted_number = (str(number))
        if len(converted_number) != 5:
            print("The phone number cannot be less or more than {}".format(self.phone_number_length))
        else:
            if number in self.phone_number:
                # To-do print the user real identity instead of just "user"
                print("User in the database") 
            else:
                print("User is not available")

    def increse_book_issued(self):
        self.add_more_books = int(input("How many more books do you want to add: "))
        if self.number_of_books_issued + self.add_more_books < self.maximum_number_limit:
            self.number_of_books_issued += self.add_more_books
            print("You now have {} books".format(self.number_of_books_issued))
        elif self.number_of_books_issued + self.add_more_books > self.maximum_number_limit:
            print("You can not add more than {} books. Total number of books so far is {}".format(self.maximum_number_limit, self.number_of_books_issued))
        else:
            print("Please enter a valid number")
    
    def decrease_books_issued(self):
        self.remove_books = int(input("How many books do you want to remove: "))
        if self.remove_books <= self.number_of_books_issued and self.remove_books != 0:
            self.remaining_books = self.number_of_books_issued - self.remove_books
            print("You have removed {} books. Remaining books are {}".format(self.remove_books, self.remaining_books))
        else:
            print(f"Please enter a number that is not 0 or above the current number of books which is {self.number_of_books_issued}")





