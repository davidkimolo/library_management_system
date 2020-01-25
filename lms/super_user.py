# Librarian Super user
import json 
import getpass

available_books  = "files/available_books.json"
the_issued_books = "files/issued_books.json"
super_login = "files/super_user.json"
librarian_files = "files/librarian.json"
issues = "files/issues.json"
patron_files = "files/patron.json"
vendor_files = "files/vendor.json"


no_librarian_issue = "Librarian does not exist. Please create one."
no_patron_issue = "Patron does not exist. Please add patron."

def super_user_login ():
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
            print (" 1. Create a librarian \n 2. Add/Edit librarian details")
            print(" 3. Remove librarian \n 4. Create a patron \n 5. edit patron details \n 6. remove patron")
            print(" 7. Create vendor \n 8. Edit vendor \n 9. Remove vendor")
            print(" 10. Change password \n 11. Check issues")
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
                        with open(issues) as missing_librarian:
                            none_librarian = json.load(missing_librarian)
                        if no_librarian_issue in none_librarian:
                            none_librarian.remove(no_librarian_issue)
                        with open(issues, "w") as remove_issues:
                            json.dump(none_librarian, remove_issues)
                        print("You have successfully created a librarian.")
                elif len(all_lib_files) == 2:
                    print("Librarian already exists!")

            elif super_user_choice == 2:
                # edit librarian details
                    librarian_data = []
                    create_librarian_location = input("Enter new librarian location: ")
                    try:
                        create_librarian_id = int(input ("Enter new librarian id: "))
                    except ValueError:
                        print("Please enter a numerical value.")
                    with open(librarian_files, "r+")  as the_lib_files:
                        #for all_data in the_lib_files:
                            #the_lib_files.remove(all_data)
                        librarian_data.append(create_librarian_location)
                        librarian_data.append(create_librarian_id)
                        json.dump(librarian_data, the_lib_files)
                        with open(issues) as missing_librarian:
                            none_librarian = json.load(missing_librarian)
                        if no_librarian_issue in none_librarian:
                            none_librarian.remove(no_librarian_issue)
                        with open(issues, "w") as remove_issues:
                            json.dump(none_librarian, remove_issues)
                        print("Librarian details added successfully.")

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
                                        print("You have successfully deleted a librarian.")
                    elif len(all_librarian) == 0:
                        print("There are no librarian available. You can add one.")
            elif super_user_choice == 4:
                patron_data = []
                with open(patron_files) as available_patron:
                    check_patron = json.load(available_patron)
                
                if len(check_patron) != 3:
                    #create a patron
                    with open(patron_files, "w") as add_patron:
                        patron_name = input("Enter a patron name: ")
                        patron_data.append(patron_name)
                        patron_email = input("Enter patron_email: ")
                        patron_data.append(patron_email)
                        patron_id = int(input("Enter patron ID: "))
                        patron_data.append(patron_id)

                        patron_data += check_patron
                        json.dump(patron_data, add_patron)
                        with open(issues) as check_missing_patron:
                            found_patron = json.load(check_missing_patron)
                        if no_patron_issue in found_patron:
                            with open(issues, "w") as all_patron_missing_issue:
                                found_patron.remove(no_patron_issue)
                                json.dump(found_patron, all_patron_missing_issue) 

                elif len(check_patron) == 3:
                    print("A patron already exists.")
            elif super_user_choice == 5:
                # edit patron
                patron_data = []
                with open(patron_files) as available_patron:
                    check_patron = json.load(available_patron)
                if len(check_patron) == 3:
                    print("You are editing patron details")
                    with open(patron_files, "w") as add_patron:
                        patron_name = input("Enter a patron name: ")
                        patron_data.append(patron_name)
                        patron_email = input("Enter patron_email: ")
                        patron_data.append(patron_email)
                        patron_id = int(input("Enter patron ID: "))
                        patron_data.append(patron_id)

                        json.dump(patron_data, add_patron)
                        print("You have editted patron details.")
                else:
                    print("Patron does not exit. TIP: Create a patron.")

            elif super_user_choice == 6:
                # remove patron
                patron_data = []
                with open(patron_files) as available_patron:
                    check_patron = json.load(available_patron)
                if len(check_patron) > 0:
                    with open(patron_files, "w") as remove_patron:
                        json.dump(patron_data, remove_patron)
                else:
                    print("There is no patron. TIP: Add a patron")
            elif super_user_choice == 7:
                # create a vendor
                with open(vendor_files) as check_vendor:
                    vendor_result = json.load(check_vendor)
                    #check if vendor exists
                if len(vendor_result) == 3:
                    print("The vendor is already there")
                elif len(vendor_result) < 3:
                    # create vendor
                    vendor_name = input("Enter vendor name: ")
                    vendor_location = input("Enter vendor location: ")
                    vendor_id = input("Enter vendor ID: ")
                    vendor_data = []
                    vendor_issue = "No vendor found. Please create a vendor."
                    with open(vendor_files, "w") as new_vendor:
                        vendor_data.append(vendor_name)
                        vendor_data.append(vendor_location)
                        vendor_data.append(vendor_id)
                        vendor_data += vendor_result
                        json.dump(vendor_data, new_vendor)
                    with open(issues) as check_vendor_issue:
                        the_vendor_issue = json.load(check_vendor_issue)
                        # removing missing vendor issue
                    if vendor_issue in the_vendor_issue:
                        the_vendor_issue.remove(vendor_issue)
                        with open (issues, "w") as resolved:
                            json.dump(the_vendor_issue, resolved)

            elif super_user_choice == 8:
                # edit vendor
                with open(vendor_files) as check_available:
                    availability = json.load(check_available)
                if len(availability) != 3:
                    print("There is no vendor. please add vendor first.")
                elif len(availability) == 3:
                    # edit user 
                    vendor_name = input("Enter vendor name: ")
                    vendor_location = input("Enter vendor location: ")
                    vendor_id = input("Enter vendor ID: ")
                    vendor_data = []
                    with open(vendor_files, "w") as new_vendor:
                        vendor_data.append(vendor_name)
                        vendor_data.append(vendor_location)
                        vendor_data.append(vendor_id)
                        json.dump(vendor_data, new_vendor)
 
            elif super_user_choice == 9:
            # remove a user
                with open(vendor_files) as check_vendor:
                    vendor_status = json.load(check_vendor)
                    #checking if there is an existing vendor
                if len(vendor_status) == 3:
                    #remove the vendor
                    print("Deleting vendor....")
                    empty_vendor = []
                    with open(vendor_files, "w") as remove_vendor:
                        #empty_vendor += vendor_status
                        json.dump(empty_vendor, remove_vendor)
                elif len(vendor_status) < 3:
                    print("There is no vendor to be removed!")

            
            elif super_user_choice == 10:
                # change password
                old_password = getpass.getpass("Enter the old password: ")
                new_password = getpass.getpass("Enter your new password: ")
                confirm_password = getpass.getpass("Confirm password: ")
                with open(super_login) as the_password:
                    all_info = json.load(the_password)
                
                with open(super_login,"w") as change_password:
                    if old_password == all_info[1] and new_password == confirm_password:
                        all_info[1] = new_password
                        json.dump(all_info, change_password)
                    print("You have successfully changed your password.")

            # Check issues
            elif super_user_choice == 11:
                with open(issues) as fix_issues:
                    all_the_issues = json.load(fix_issues)
                if len(all_the_issues) != 0:
                    number_of_issues = len(all_the_issues)
                    print("This are the issues that have been submitted. Number of issues ({})".format(number_of_issues))
                    for issue in all_the_issues:
                        print(f"-> {issue}")
                else:
                    print("There are no issues.")

        else:
            print("Failed")


