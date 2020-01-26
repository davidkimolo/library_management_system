#imports
import json
from library import Library as librr
import collections

vendor_file = "files/vendor.json"
vendor_payment_details = "files/vendor_payment_details.json"
requested_books = "files/requested_books.json"
librarian_data = "files/librarian.json"
issue = "files/issues.json"
vendor_books = "files/vendor_books.json"
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
        # load librarylocation and librarian ID
        with open (librarian_data) as all_library_data:
            library_data = json.load(all_library_data)
        
        if len(library_data) == 2:
            self.library_location = library_data[0]
            self.librarian_id = library_data[1]
            self.supply_to = librr(self.library_location, self.librarian_id)
            print(f"You have loaded the library in '{self.library_location}' and you are dealing with librarian of ID '{self.librarian_id}'' ")
            # to do check more conditions
            # load and display the books we have to supply (requested books)

            with open (requested_books) as check_requested:
                load_requested = json.load(check_requested)
            count = collections.Counter()

            for requested_book in load_requested:
                count[requested_book] +=1
            print ("This are the requested books: ")
            for book_name in count.items():
                print(f"-> {book_name}")
            print("This are the books available:")
            with open(vendor_books) as available_vendor_books:
                the_available_vendor_books = json.load(available_vendor_books)
            book_counter = collections.Counter()

            for checking_available_books in the_available_vendor_books:
                book_counter[checking_available_books] += 1
            for vendor_available_book in book_counter.items():
                print(f"-> {vendor_available_book}")
        else:
            # sending missing librarian issue to super user 
            no_librarian_issue = ["Librarian does not exist. Please create one."]
            missing_librarian_checker = no_librarian_issue[0]
            with open(issue) as submit_issue:
                load_issue_file = json.load(submit_issue)
            #checking if the issue already exists
            if missing_librarian_checker in load_issue_file:
                
                print("Librarian does not exist. The issue was already submitted!")
            else:
                # writting the issue to file
                print("Librarian does not exist. Sending issue to Super User...")
                with open(issue, "w") as submiting_issue:
                    no_librarian_issue += load_issue_file
                    json.dump(no_librarian_issue, submiting_issue)

    def payment_details(self):
        """ this shows the payment details where the funds will go """
        # load the payment file
        with open(vendor_payment_details) as vendor_pay_details:
            all_pay_details = json.load(vendor_pay_details)
        if len(all_pay_details) < 3:
            all_vendor_payment_details = []
            self.bank_name = input("Enter bank name: ")
            all_vendor_payment_details.append(self.bank_name)
            try:
                self.account_number = int(input("Enter account number: "))
            except ValueError:
                print("Please enter a numerical input!")
            else:
                all_vendor_payment_details.append(self.account_number)
                self.branch_location = input("Enter branch location: ")
                all_vendor_payment_details.append(self.branch_location)

            # saving the payment details to vendor payment file
            with open(vendor_payment_details, "w") as add_payment_details:
                json.dump(all_vendor_payment_details, add_payment_details)
        else:
            update_choice = input("vendor details already exists do you want to update it? 'y' | 'n': ")
            update_choice = update_choice.lower()
            if update_choice == "y":
                all_vendor_payment_details = []
                self.bank_name = input("Enter bank name: ")
                all_vendor_payment_details.append(self.bank_name)
                try:
                    self.account_number = int(input("Enter account number: "))
                except ValueError:
                    print("Please enter a numerical input!")
                else:
                    all_vendor_payment_details.append(self.account_number)
                    self.branch_location = input("Enter branch location: ")
                    all_vendor_payment_details.append(self.branch_location)

                # saving the payment details to vendor payment file
                with open(vendor_payment_details, "w") as add_payment_details:
                    json.dump(all_vendor_payment_details, add_payment_details)
            elif update_choice == "n":
                print("Cancelling update...")
            else:
                print("Invalid choice!")
    def add_books(self):
        """ this adds books in the vendor inventory"""
        number_of_books = int(input("Enter the number of books you want to add: "))
        book_adder = 0
        added_books = []
        while (book_adder < number_of_books):
            add_book = input("Enter book name: ")
            added_books.append(add_book)
            book_adder += 1
        #loading the vendor books file
        with open(vendor_books) as the_vendor_books:
            all_vendor_books = json.load(the_vendor_books)

        # adding books to vendor books file
        with open (vendor_books, "w") as add_books:
            added_books += all_vendor_books
            json.dump(added_books, add_books)
            

        # print("Payment will be made to")
        # print(f"Account number:\t {self.account_number}")
        # print(f"Bank name:\t {self.bank_name}")
        # print(f"Bank branch:\t {self.branch_location}")
    

