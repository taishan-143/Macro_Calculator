
activity = """How active are you?

1. Sedentary - Normal everyday activity like walking, couple flights of stairs.
2. Lightly active - Participate in any activity that burns an additional 200-400 calories for women, and 250-500 for men.
3. Moderately active - Any activity that burns an additional 400-650 calories for women, or 500-800 for men.
4. Very active - Any activity that burns more than 650 calories for women, or more than 800 for men.

1 - 4: 
"""

# weight in kg, height in cm 

def male_REE(weight, height, age):
    return (10 * weight) + (6.25 * height) - (5 * age) + 5

def female_REE(weight, height, age):
    return (10 * weight) + (6.25 * height) - (5 * age) - 161

def calculate_REE(sex, weight, height, age):
    if sex[0].lower() == 'm':
        return male_REE(weight, height, age)
    elif sex[0].lower() == 'f':
        return female_REE(weight, height, age)
    else:
        # elaborate on error checks!
        raise KeyError

def determine_TDEE_constant(activity):
    # Condition to hold the loop open
    not_determined_constant = True 
    while not_determined_constant:
        try:
            # Get user input for TDEE constant
            activity_measure = int(input(activity))
            # return the correct constant 
            if activity_measure == 1:
                return 1.2
                not_determined_constant = False
            elif activity_measure == 2:
                return 1.375
                not_determined_constant = False
            elif activity_measure == 3: 
                return 1.55
                not_determined_constant = False
            elif activity_measure == 4:
                return 1.725
                not_determined_constant = False
            # check a correct value has been input
            else: 
                print("Sorry I dont understand, choose between 1 and 4.")
                not_determined_constant = True 
        # Check an integer is being input. 
        except ValueError as v:
            print("Sorry, you didn't enter a number between 1 and 4.")
            not_determined_constant = True

def calculate_TDEE(TDEE_constant, REE):
    return TDEE_constant * REE


def maintenance_calories(user_data):

    age = user_data["Age"]
    sex = user_data["Sex"]
    weight = user_data["Weight"]
    height = user_data["Height"]

    REE = calculate_REE(sex, weight, height, age)
    activity_constant = determine_TDEE_constant(activity)
    TDEE = calculate_TDEE(activity_constant, REE)
    return f"Your maintenance calories are: {TDEE:.2f} calories"


