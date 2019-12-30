class Patron:
    """ this is the Patron class """
    def __init__(self, name, email, patron_id):
        """ this are the patron class attributes """
        self.name = name
        self.email = email
        self. patron_id = patron_id

    def search(self):
        """ this will enable the patron search a book """
        pass

    def request(self):
        """ this enables the patron to see book requests """
        pass
    
    def pay_fine(self):
        """ this will make the patron be able to pay fines """
        pass

class Patron_record(Patron):
    """ this is a child class of the parent Patron """
    def __init__(self, name, email, patron_id, date_of_membership, no_of_books_issued, max_no_limit, phone_no, fines_owed):
        super().__init__(name, email, patron_id)
        """ this are thr attributes of the child class Pareon_record """
        self.patron_id = patron_id
        self.name  = name
        self.email = email
        self.date_of_membership = date_of_membership
        self.number_of_books_issued = no_of_books_issued
        self.maximum_number_limit = max_no_limit
        self.phone_number = phone_no
        self.fines_owed = fines_owed

