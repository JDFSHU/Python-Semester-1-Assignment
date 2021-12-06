import string
import random
from functools import reduce

# Name: Jacob Frazer
# Student Number: 31004433

loginAttempts = 1  # login attempt counter for admin login
records = 0  # used for view user menu records counter
showRecords = 0  # used for view user menu records counter for viewable passwords
searchRecords = 0

#  user details lists
autoUsername = []  # used to hold auto generated username later on
hiddenPassword = []  # used to hold auto generated hidden password later on
users = []  # 1d list to place user details
allUserDetails = []  # 2d list for non asterisked passwords


def main_menu():  # function for main menu
    print(":: Main Menu ::")
    print("1. Create New User")
    print("2. View User")
    print("3. Update User")
    print("4. Quit")


def new_user_menu():  # function for the new user menu
    print("\n::New User Menu::")
    print("-" * 17)


def user_role():  # function for role selection menu
    print("\nSelect role for the user: ")
    print("1. User")
    print("2. Admin")


def department():  # function for the department selection menu
    print("\nSelect department for the user: ")
    print("1. Administration")
    print("2. Operation")
    print("3. Technology")


def dept_summary():  # function for the user profile
    print("\n:: User Profile Summary ::")
    print("-" * 25)
    print("First Name: ", users[-4])
    print("Last Name: ", users[-3])
    print("User Role: ", users[-2])
    print("User Department:", users[-1], "\n")


def view_user():  # function for view user menu
    print("\n:: View User ::")
    print("\nList of Users")
    print("-" * 15)


def update_user():  # function for update user menu
    print("\n:: Update User ::")
    print("-" * 17)
    print("\nWhich field would you like to update?\n")
    print("1. First Name")
    print("2. Last Name")
    print("3. Role")
    print("4. Department")


def random_password():  # function that creates a random password when called
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits  # what characters are available to be used
    size = random.randint(8, 8)  # what range the password can fall between
    return ''.join(random.choice(chars) for x in range(size))


def random_username():  # function that creates a random username when called
    chars = string.ascii_lowercase + string.digits  # what characters are available to be used
    size = random.randint(1, 2)  # what range the username can fall between
    return firstName.lower() + lastName.lower().join(random.choice(chars) for x in range(size))


# ------------------------------------------------ REQUIREMENT 1 ------------------------------------------------------#
# Initial login message and inputs asking for user to enter username and password
print(" :: Welcome to User Management System :: ")
print("-" * 42)
userName = input("Username : ")
userPassword = input("Password : ")

# ------------------------------------------------ REQUIREMENT 2 ------------------------------------------------------#
# While loop to check user input is correct username and password is correct if not, login attempts are incremented by 1
# if login attempts reaches 3 attempts, else statement kicks into effect and ends program
while userName != "admin" or userPassword != "123":
    if loginAttempts <= 2:
        print("Attempt : ", loginAttempts)
        print("Invalid username and password!\n")
        userName = input("Username : ")
        userPassword = input("Password : ")
        loginAttempts += 1
    else:
        print("Account has been blocked")
        quit()

# ------------------------------------------------ REQUIREMENT 3 ------------------------------------------------------#
# if details are correct, this message is printed and then the main_menu function is called to print the main menu
# once main menu printed, user input is asked to select a menu number
print("\nSuccessfully logged in\n")
main_menu()  # main menu function
mainSelection = input("\nSelect a menu - input a number: ")

# ------------------------------------------------ REQUIREMENT 4 ------------------------------------------------------#
# This is the main while loop that the rest of the program is contained within, there is an else statement right at the
# end of the program which checks if the user has entered digits outside of the expected digits, the if statement checks
# if the input is a digit and asks user to renter if not.
while mainSelection != ("1", "2", "3", "4"):  # loops while main selection isn't expected digits
    if not mainSelection.isdigit():  # checking that main menu selection is a digit
        mainSelection = input("\nYou have entered a non digit value, Select again: ")  # prompting reentry

