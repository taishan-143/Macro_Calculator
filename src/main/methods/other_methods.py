# Create function to read through json file, grab names and append to a list -> potentially edit json file to support dictionary indexing.
def create_register(database):
    return list(database.keys())
    # returns '[name1, name2, name3]'

# Create function which takes a name, and returns the appropriate data 
def user_data(database, name):
    return database[name]
    # returns '{Age: value, Sex: value, Weight: value, Height: value}'


# Create table width function 
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

# create function to display data in a table 
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

def read_file(filepath):
    with open(filepath, 'r') as data:
        contents = data.read()
        print(contents)

def choose_user(list_of_names):
    # show names in a table
    table("USERS", list_of_names)
    # take input from the user
    option = int(input(f"Which person would you like to select? (1 - {len(list_of_names)}): "))
    # from that input, return the desired name
    for index, name in enumerate(list_of_names, 1):
        if option == index:
            return name 

    
