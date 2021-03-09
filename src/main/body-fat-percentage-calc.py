import src.main.math_methods
import conversion_data

### Calc logic placed here
# while loop to keep running
# take measurement inputs from user 
# return body fat percentage 


# input name
full_name = input("Enter your first and last name: ")
# input age
age = int(input("Enter your age: "))
# input sex
sex = input("Are you male or female?: ")

## check against data to determine correct measurements to take
# ask for required measurements e.g:
# - input buttocks
# - input abdomen
# - input forearm 

### be more specific with measurement guides!
if sex[0] == "m":
    if age < 30: # young
        upper_arm = input("Input the measure your upper arm (inches): ")
        abdomen = input("Input the measure your abdomen (inches): ")
        forearm = input("Input the measure your forearm (inches): ")
        # linear regression function here
        UPPER_ARM_CONSTANT = LinearRegressionModel(conversion_data.young_men.UPPER_ARM_MEASURE, conversion_data.young_men.UPPER_ARM_CONSTANTS, upper_arm)
        print(UPPER_ARM_CONSTANT)
    else: # old 
        buttocks = input("Input the measure your buttocks (inches): ")
        abdomen = input("Input the measure of your abdomen (inches): ")
        forearm = input("Input the measure of your forearm (inches): ")
        # linear regression function here
elif sex[0] == "f":
    if age < 30: # young 
        abdomen = input("Input the measure your abdomen (inches): ")
        thigh = input("Input the measure your thigh (inches): ")
        forearm = input("Input the measure your forearm (inches): ")
        # linear regression function here
    else: # old
        abdomen = input("Input the measure your abdomen (inches): ")
        thigh = input("Input the measure your thigh (inches): ")
        forearm = input("Input the measure your forearm (inches): ")
        # linear regression function here
else:
    raise KeyError


# calculate body fat percentage 