# ------------------------------------------------ REQUIREMENT 5 ------------------------------------------------------#
# if user input on the main menu is 1 then the create new user block of code is initiated, this asks for the first and
# last name of the new user, these details are then appended to a list of users
    elif mainSelection == "1":  # create new user menu code block
        new_user_menu()  # new user menu function
        firstName = input("Input First name: ")
        users.append(firstName)
        lastName = input("Input Last Name: ")
        users.append(lastName)

# ------------------------------------------------ REQUIREMENT 9 ------------------------------------------------------#
# random_username function randomly generates a username based on the first and last name the user inputted + some
# random digits, if this new randomised username is found in the allUserDetails list then the new randomised username
# is deleted autoUsername[-1] and another is randomly generated. Once username is checked and found to be unique, its
# appended to autoUsername list
        autoUsername.append((random_username()))
        if autoUsername[-1] in allUserDetails:
            print("\nGenerating new username and checking database")
            print("\nUsername already exists generating new")
            print("\nDuplicate username = ", autoUsername[-1])
            del autoUsername[-1]  # deleting the last element in autoUsername that was just created
            autoUsername.append(random_username())  # generating new username
        else:
            print("\nUsername provisionally generated Checked and OK!")  # will pretty much always print this due to
            # username generation complexity

# ------------------------------------------------ REQUIREMENT 6 ------------------------------------------------------#
# selecting user role for the creation of a new user, user role menu is printed via function user_role() and then user
# is asked for input, if user doesnt select the correct input they are asked again. if user selects the correct input
# their selection is appended to the users list.
        user_role()  # prints user role menu
        roleSelect = input("Enter here: ")
        while roleSelect != "1" and roleSelect != "2":  # while loop to check correct selection
            print("Unrecognised Input!\n")
            user_role()
            roleSelect = input("enter here: ")
        if roleSelect == "1":
            users.append("User")
        elif roleSelect == "2":
            users.append("Admin")
# selecting department for the creation of the new user, department menu is printed via function department(), again
# if user doesnt generate the right input, the while loop will keep looping until they do
        department()  # prints department menu
        deptSelect = input("Enter here: ")
        while deptSelect != "1" and deptSelect != "2" and deptSelect != "3":  # while loop to check correct selection
            print("Unrecognised Input!\n")
            department()
            deptSelect = input("enter here: ")

# ------------------------------------------------ REQUIREMENT 7 ------------------------------------------------------#
# Once the department selection has been appended to the users list, the dept_summary() function is called which prints
# the current user details that have been inputted for this latest user.
        if deptSelect == "1":
            users.append("Administration")
            dept_summary()
        elif deptSelect == "2":
            users.append("Operation")
            dept_summary()
        elif deptSelect == "3":
            users.append("Technology")
            dept_summary()
# ------------------------------------------------ REQUIREMENT 8 ------------------------------------------------------#
# Asking user if they want to quit and delete the details they have inputted so far, while loop checks for any entry
# other than 1, if they choose 1 the program continues, if they hit any key, the user details are deleted via emptying
# the users list
        userConfirm = input("Press 1 to proceed with username and password creation or any to quit: ")
        while userConfirm != "1":
            print("\nDetails deleted\n")
            users = []  # emptying all the appended details that have just been created
            main_menu()  # printing main menu
            mainSelection = input("\nSelect a menu - input a number: ")  # asking user for entry
            break
# ------------------------------------------------ REQUIREMENT 10 -----------------------------------------------------#
# This block of code uses the random_password() function to auto generate a new user password and then also slices that
# passwords first 5 digits and replaces them with asterisks, once done this hidden password is printed with the auto
# generated username and then both are appended to the users list, the user list is also appended with the temp password
# which was created prior to slicing and all are thrown into the users list, the user list is then appended to a 2d list
# allUserDetails and then the user list is emptied for future creation of new users
        else:
            print("\nGenerating username and password .....\n")
            users.append(autoUsername[-1])  # Last username generated added to visibleUsers
            tempPass = random_password()  # random password generated and held in temporary variable tempPass
            passConvert = list(tempPass)  # converting tempPass to a list passConvert
            passConvert[0:5] = "*****"  # slicing first 5 digits of passConvert and replacing with asterisks
            asteriskPass = "".join(passConvert)  # joining passConvert to a new variable asteriskPass
            hiddenPassword.append(asteriskPass)  # appending new variable to hiddenPassword list
            print("Generated username: ", autoUsername[-1])  # printing the last userName generated
            print("Generated password: ", hiddenPassword[-1])  # printing the last password generated but hidden
            users.append(hiddenPassword[-1])  # appending hiddenPassword to hiddenUsers list
            users.append(tempPass)  # temp password appended to visibleUsers before its altered
            allUserDetails.append(users)  # creation of 2D list
            print("\nUser account has been successfully saved \n")
            users = []  # emptying list
            main_menu()  # printing the main menu
            mainSelection = input("\nSelect a menu - input a number: ")  # asking user for main menu input

