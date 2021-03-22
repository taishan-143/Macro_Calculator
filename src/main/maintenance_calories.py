
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

# input weight
weight = int(input("Please insert your weight to the nearest kg: "))
# input height 
height = float(input("Please insert your height in cm: "))
# input age
age = int(input("How old are you?: "))
# input sex
sex = input("Are you male or female?: ")

def calculate_REE(sex):
    if sex[0].lower() == 'm':
        male_REE(weight, height, age)
    elif sex[0].lower() == 'f':
        female_REE(weight, height, age)
    else:
        # elaborate on error checks!
        raise KeyError

def determine_TDEE_constant(activity):
    not_determined_constant = True 
    while not_determined_constant:
        activity_measure = int(input(activity))
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
        elif activity_measure < 0 and activity_measure > 4:
            print("Sorry I dont understand, choose between 1 and 4.")
            not_determined_constant = True 
        else:
            print("Sorry, you didn't enter a number between 1 and 4.")
            not_determined_constant = True

def calculate_TDEE(TDEE_constant, REE):
    return TDEE_constant * REE

