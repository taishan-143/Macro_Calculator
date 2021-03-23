
class Person:
    def __init__(self):
        self.forename = ''
        self.surname  = ''
        self.age      = ''
        self.sex      = ''
        self.weight   = '' 
        self.height   = ''

    def input_name(self):
        # Enter full name.
        full_name = input("Enter your full name: ")
        # Split string and slice at indexes 0 and 1 for the forename and surname respectively.
        self.forename = full_name.split()[0].capitalize()
        self.surname = full_name.split()[1].capitalize()
        # Return a tuple of the forename and surname. 
        return (self.forename, self.surname)
    
    def input_age(self):
        # Condition to hold the loop in place 
        not_acquired_age = True
        while not_acquired_age:
            try: 
                # Acquire the age
                self.age = int(input("How old are you?: "))
                # Check the age isn't less than zero -> impossible.
                if self.age < 0:
                    print("You can't be negative years old, can you?")
                    not_acquired_age = True
                else:
                    # Exit loop and return the age
                    not_acquired_age = False
                    return self.age 
            # Check an integer was passed in for the age
            except ValueError as e:
                print("You entered an invalid age, try again.")
                not_acquired_age = True 
    
    def input_sex(self):
        # Contition to hold the loop open 
        not_acquired_sex = True
        while not_acquired_sex:
            # Input sex
            self.sex = input("Are you male or female?: ")
            # Check to see if sex is male or female
            if self.sex[0].lower() == 'm' or self.sex[0].lower() == 'f':
                not_acquired_sex = False
                return self.sex 
            # If not, keep looping until a correct result is returned.
            else:
                print("You haven't entered a valid sex.")
                not_acquired_sex = True

    def input_weight(self):
        try:
            self.weight = int(input("Enter your weight in kg: "))

    def input_height(self):
        try:
            self.height = int(input("Enter your height in cm: "))






person = Person()





