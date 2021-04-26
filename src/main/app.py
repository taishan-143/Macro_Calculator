import time

from src.main.classes.persistence import *
import src.main.functions.methods as methods
from src.main.functions.body_fat_percentage_calc import body_fat_percentage_new_calc
from src.main.functions.maintenance_calories import maintenance_calories




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

def start():
    methods.app_initialisation("src/main/extras/titlepage.txt")
    while True:
        methods.clear()

        menu()
        
        persistence = Persistence()
        database = persistence.load_data("src/main/data/app_data.json")

        # create a register of names
        names = methods.create_register(database)

        view_menu = True
        while view_menu:
            try:
                option = int(input("Choose your selection here: "))

                if option == 0:
                    methods.clear()
                    methods.personal_information(database)
                    view_menu = False
                    # stick menu in without asking to view it here 
                elif option == 1:
                    methods.clear()
                    methods.read_file("src/main/extras/body_fat_percentage_instructions.txt")
                    # grab a specific user from the list of names
                    specific_person = methods.choose_user(names)
                    # return that users data
                    specific_user_data = methods.user_data(database, specific_person)
                    # run body_fat_percent_calc on  user
                    body_fat_percentage = body_fat_percentage_new_calc(specific_user_data)
                    print(body_fat_percentage)
                    view_menu = False
                elif option == 2:
                    methods.clear()
                    # grab a specific user from the list of names
                    specific_person = methods.choose_user(names)
                    # return that users data
                    specific_user_data = methods.user_data(database, specific_person)
                    # calculate that users maintenance calories
                    maintenance_cals = maintenance_calories(specific_user_data)
                    print(maintenance_cals)
                    view_menu = False
                elif option == 3:
                    methods.clear()
                    print("Stay healthy and motivated!")
                    time.sleep(1.5)
                    exit()
                else:
                    print("\nSorry I dont understand.\nPlease choose either 1 or 2.")
            except ValueError as v:
                print("\nThat's not a number, try again")

        if not methods.view_another_page("\nWould you like to view the main menu again, Y or N?: "):
            print("Stay healthy and motivated!")
            time.sleep(2)
            methods.clear()
            break 



if __name__ == "__main__":
    start()