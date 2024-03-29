import time

from src.main.database import database
import src.main.functions.methods as methods
from src.main.functions.body_fat_percentage_calc import body_fat_percentage_calc
from src.main.functions.maintenance_calories import maintenance_calories
from src.main.functions.macronutrients import new_caloric_intake, macronutrient_ratios, display_macro_ratios

def menu():
    print(""" 
    Welcome to Macronumeracy! 

    Start by filling out your personal information.

    +===========================+
    |        MAIN MENU          |
    +===========================+
    | [0] Personal Information  |
    | [1] Body Fat Percentage   |
    | [2] Maintenance Calories  |
    | [3] Macronutrients        |    
    | [4] View User Information |
    | [5] Exit                  |
    +===========================+
    
    """)

def start():
    # methods.app_initialisation("src/main/extras/titlepage.txt")
    while True:
        methods.clear()

        menu()
        
        persistence = database.Data_Persistence()
    
        # create a register of names
        register = persistence.create_register()


        view_menu = True
        while view_menu:
            try:
                option = int(input("Choose your selection here: "))

                if option == 0:
                    methods.clear()
                    methods.personal_information()
                    view_menu = False
                    # stick menu in without asking to view it here 
                elif option == 1:
                    methods.clear()
                    methods.read_file("src/main/extras/body_fat_percentage_instructions.txt")
                    # grab a specific user from the list of names
                    specific_person = methods.choose_user(register)
                    # return that users data
                    specific_user_data = methods.user_data(specific_person)
                    print(specific_user_data)
                    # run body_fat_percent_calc on  user
                    body_fat_percentage = body_fat_percentage_calc(specific_user_data)
                    print(f"\nYour body fat percentage is {body_fat_percentage:.2f}%")
                    persistence.update_value_in_database("body_fat_percentage", body_fat_percentage, "name", specific_person)
                    view_menu = False
                elif option == 2:
                    methods.clear()
                    # grab a specific user from the list of names
                    specific_person = methods.choose_user(register)
                    # return that users data
                    specific_user_data = methods.user_data(specific_person)
                    # calculate that users maintenance calories
                    maintenance_cals = maintenance_calories(specific_user_data)
                    print(f"Your maintenance calories are: {maintenance_cals:.2f} calories")
                    persistence.update_value_in_database("maintenance_calories", maintenance_cals, "name", specific_person)
                    view_menu = False
                elif option == 3:
                    methods.clear()
                    # grab a user
                    specific_person = methods.choose_user(register)
                    # get their maintenance calories
                    maintenance_cals = persistence.load_data_from_database("maintenance_calories", "name", specific_person)
                    # calculate their macros
                    preference = input("Are you bulking, or cutting?: ")
                    New_Caloric_Intake = new_caloric_intake(preference, maintenance_cals)  
                    preferred_macro_ratios = macronutrient_ratios(New_Caloric_Intake)
                    show_ratios = display_macro_ratios(preferred_macro_ratios, New_Caloric_Intake)
                    print(show_ratios)
                    view_menu = False
                elif option == 4:
                    methods.clear()
                    # grab a user
                    specific_person = methods.choose_user(register)
                    # show their data
                    person_data = methods.view_user_information(specific_person)
                    methods.data_table(f"{specific_person}'s Information", person_data)
                    view_menu = False
                elif option == 5:
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