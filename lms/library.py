# Parent Library class
import json 
import getpass

available_books  = "files/available_books.json"
the_issued_books = "files/issued_books.json"
super_login = "files/super_user.json"
librarian_files = "files/librarian.json"
class Library:
    """ This is the parent Library class """
    def __init__(self, location, librarian_id):
        """ this are the attributes of the Library class """
        self.location = location
        self.librarian_id = librarian_id
        

# Librarian child class
class Librarian(Library):
    """ This is a child class of the library class """
    def __init__(self, location, librarian_id):
        """ initializing attributes of the Library class """
        super().__init__(location, librarian_id)
        """ initializing attributes of the Librarian child class """
        self.name = ""
        self.librarian_id = ""
        self.verified_members = "files/verified_members.json"
        self.payments = [12.5, 34.9, 98, 31]
        self.requested_book = []
        self.total_payments  = sum(self.payments)
        self.issue_books = []
        self.issued_book = []
        self.issue_books += self.issued_book
        try:
            with open(available_books) as all_books:
                self.availabale_books  = json.load(all_books)
        except FileNotFoundError:
            print(f"The file '{available_books}' was not found")
        else:
            pass

    # Librarian Super user
    def super_user_login (self):
        """ This is will register / login a super user """
        with open(super_login) as sp_login:
            super_data = json.load(sp_login)

        if len(super_data) < 2 :
            # register super user
            print("There is no super user please register super user")
            set_super_username = input("Enter new super user username: ")
            set_super_password = getpass.getpass("Enter new super user password: ")
            set_super_password_again = getpass.getpass("Enter new super user password again: ")
            super_input = []
            number_of_characters = 6
            if len(set_super_username)  >= number_of_characters:
                if set_super_password == set_super_password_again and len(set_super_password) >= number_of_characters:
                    with open(super_login, "w") as sp_logged_in:
                        super_input.append(set_super_username)
                        super_input.append(set_super_password)
                        json.dump(super_input, sp_logged_in)
                else:
                    print("Password does not match or password is less than {} characters!".format(number_of_characters))
            else:
                print("The length of your username cannot be less than {}".format(number_of_characters))


        elif len(super_data) == 2:
            # logging in 
            super_username = input("Enter username: ")
            super_password = getpass.getpass("Enter password: ")
            if super_username ==  super_data[0] and super_password == super_data[1]:
                # Super User Menu
                print (" 1. Create a librarian \n 2. edit librarian details \n 3. delete librarian \n 4. Change password")
                super_user_choice = int(input("Enter what action you want to perform: "))
                if super_user_choice == 1:

                    # create a libaraian
                    print("Creating a new librarian")
                    librarian_data = []
                    with open(librarian_files) as lib_files:
                        all_lib_files = json.load(lib_files)
                    if len(all_lib_files) > 2 or len(all_lib_files) < 2:
                        #creates the librarian and stores the info
                        create_librarian_location = input("Enter Librarian location: ")
                        create_librarian_id = input ("Enter librarian id: ")
                        with open(librarian_files, "w")  as the_lib_files:
                            librarian_data.append(create_librarian_location)
                            librarian_data.append(create_librarian_id)
                            json.dump(librarian_data, the_lib_files)
                    elif len(all_lib_files) == 2:
                        print("Librarian already exists!")

                elif super_user_choice == 2:
                    # edit librarian details
                        librarian_data = []
                        create_librarian_location = input("Enter new librarian location: ")
                        create_librarian_id = input ("Enter new librarian id: ")
                        with open(librarian_files, "r+")  as the_lib_files:
                            #for all_data in the_lib_files:
                                #the_lib_files.remove(all_data)
                            librarian_data.append(create_librarian_location)
                            librarian_data.append(create_librarian_id)
                            json.dump(librarian_data, the_lib_files)

                elif super_user_choice == 3:
                    # remove / delete librarian
                    
                        librarian_data = []
                        count = 0 
                        with open(librarian_files) as remove_librarian:
                            all_librarian = json.load(remove_librarian)
                        if len(all_librarian) == 2:
                            delete_choice   = input("Are you sure you want to delete librarian?: 'y' | 'n': ")
                            delete_choice = delete_choice.lower()
                            if delete_choice == "y":
                                while (count < len(all_librarian)):
                                    with open(librarian_files,"w") as removed_librarian:
                                            for available_librarian in all_librarian:
                                                all_librarian.remove(available_librarian)
                                            json.dump(librarian_data, removed_librarian)
                                            count += 1
                        elif len(all_librarian) == 0:
                            print("There are no librarian available. You can add one.")

                elif super_user_choice == 4:
                    pass
                    # change password
                print("Success")
            else:
                print("Failed")
            

    # issue status
    def available_books(self):
        """ this shows all the books issued to people(s) """ 
        try:
            self.total_number_of_books = len(self.availabale_books)
        except AttributeError:
            print(f"There is an attribute error. Tip: Maybe the file '{available_books}' is missing")
        else:
            print(f"The total number of available books is: {self.total_number_of_books}")

    #search book
    def search_book(self, check_book):
        """ this searches for a book """
        if check_book in self.availabale_books:
            print(f"{check_book}: is available")
        else:
            print(f"{check_book}: is not available! This are the available book(s)")
            for book in self.availabale_books:
                print(f"-> {book}")

    #verify member
    def verify_member(self, verify_member):
        """ this will verify a member """
        self.unverified_members = "files/unverified_members.json"
        self.actual_member = []
        self.unactual_member = []
        try:
            with open(self.verified_members) as the_verified_members:
                all_verified_members = json.load(the_verified_members)
        except FileNotFoundError:
            print(f"The file '{self.verified_members}' was not found!")

        try:
            with open(self.unverified_members) as the_unverified_members:
                all_unverified_members = json.load(the_unverified_members)
        except FileNotFoundError:
            print(f"The file '{self.unverified_members}' was not found!")
        else:
            if verify_member in all_unverified_members:
                with open(self.verified_members,"w") as verify:
                    self.actual_member += all_verified_members
                    self.actual_member.append(verify_member)
                    json.dump(self.actual_member, verify)

                    with open(self.unverified_members, "w") as unverified:
                        all_unverified_members.remove(verify_member)
                        json.dump(all_unverified_members, unverified)


                    #all_unverified_members.remove(verify_member)
                    print(f"{verify_member}: has been verified")
            else:
                print(f"{verify_member}: was not found! This are the unverified member(s): ")
                with open(self.unverified_members) as not_found:
                    unverified_members  = json.load(not_found)
                    for member in unverified_members:
                        print(f"->. {member}")

    #issue book
    def issue_book(self, issue_book):
        """ this will issue a book if it is available"""
        the_added_issued_books = []
        try:
            with open(available_books, "w") as remove_book:
                if issue_book in self.availabale_books:
                    print(f"{issue_book}: has been issued")
                    self.issued_book = self.availabale_books.remove(issue_book)
                    json.dump(self.availabale_books, remove_book) 
                else:
                    print(f"{issue_book}: was not found! This are the available book(s): ")
                    json.dump(self.availabale_books, remove_book)
                    for book in self.availabale_books:
                        print(f"-> {book}")

            with open(the_issued_books) as all_issued_books:
                view_issued_books = json.load(all_issued_books)

            with open(the_issued_books, "w") as add_issued_book:
                if issue_book in self.availabale_books: 
                    the_added_issued_books.append(issue_book)
                    the_added_issued_books += view_issued_books
                    json.dump(the_added_issued_books, add_issued_book)
                else:
                    json.dump(view_issued_books, add_issued_book)
        except FileNotFoundError:
            print(f"The file(s) '{available_books}' or '{the_issued_books}' was not found!")
    # check issued books

    # payment 
    def payment (self):
        """ this will check the payments """ 
        print(f"The payments are: ")
        for pay in self.payments:
            print(f"-> {pay}")
        print (f"Total number of payment is {self.total_payments}")

