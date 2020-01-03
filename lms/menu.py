# import relevant files
import vendor as vnd 
import library as lbr 
from patron import Patron as ptr

# The menu
print("MENU")
print(" 1. Librarian \n 2. Patron \n 3. Vendor")
choice = int(input("Select who you are (choose a number): "))

# Librarian choice 

if choice == 1:
    print(" 1. Check issued books \n 2. Search for a book \n 3. Verify a member \n 4. Issue a book \n 5. Check payments ")
    librarian_choice_one = int(input("What would you like to do? :"))
    librarian_location = input("Enter your location: ")
    librarian_id = input("Enter your librarian ID: ")
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
    print(" 1. search a book \n 2. Request a book \n 3. Pay fine")
    patron_choice  = int(input("Enter what you want to do: "))
    patron_name = input("Enter patron name: ")
    patron_email = input("Enter patron email: ")
    patron_id = input("Enter patron Id: ")
    logged_in_patron = ptr(patron_name, patron_email, patron_email)

    if patron_choice == 1:
        logged_in_patron.search()
    elif patron_choice == 2:
        logged_in_patron.request()
    elif patron_choice == 3:
        logged_in_patron.pay_fine()
    else:
        print("You have entered an invalid choice!")

# Vendor Choice    
elif choice == 3:
    print("What would you like to do? :")

else:
    print("Please enter a valid choice. Exiting program ...")




