import time
import os

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

    +==========================+
    |        MAIN MENU         |
    +==========================+
    | [1] Body fat percentage  |
    | [2] Maintenance calories |
    +==========================+
    
    Choose an option:
    """)

def view_another_page():  # The user decides if they wish to view the menu

    while True:
        choice = input("\nWould you like to view the menu again, Y or N?: ")
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


def start():
    app_initialisation("src/main/titlepage.txt")
    while True:
        clear()

        menu()

        
