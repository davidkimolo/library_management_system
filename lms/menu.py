# import relevant files
import sys 
import vendor as vnd 
import library as lbr 
from patron import Patron as ptr
from patron import Patron_record as ptrr
while (True):
    # The menu
    print("MENU")
    print(" 1. Librarian \n 2. Patron \n 3. Vendor")
    try:
        choice = int(input("Select who you are (choose a number): "))
    except ValueError:
        print("you have not entered a numerical input! \nplease enter a number")
        
    # Librarian choice 

    if choice == 1:
        print(" 1. Check issued books \n 2. Search for a book \n 3. Verify a member \n 4. Issue a book \n 5. Check payments ")
        while (True):
            # Handling Value Error
            try:
                librarian_choice_one = int(input("What would you like to do? :"))
            except ValueError:
                print("you have not entered a numerical input! \nplease enter a number")
                break
            else:
                librarian_location = input("Enter your location: ")
                # handling ValueError
                try:
                    librarian_id = int(input("Enter your librarian ID: "))
                except ValueError:
                    print("Error! Please enter a numerical input")
                else: 
                    logged_in_user = lbr.Librarian(librarian_location, librarian_id)
            
                    if librarian_choice_one == 1:
                        logged_in_user.issue_status()

                    elif librarian_choice_one == 2:
                        check_book = input("Enter the book you want to check: ")
                        logged_in_user.search_book(check_book)

                    elif librarian_choice_one == 3:
                        verify_member = input ("Enter a member to verify: ")
                        logged_in_user.verify_member(verify_member)

                    elif librarian_choice_one == 4:
                        issue_book = input("Enter the book you want to issue: ")
                        logged_in_user.issue_book(issue_book)
                    elif librarian_choice_one == 5:
                        logged_in_user.payment()

    # Patron Choice            
    elif choice == 2:
        print(" 1. search a book \n 2. Request a book \n 3. Pay fine \n 4. Retrive user \n 5. Increase books issued \n 6. Decrease books")
        # Handling ValueError
        try:
            patron_choice  = int(input("Enter what you want to do: "))
        except ValueError:
            print("you have not entered a numerical input! \nplease enter a number")
        else:
            patron_name = input("Enter patron name: ")
            patron_email = input("Enter patron email: ")

            # handling ValueError
            try:
                patron_id = int(input("Enter patron Id: "))
            except ValueError:
                print("you have not entered a numerical input! \nplease enter a number")
            else:
                logged_in_patron = ptr(patron_name, patron_email, patron_id)

                if patron_choice == 1:
                    logged_in_patron.search()
                elif patron_choice == 2:
                    logged_in_patron.request()
                elif patron_choice == 3:
                    logged_in_patron.pay_fine()
                elif patron_choice == 4:
                    logged_in_patron_record = ptrr(patron_name, patron_email, patron_id)
                    try:
                        phone_number = int(input("Enter member phone number to search: "))
                    except ValueError:
                        print("Error! Please enter a numerical input.")
                    else:
                        phone_number = str(phone_number)
                        logged_in_patron_record.retrive_member(phone_number)
                elif patron_choice == 5:
                    logged_in_patron_record = ptrr(patron_name, patron_email, patron_id)
                    logged_in_patron_record.increse_book_issued()
                elif patron_choice == 6:
                    logged_in_patron_record = ptrr(patron_name, patron_email, patron_id)
                    logged_in_patron_record.decrease_books_issued()
                else:
                    print("You have entered an invalid choice!")

    # Vendor Choice    
    elif choice == 3:
        print(" 1. To search for a book \n 2. Supply books \n 3. Payment details")

        # handling ValueError
        try:
            vendor_choice  = int(input("Enter what you want to do: "))
        except ValueError:
            print("Error! Please enter a numerical input")
        else:
            vendor_instance = vnd.Vendor()
            if vendor_choice == 1:
                vendor_instance.search()
            elif vendor_choice == 2:
                vendor_instance.supply_book()
            elif vendor_choice == 3:
                vendor_instance.payment_details()
            else:
                print("Please enter the corrent number option")

    else:
        print("Please enter a valid choice. Exiting program ...")




