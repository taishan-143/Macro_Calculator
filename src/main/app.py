import time
import os

from src.main.classes.person import *
from src.main.classes.persistence import *
from src.main.methods.body_fat_percentage_calc import body_fat_percentage_calculator
from src.main.methods.other_methods import *

def read_file(filepath):
    with open(filepath, 'r') as data:
        contents = data.read()
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
    read_file(title_path)
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
    | [3] Exit                 |
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

def personal_information(database):
    # instantiate person class
    while True:
        person = Person()
        persistence = Persistence()

        personal_info_menu()

        name = person.input_name()
        database[name] = {}

        age = person.input_age()
        persistence.save_data(database, "src/main/data/app_data.json", name, "Age", age)
        sex = person.input_sex()
        persistence.save_data(database, "src/main/data/app_data.json", name, "Sex", sex)
        weight = person.input_weight()
        persistence.save_data(database, "src/main/data/app_data.json", name, "Weight", weight)
        height = person.input_height()
        persistence.save_data(database, "src/main/data/app_data.json", name, "Height", height)
         
        if not view_another_page("\nWould you like to enter more details, Y or N?: "):
            print("Thanks, now calculate those macro's!")
            time.sleep(1)
            clear()
            break 


def start():
    app_initialisation("src/main/extras/titlepage.txt")
    while True:
        clear()

        menu()

        persistence = Persistence()
        database = persistence.load_data("src/main/data/app_data.json")

        view_menu = True
        while view_menu:
            try:
                option = int(input("Choose your selection here: "))

                if option == 0:
                    personal_information(database)
                    view_menu = False
                    # stick menu in without asking to view it here 
                elif option == 1:
                    read_file("src/main/extras/body_fat_percentage_instructions.txt")
                    # insert method which allows the user to choose a name and selects it's data
                    # run body_fat_percent_calc on user
                    view_menu = False
                elif option == 2:
                    # insert method which chooses a name and calculates maintenance calories
                    view_menu = False
                elif option == 3:
                    clear()
                    print("Stay healthy and motivated!")
                    time.sleep(1.5)
                    exit()
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