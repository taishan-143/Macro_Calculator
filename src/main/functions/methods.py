import time
import os

import src.main.classes

# Clears the screen
def clear():
    # clears the screen
    os.system("clear")

# Function to read through json file, grab names and append to a list -> potentially edit json file to support dictionary indexing.
def create_register(database):
    return list(database.keys())
    # returns '[name1, name2, name3]'

# Function which takes a name, and returns the appropriate data 
def user_data(database, name):
    return database[name]
    # returns '{Age: value, Sex: value, Weight: value, Height: value}'

# Table width function 
def table_width(header, data):
    biggest = len(header)
    if data == []:
        return biggest + 2
    elif type(data) == list:    
        for item in data:
            if item == '':
                continue
            elif len(item) > biggest:
                biggest = len(item)
        return biggest + 2
    else:                           
        for key, value in data.items():
            if value == '':
                continue
            elif len(str(value)) + len(str(key)) > biggest:
                biggest = len(str(value)) + len(str(key))
        return biggest + 5

# Function to display data in a table, data is in a list
def table(header, data):
    separator = '+' + '='*(table_width(header, data) + 4) + '+'
    print('\n' + separator)
    print(f'| {header}' + ' '*(table_width(header, data)-len(header) + 3) + '|')
    print(separator)
    for index, item in enumerate(data, 1):
        if item == '':
            continue
        else:
            print('|' + ' ' + '[' + str(index) + ']' + ' ' + item + ' '*(table_width(header, data) - len(item) - len(str(index))) + '|')
    print(separator)

# create function to display personal data in a table, data is in a list
def data_table(header, data):
    separator = '+' + '='*(table_width(header, data) + 1) + '+'
    print('\n' + separator)
    print(f'| {header}' + ' '*(table_width(header, data)-len(header)) + '|')
    print(separator)
    for item in data:
        if item == '':
            continue
        else:
            print('|' + ' ' + item + ' '*(table_width(header, data) - len(item)) + '|')
    print(separator)

# Read file data
def read_file(filepath):
    with open(filepath, 'r') as data:
        contents = data.read()
        print(contents)

# choose a user from a list of names
def choose_user(list_of_names):
    # show names in a table
    table("USERS", list_of_names)
    # take input from the user
    option = int(input(f"Which person would you like to select? (1 - {len(list_of_names)}): "))
    # from that input, return the desired name
    for index, name in enumerate(list_of_names, 1):
        if option == index:
            return name 

# The user decides if they wish to view the menu
def view_another_page(message):  

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

# Prompts the user to input personal information
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

# The loading screen for the app start
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

# View the users information
def view_user_information(database, user):
    age = database[user]["Age"]
    sex = database[user]["Sex"]
    weight = database[user]["Weight"]
    height = database[user]["Height"]
    body_fat = database[user]["Body Fat Percentage"]
    maintenance = database[user]["Maintenance Calories"]

    age_line = f"Age: {age} years"
    sex_line = f"Sex: {sex}"
    weight_line = f"Weight: {weight}kg"
    height_line = f"Height: {height}m"
    body_fat_line = f"Body Fat Percentage: {body_fat}%"
    maintenance_line = f"Maintenance Calories: {maintenance} calories"

    personal_data = [age_line, sex_line, weight_line, height_line, body_fat_line, maintenance_line]
    data_table(f"{user}'s Information", personal_data)
    