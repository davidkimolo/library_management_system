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
        librarian_id = ""
    
    def issue_status(self):
        """ this shows all the books issued to people(s) """ 
        self.total_number_of_books = 416
        print(f"The total number of issued books is: {self.total_number_of_books}")

    
    def search_book(self, check_book):
        """ this searches for a book """
        self.availabale_book = ["The Great Gatsby", "Beloved", "Invisible Man", "On The road" ]
        if check_book in self.availabale_book:
            print(f"{check_book}: is available")
        else:
            print(f"{check_book}: is not available")

    def verify_member(self):
        """ this will verify a member """
        pass
    
    def issue_book(self):
        """ this will issue a book """
        pass
    def payment (self):
        """ this will check the payments """ 
        pass

# Boos_database class
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
    

    

