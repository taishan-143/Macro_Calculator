import numpy as np

### Be more specific with measurement guides! 
# Print a message to the user if this calculator is selected.

# male and female body fat percentage equations 
def male_body_fat_percentage(neck, abdomen, height):
  return (86.010 * np.log10(abdomen - neck)) - (70.041 * np.log10(height)) + 36.76

def female_body_fat_percentage(neck, waist, hips, height):
  return (163.205 * np.log10(waist + hips - neck)) - (97.684 * np.log10(height)) - 78.387


def body_fat_percentage_calc(user_data):
    # define user sex and height
    sex = user_data["Sex"]
    height = user_data["Height"] * 0.393701 ### => conversion to inches
    # determine which equation applies to the user
    try:
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
    except KeyError:
      print("That is an unspecified sex.")
          