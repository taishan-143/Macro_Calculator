import time
import os

from src.main.person import *

# Calculate body fat percentage => DONE
# Calculate maintenance calories
#   - weight, height, age input etc
#   - dependant on sex
# Calculate required daily macros 
#   - dependant on weight loss or gain


def title_page(title):
    with open(title, 'r') as starting_page:
        contents = starting_page.read()
        print(contents)
    
def app_initialisation(title_path):
    clear()
    print("initialising app .")
    time.sleep(0.5)
    clear()
    print("initialising app . .")
    time.sleep(0.5)
    clear()
    print("initialising app . . .")
    time.sleep(1)
    clear()
    title_page(title_path)
    time.sleep(2)
    print("\nCreated by Taishan Rowe :)")
    time.sleep(2)
    clear()


def clear():
    # clears the screen
    os.system("clear")

def menu():
    print(""" 
    Welcome to Macronumeracy! 

    Start by filling out your personal information.

    +==========================+
    |        MAIN MENU         |
    +==========================+
    | [0] Personal Information |
    | [1] Body Fat Percentage  |
    | [2] Maintenance Calories |
    +==========================+
    
    """)

def view_another_page(message):  # The user decides if they wish to view the menu

    while True:
        choice = input(message)
        if choice == '' or choice == ' ':
            continue
        elif choice[0].lower() == 'y':
            clear()
            # return true
            return choice      
        elif choice[0].lower() == 'n':
            clear()
            return False                                                        
        else:
            print("\nI dont understand.") 

def personal_information():
    # instantiate person class
    while True:
        person = Person()

        personal_info_menu()
        view_personal_details = True
        while view_personal_details:
            try:
                option = int(input("Choose some information to update, 1-6: "))

                if option == 1:
                    person.input_name()
                    view_personal_details = False
                elif option == 2:
                    person.input_age()
                    view_personal_details = False
                elif option == 3:
                    person.input_sex()
                    view_personal_details = False
                elif option == 4:
                    person.input_weight()
                    view_personal_details = False
                elif option == 5:
                    person.input_height()
                    view_personal_details = False
                else:
                    print("\nSorry I dont understand.\nPlease choose between 1 and 6.")
            except ValueError as v:
                print("Sorry, you didn't select a number.")

        if not view_another_page("Would you like to enter more details, Y or N?: "):
            print("Thanks, now calculate those macro's!")
            time.sleep(1)
            clear()
            break 


def start():
    app_initialisation("src/main/titlepage.txt")
    while True:
        clear()

        menu()

        view_menu = True
        while view_menu:
            try:
                option = int(input("Choose your selection here: "))

                if option == 0:
                    personal_information()
                    view_menu = False
                elif option == 1:
                    print("Fart")
                    view_menu = False
                elif option == 2:
                    print("Tart")
                    view_menu = False
                else:
                    print("\nSorry I dont understand.\nPlease choose either 1 or 2.")
            except ValueError as v:
                print("\nThat's not a number, try again")

        if not view_another_page("\nWould you like to view the main menu again, Y or N?: "):
            print("Stay healthy and motivated!")
            time.sleep(2)
            clear()
            break 


start()