# ------------------------------------------------ REQUIREMENT 11 -----------------------------------------------------#
# if option 2 on main menu the view_user() function is called and a for loop initiated to loop through the records in
# the 2d list allUserDetails, a records counter is incremented by 1 each loop to show which record is which and is
# cleared at the end once the loop has finished to ensure that viewing the users a second time still shows the correct
# record numbers
    elif mainSelection == "2":
        view_user()  # prints the view user menu
        print("\nThere is/are ", len(allUserDetails), "records\n")
        records += 1
        print("-" * 35)
        for row in range(len(allUserDetails)):
            print("Record: ", records)
            records += 1
# creating a new variable s which utilises f strings to allow me to print strings in front of the list elements
            s = (f"""\
Name          : {allUserDetails[row][0]} {allUserDetails[row][1]}
Role          : {allUserDetails[row][2]}
Department    : {allUserDetails[row][3]}
Username      : {allUserDetails[row][4]}
Password      : {allUserDetails[row][5]}""")  # element 5 is the hidden password

            maxlen = reduce(lambda x, y: max(x, len(y)), s.split("\n"), 0)
            print(f"{s}\n{'-' * 35} \n")  # prints a new line in between each record
        records = 0
        print()
        revealPasswords = input("""\nPress 999 to see the user passwords - (Warning user password view should get
    permissions from super admin!) Press 1 to return to Main Menu: """)
        # asking user if they want to reveal or return

# ------------------------------------------------ REQUIREMENT 12 -----------------------------------------------------#
# while loop checks if the user entered the correct digits, if not if keeps asking until they do, if the user asks to
# reveal the hidden passwords then the same for loop as above is initiated but instead of calling the 5th element for
# the password column it calls the 6th which is the temporary password that was created prior to slicing with asterisks
        while revealPasswords != ("999", "1"):  # loops while main selection isn't expected digits
            if not revealPasswords.isdigit():  # checking that main menu selection is a digit
                revealPasswords = input("You have entered a non digit value, Select again: ")  # prompting reentry
            elif revealPasswords == "999":
                print("\nThere is/are ", len(allUserDetails), "records\n")
                showRecords += 1  # different records counter to ensure records continuity
                print("-" * 35)
                for row in range(len(allUserDetails)):
                    print("Record: ", showRecords)
                    showRecords += 1
                    s = (f"""\
Name          : {allUserDetails[row][0]} {allUserDetails[row][1]}
Role          : {allUserDetails[row][2]}
Department    : {allUserDetails[row][3]}
Username      : {allUserDetails[row][4]}
Password      : {allUserDetails[row][6]}""")  # element 6 is the viewable password

                    maxlen = reduce(lambda x, y: max(x, len(y)), s.split("\n"), 0)
                    print(f"{s}\n{'-' * 35}\n")

                showRecords = 0
                print()
                main_menu()
                mainSelection = input("\nSelect a menu - input a number: ")  # main menu selection from user
                break
# if user enters 1 then main menu is printed again, when user selects a new menu selection the program breaks out of the
# while loop and the program enters the selected menu
            elif revealPasswords == "1":
                print()
                main_menu()
                mainSelection = input("\nSelect a menu - input a number: ")  # main menu selection from user
                break
            else:
                revealPasswords = input(("Select either 999 to view passwords !Super Admin! only or press 1 to"
                                         "return to Main Menu: "))

