# import relevant files
import json 
import vendor as vnd 
import library as lbr 
from patron import Patron as ptr
from patron import Patron_record as ptrr
import super_user as sup

librarian_files = "files/librarian.json"
issues = "files/issues.json"
patron_files = "files/patron.json"
issues = "files/issues.json"
vendor_files = "files/vendor.json"


while (True):
    # The menu
    print("MENU")
    print(" 1. Librarian \n 2. Patron \n 3. Vendor \n 4. Super User")
    try:
        choice = int(input("Select who you are (choose a number): "))
    except ValueError:
        print("you have not entered a numerical input! \nplease enter a number")
        
    # Librarian choice 

    if choice == 1:
        print(" 1. Check Available books \n 2. Search for a book \n 3. Verify a member \n 4. Issue a book \n 5. Check payments ")
        while (True):
            # Handling Value Error
            try:
                librarian_choice_one = int(input("What would you like to do? :"))
            except ValueError:
                print("you have not entered a numerical input! \nplease enter a number")
                break
            else:
                with open(librarian_files) as librarian_details:
                    librarian_login_info = json.load(librarian_details)
                if len(librarian_login_info) == 2: 
                    logged_in_user = lbr.Librarian(librarian_login_info[0], librarian_login_info[1])
                    print(f"You have logged in as '{librarian_login_info[0]}' of id '{librarian_login_info[1]}'")
                else:
                    print("Librarian does not exist, sending error to super user...")
                    
                    all_issues = []
                    with open(issues) as non_librarian:
                        no_librarian = json.load(non_librarian)
                    issue_message = "Librarian does not exist. Please create one."
                    if issue_message in no_librarian:
                        print("The issue had already been submitted")
                        break
                    else:
                        with open(issues, "w") as create_librarian:
                            all_issues.append(issue_message)
                            all_issues += no_librarian
                            json.dump(all_issues, create_librarian)      
                        break
            
                if librarian_choice_one == 1:
                    logged_in_user.available_books()

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
        with open(patron_files) as load_patron:
            the_patron = json.load(load_patron)
        print(" 1. search a book \n 2. Request a book \n 3. Pay fine \n 4. Retrive user \n 5. Increase books issued \n 6. Decrease books")
        # Handling ValueError
        try:
            patron_choice  = int(input("Enter what you want to do: "))
        except ValueError:
            print("you have not entered a numerical input! \nplease enter a number")
        else:
            if len(the_patron) == 3:
                patron_name = the_patron[0]
                patron_email = the_patron[1]
                patron_id = the_patron[2]
                logged_in_patron = ptr(patron_name, patron_email, patron_id)
            else:
                print("Patron does not exist! Submitting issue to super user.")
                #add issue message to issues 
                missing_patron_isssue = ["Patron does not exist. Please add patron."]
                with open (issues) as view_missing:
                    if_missing = json.load(view_missing)
                if missing_patron_isssue[0] in if_missing:
                    print("The issue has already been submitted.")
                    break
                else:
                    with open(issues) as check_issue:
                        found_issue = json.load(check_issue)
                    with open(issues, "w") as missing_patron:
                        missing_patron_isssue += found_issue
                        json.dump(missing_patron_isssue, missing_patron)
                    break 

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
        with open (vendor_files) as vendor_data:
            all_vendor = json.load(vendor_data)
        # checking is there is an available vendor
        if len(all_vendor) < 3:
            print("There is no vendor available!")
            # send an issue message to super user
            vendor_issue = ["No vendor found. Please create a vendor."]
            with open(issues) as available_issues:
                get_issues = json.load(available_issues)
            with open(issues, "w") as submit_issue:
                vendor_issue += get_issues
                json.dump(vendor_issue, submit_issue)

        # assigning variables once a vendor is available
        elif len(all_vendor) == 3:
            vendor_name = all_vendor[0]
            vendor_location =  all_vendor[1]
            vendor_id = all_vendor[2]

            
        print(" 1. To search for a book \n 2. Supply books \n 3. Add books to inventory \n 4. Payment details")

        # handling ValueError
        try:
            vendor_choice  = int(input("Enter what you want to do: "))
        except ValueError:
            print("Error! Please enter a numerical input")
        else:
            vendor_instance = vnd.Vendor(vendor_name, vendor_location, vendor_id)
            print(f"You are logged in as '{vendor_name}'")
            if vendor_choice == 1:
                vendor_instance.search()
            elif vendor_choice == 2:
                vendor_instance.supply_book()
            elif vendor_choice == 3:
                vendor_instance.add_books()
            elif vendor_choice == 4:
                vendor_instance.payment_details()
            else:
                print("Please enter the corrent number option")

    elif choice == 4:
        print(sup.super_user_login())
        
    else:
        print("Please enter a valid choice. Exiting program ...")