# Books_database class
class Books_database(Librarian):
    """ This is a child class of the Library class """
    def __init__(self, location, librarian_id):
        """ initializing attributes of the Library class """
        super().__init__(location, librarian_id)
        self.book_title = ""
        self.book_author = ""
        self.book_id = ""
    # To-do compare with other book lists
    def update (self):
        """ this updates the books """
        self.bookname = input("Write which book you want to update: ")
        if self.bookname in self.availabale_books:
            print("Book found.")
            print("press 'd' to delete the book")
            print("press 'a' to update authour")
            print("press 't' to update title")
            print("press 'i' to update book ID")
            self.update_choice = input("what do you want to do?: ")
            self.update_choice = self.update_choice.lower()

            if self.update_choice == "d":
                self.availabale_books.remove(self.bookname)
                print(f"{self.bookname} has been deleted")
            elif self.update_choice == "a":
                self.new_book_author = input("Who is the book authour: ")
                self.book_author = self.new_book_author
                print("The new book author of {} is {}".format(self.bookname, self.book_author))
            elif self.update_choice == "t":
                self.new_book_title = input("Enter the new book title: ")
                self.book_title = self.new_book_title
                print("The book title of {} has update to {}".format(self.bookname,self.new_book_title))
            elif self.update_choice == "i":
                self.new_book_id = input("Enter new book ID: ")
                self.book_id = self.new_book_id
                print("The book {} has been update to {} ID number".format(self.bookname, self.book_id))
        else:
            print("Book not found")
        

    

    
person = Librarian("Nairobi", 1234)
print(person.super_user_login())