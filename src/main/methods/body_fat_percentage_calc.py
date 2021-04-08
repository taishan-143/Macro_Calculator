from src.main.methods.math_methods import *

from conversion_data.young_men import *
from conversion_data.old_men import *
from conversion_data.young_women import *
from conversion_data.old_women import *





### Be more specific with measurement guides! 
# Print a message to the user if this calculator is selected.

def body_fat_percentage_calculator(sex, age):

    if sex[0].lower() == "m":
        if age < 30: # young
            upper_arm = float(input("Input the measure your upper arm (inches): "))
            abdomen = float(input("Input the measure your abdomen (inches): "))
            forearm = float(input("Input the measure your forearm (inches): "))
            # linear regression here
            upper_arm_constant = constant_evaluation(YOUNG_UPPER_ARM_MEASURE, YOUNG_UPPER_ARM_CONSTANTS, upper_arm)
            abdomen_constant = constant_evaluation(YOUNG_ABDOMEN_MEASURE, YOUNG_ABDOMEN_CONSTANTS, abdomen)
            forearm_constant = constant_evaluation(YOUNG_FOREARM_MEASURE, YOUNG_FOREARM_CONSTANTS, forearm)
            # evaluate body fat percentage 
            BFP = body_fat_percentage(age, sex, upper_arm_constant, abdomen_constant, forearm_constant)
            return f"Your body fat percentage is {BFP:.2f}%."
        else: # old 
            buttocks = float(input("Input the measure your buttocks (inches): "))
            abdomen = float(input("Input the measure of your abdomen (inches): "))
            forearm = float(input("Input the measure of your forearm (inches): "))
            # linear regression here
            buttocks_constant = constant_evaluation(OLD_BUTTOCKS_MEASURE, OLD_BUTTOCKS_CONSTANTS, buttocks)
            abdomen_constant = constant_evaluation(OLD_ABDOMEN_MEASURE, OLD_ABDOMEN_CONSTANTS, abdomen)
            forearm_constant = constant_evaluation(OLD_FOREARM_MEASURE, OLD_FOREARM_CONSTANTS, forearm)
            # evaluate body fat percentage 
            BFP = body_fat_percentage(age, sex, buttocks_constant, abdomen_constant, forearm_constant)
            return f"Your body fat percentage is {BFP:.2f}%."
    elif sex[0].lower() == "f":
        if age < 30: # young 
            abdomen = float(input("Input the measure your abdomen (inches): "))
            thigh = float(input("Input the measure your thigh (inches): "))
            forearm = float(input("Input the measure your forearm (inches): "))
            # linear regression here
            abdomen_constant = constant_evaluation(ABDOMEN_MEASURE_YW, ABDOMEN_CONSTANTS_YW, abdomen)
            thigh_constant = constant_evaluation(THIGH_MEASURE_YW, THIGH_CONSTANTS_YW, thigh)
            forearm_constant = constant_evaluation(FOREARM_MEASURE_YW, FOREARM_CONSTANTS_YW, forearm)
            # evaluate body fat percentage 
            BFP = body_fat_percentage(age, sex, abdomen_constant, thigh_constant, forearm_constant)
            return f"Your body fat percentage is {BFP:.2f}%."
        else: # old
            abdomen = float(input("Input the measure your abdomen (inches): "))
            thigh = float(input("Input the measure your thigh (inches): "))
            forearm = float(input("Input the measure your forearm (inches): "))
            # linear regression here
            abdomen_constant = constant_evaluation(ABDOMEN_MEASURE_OW, ABDOMEN_CONSTANTS_OW, abdomen)
            thigh_constant = constant_evaluation(THIGH_MEASURE_OW, THIGH_CONSTANTS_OW, thigh)
            forearm_constant = constant_evaluation(FOREARM_MEASURE_OW, FOREARM_CONSTANTS_OW, forearm)
            # evaluate body fat percentage 
            BFP = body_fat_percentage(age, sex, abdomen_constant, thigh_constant, forearm_constant)
            return f"Your body fat percentage is {BFP:.2f}%."
    else:
        raise KeyError

