# Parent Library class
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
        self.availabale_books  = ["The Great Gatsby", "Beloved", "Invisible Man", "On The road" ]
        self.verified_members = []

    # issue status
    def issue_status(self):
        """ this shows all the books issued to people(s) """ 
        self.total_number_of_books = len(self.availabale_books)
        print(f"The total number of issued books is: {self.total_number_of_books}")

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
        self.unverified_members = ["David", "Kimolo", "Mwikya"]

        if verify_member in self.unverified_members:
            self.verified_members.append(verify_member)
            self.unverified_members.remove(verify_member)
            print(f"{verify_member}: has been verified")
        else:
            print(f"{verify_member}: was not found! This are the unverified member(s): ")
            for member in self.unverified_members:
                print(f"->. {member}")

    #issue book
    def issue_book(self, issue_book):
        """ this will issue a book if it is available"""
        if issue_book in self.availabale_books:
            print(f"{issue_book}: has been issued")
            self.availabale_books.remove(issue_book)
        else:
            print(f"{issue_book}: was not found! This are the available book(s): ")
            for book in self.availabale_books:
                print(f"-> {book}")


    # payment 
    def payment (self):
        """ this will check the payments """ 
        pass

# Books_database class
class Books_database(Library):
    """ This is a child class of the Library class """
    def __init__(self, location, librarian_id):
        """ initializing attributes of the Library class """
        super().__init__(location, librarian_id)
        self.book_title = ""
        self.book_author = ""
        self.book_id = ""

    def update (self):
        """ this updates the books """
        pass
    

    

