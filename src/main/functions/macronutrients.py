# Ask user if they're bulking or cutting
# Let user choose protein and fat ratio's, then calculate carb ratio. GIVE EXAMPLES 
# Return their macro's according to their preference 
#  - take maintenance calories
#  - divide by macro's:
#    - 4 cals per gram of protein
#    - 4 cals per gram of carbs
#    - 9 cals per gram of fat 

def new_caloric_intake(preference, maintenance_calories):
    
    if preference == 'bulking':
        word = 'bulk'
    else:
        word = 'cut'

    not_calculated_new_intake = True
    while not_calculated_new_intake:
        try:
            percentage = int(input(f"What percentage would you like to {word} by? (0 - 100): "))
            if percentage < 0 or percentage > 100:
                print("Your choice is out of range, try again")
                not_calculated_new_intake = True
            else:
                new_calorie_intake = maintenance_calories * (1 - percentage/100)
                return new_calorie_intake
                not_calculated_new_intake = False
        except ValueError as v:
            print("\nThat isn't a number, try again.")


# Choice for percentage of protein intake
def protein_choice():
    not_chosen_protein_percentage = True
    while not_chosen_protein_percentage:
        protein = int(input("\nWhat percentage of protein do you want? (0 - 100): "))
        if protein <= 0 or protein > 100:
            print("\nYou're out of range, try again.")
            not_chosen_protein_percentage = True
        else:
            return protein
            not_chosen_protein_percentage = False

# Choice for percentage of fat intake, reliant on protein choice.
def fat_choice(protein):
    not_chosen_fat_percentage = True
    while not_chosen_fat_percentage:
        fat = int(input("What percentage of fat do you want? (0 - 100): "))
        if fat <= 0 or fat > (100 - protein):
            print("\nYou're out of range, try again.")
            not_chosen_fat_percentage = True
        else:
            return fat
            not_chosen_fat_percentage = False
            

# Final calculation of macronutrients.
def macronutrient_ratios(new_caloric_intake):
    not_chosen_macro_preferences = True
    while not_chosen_macro_preferences:
        try:
            # percentages 
            protein = protein_choice()
            fat = fat_choice(protein)
            carbs = 100 - (protein + fat)
 
            protein_cals = new_caloric_intake * (protein/100) # convert percentages to decimals for calculation.
            fat_cals = new_caloric_intake * (fat/100)
            carb_cals = new_caloric_intake - (protein_cals + fat_cals)

            protein_in_grams = protein_cals / 4 # 4 cals of protein per gram
            fat_in_grams = fat_cals / 9 # 9 cals of fat per gram
            carbs_in_grams = carb_cals / 4 # 4 cals of carbs per gram

            return f"""\nDaily macronutrients based on your dietary preference:
        Protein: {protein_in_grams:.2f}g ({protein}%)
        Fat: {fat_in_grams:.2f}g ({fat}%)
        Carbohydrates: {carbs_in_grams:.2f}g ({carbs}%)
            """
        except ValueError as v:
            print("\nThat isn't a number, try again.")




