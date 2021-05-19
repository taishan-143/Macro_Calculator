def create_username(database):
    not_chosen_username = True
    while not_chosen_username:
        username = input("Create a username: ")
        if username is in database:
            print("That username already exists, try again.")
        else:
            return username 

def create_password(database):
    not_set_password = True
    while not_set_password:
        password = input("Create a password: ")
        password_2 = input("Re-enter your password: ")
        if password != password_2:
            print("Your passwords don't match! Try again.")
            not_set_password = True
        else:
            return password 

def register(database):
    name = input("Enter your full name: ")
    username = create_username(database)  
    password = create_password(database)  
    return name, username, password

def login(database):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    

    
def login_system():
    pass