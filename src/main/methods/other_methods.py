# Create function to read through json file, grab names and append to a list -> potentially edit json file to support dictionary indexing.
def create_register(filepath):
    return list(filepath.keys())
    # returns '[name1, name2, name3]'

# Create function which takes a name, and returns the appropriate data 
def user_data(filepath, name):
    return filepath[name]
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
    separator = '+' + '='*table_width(header, data) + '+'
    print('\n' + separator)
    print(f'| {header}' + ' '*(table_width(header, data)-len(header)-1) + '|')
    print(separator)
    if type(data) == dict:
        for key, value in data.items():          
            print('|' + ' ' + f"[{str(key)}]" + ' ' + str(value) + ' '*(table_width(header, data)-len(str(key))-len(str(value))-4) + '|')
    else:
        for item in data:
            print('|' + ' ' + item + ' '*(table_width(header, data)-len(item)-1) + '|')
    print(separator)



