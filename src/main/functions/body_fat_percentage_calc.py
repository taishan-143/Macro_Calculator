from src.main.functions.math_methods import *

from conversion_data.young_men import *
from conversion_data.old_men import *
from conversion_data.young_women import *
from conversion_data.old_women import *

### Be more specific with measurement guides! 
# Print a message to the user if this calculator is selected.

def body_fat_percentage_new_calc(user_data):
    # define user sex and height
    sex = user_data["Sex"]
    height = user_data["Height"] * 0.393701 ### => conversion to inches
    # determine which equation applies to the user
    if sex[0].lower() == 'm':
        neck    = float(input("\nInput the measure of your neck (inches): "))
        abdomen = float(input("Input the measure of your abdomen (inches): "))
        body_fat_perc = male_body_fat_percentage(neck, abdomen, height)
        return round(body_fat_perc, 2)
    elif sex[0].lower() == 'f':
        neck = float(input("\nInput the measure of your neck (inches): "))
        waist = float(input("Input the measure of your waist (inches): "))
        hips = float(input("Input the measure of your hips (inches): "))
        body_fat_perc = female_body_fat_percentage(neck, waist, hips, height)
        return round(body_fat_perc, 2)
    else:
        raise KeyError