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
        """ this shows all the books issues to people(s) """ 
        pass 
    
    def search_book(self):
        """ this searches for a book """
        pass
    def verify_member(self):
        """ this will verify a member """
        pass
    
    def issue_book(self):
        """ this will issue a book """
        pass
    def payment (self):
        """ this will pay for books """ 
        pass
    

    