# ------------------------------------------------ REQUIREMENT 13 -----------------------------------------------------#
# if user selects main menu 3 the user search input is asked of the user, converted all user input to lowercase as all
# usernames are created lowercase by default in the random_username function
    elif mainSelection == "3":
        print("\n:: User Search :: ")
        print("-" * 17)
        searchUser = input("\nInput username to edit (press 1 to return to Main Menu): ").lower()

# ------------------------------------------------ REQUIREMENT 14 -----------------------------------------------------#
# while user input of the username is not found in allUserDetails the user is advised that the record cannot be located
# for loop loops through the records, if it finds the record it prompts the user to that it is found and what field
# they would like to update, user is able to update the same user by pressing 1 or by hitting any they return to the
# search field and can enter 1 to return to the main menu.
        while searchUser != "1":
            for x in allUserDetails:
                if x[4] == searchUser:
                    print()
                    print(searchUser, "found in the list")
                    update_user()
                    updateSelection = input("\nInput number of field or press any to return to Menu 3: ")

# ------------------------------------------------ REQUIREMENT 15 -----------------------------------------------------#
# based on user input of the update_user() menu function, the user is able to update first name, last name, role and
# department, this is achieved by indexing the list that contains the username as x and then updating element positions
# of x with user input or user selections of roles and departments available, user is able to update the same user or
# return to menu 3 by hitting any key

                    if updateSelection == "1":
                        newFirstName = input("\nInput new First Name: ")
                        x[0] = newFirstName
                        print("\nUpdate Successful")
                        goAgain = input("\nPress 1 to update the same user again, press any to search new user: ")
                        if goAgain == "1":
                            update_user()
                            updateSelection = input("\nInput number of field or press any to return to Menu 3: ")
                        if goAgain != "1":
                            continue

                    if updateSelection == "2":
                        newLastName = input("\nInput new Last Name: ")
                        x[1] = newLastName
                        print("\nUpdate Successful")
                        goAgain = input("\nPress 1 to update the same user again, press any to search new user: ")
                        if goAgain == "1":
                            update_user()
                            updateSelection = input("\nInput number of field or press any to return to Menu 3: ")
                        if goAgain != "1":
                            continue

                    if updateSelection == "3":
                        print("\nSelect Role for the selected User")
                        print("1: User")
                        print("2: Admin")
                        newRole = input("\nInput number of field: ")
                        if newRole == "1":
                            x[2] = "User"
                            print("\nUpdate Successful")
                        if newRole == "2":
                            x[2] = "Admin"
                            print("\nUpdate Successful")
                        goAgain = input("\nPress 1 to update the same user again, press any to search new user: ")
                        if goAgain == "1":
                            update_user()
                            updateSelection = input("\nInput number of field or press any to return to Menu 3: ")
                        if goAgain != "1":
                            continue

                    if updateSelection == "4":
                        print("\nSelect Department for the selected User")
                        print("1: Administration")
                        print("2: Operation")
                        print("3: Technology")
                        newDepartment = input("\nInput number of field: ")
                        if newDepartment == "1":
                            x[3] = "Administration"
                            print("\nUpdate Successful")
                        if newDepartment == "2":
                            x[3] = "Operation"
                            print("\nUpdate Successful")
                        if newDepartment == "3":
                            x[3] = "Technology"
                            print("\nUpdate Successful")
                        goAgain = input("\nPress 1 to update the same user again, press any to search new user: ")
                        if goAgain == "1":
                            update_user()
                            updateSelection = input("\nInput number of field or press any to return to Menu 3: ")
                        if goAgain != "1":
                            continue
            else:
                print("\nUser not found")
                break
        else:
            print()
            main_menu()
            mainSelection = input("\nSelect a menu - input a number: ")  # main menu selection from user

    elif mainSelection == "4":
        print("\nYou have logged out")  # self explanatory but when user choose 4 on the main menu, the program finishes
        quit()  # quit function to close program

# -------------------------------------------------REQUIREMENT 4 ------------------------------------------------------#
    else:
        print("\nThere is no menu ", mainSelection, "\n")  # telling the user that their specific entry isn't an option
        main_menu()  # printing the main menu again
        mainSelection = input("\nSelect a menu - input a number: ")  # asking user for re-entry


