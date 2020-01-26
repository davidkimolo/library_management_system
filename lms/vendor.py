#imports
import json
from library import Library as librr

vendor_file = "files/vendor.json"
vendor_payment_details = "files/vendor_payment_details.json"
requested_books = "files/requested_books.json"
librarian_data = "files/librarian.json"
issue = "files/issues.json"
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
            self.number_of_supply_books = int(input("How many books are you supplying: "))
            if self.number_of_supply_books <= len(self.book_names):
                print(f"{self.number_of_supply_books} have been send to {self.supply_to.location} location to the librarian with the ID {self.librarian_id}") 
            else:
                print(f"Please enter books that are not higher than {len(self.book_names)}")
        else:
            # sending missing librarian issue to super user 
            no_librarian_issue = ["Librarian does not exist. Please create one."]
            missing_librarian_checker = no_librarian_issue[0]
            with open(issue) as submit_issue:
                load_issue_file = json.load(submit_issue)
            #checking if the issue already exists
            if missing_librarian_checker in load_issue_file:
                print("The issue was already submitted!")
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
    
             
        # print("Payment will be made to")
        # print(f"Account number:\t {self.account_number}")
        # print(f"Bank name:\t {self.bank_name}")
        # print(f"Bank branch:\t {self.branch_location}")
    

