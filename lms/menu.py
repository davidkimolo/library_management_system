# import relevant files
import vendor as vnd 
import patron as ptr 
import library as lbr 

# The menu
print("MENU")
print(" 1. Librarian \n 2. Patron \n 3. Vendor")
choice = int(input("Select who you are (choose a number): "))


if choice == 1:
    print(" 1. Check issued books \n 2. Search for a book \n 3. Verify a member \n Issue a book \n Check payments ")
    librarian_choice_one = int(input("What would you like to do? :"))

    if librarian_choice_one == 1:
        librarian_location = input("Enter your location: ")
        librarian_id = input("Enter your librarian ID: ")
        logged_in_user = lbr.Librarian(librarian_location, librarian_id)
        logged_in_user.issue_status()
        
elif choice == 2:
    print("What would you like to do? :")
    
elif choice == 3:
    print("What would you like to do? :")

else:
    print("Please enter a valid choice. Exiting program ...")

