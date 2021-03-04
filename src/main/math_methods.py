import decimal

def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += float(decimal.Decimal(step))


# def max_values(measurement, measurement_dictionary):
#   absolute_difference = lambda list_value : abs(list_value - measurement)
#   RHS_Measure = max(measurement_dictionary.keys(), key = absolute_difference)
#   RHS_Constant = measurement_dictionary[RHS_Measure]
#   return {RHS_Measure:RHS_Constant}
# ### refactor max and min functs into 1 funct.
# def min_values(measurement, measurement_dictionary):
#   absolute_difference = lambda list_value : abs(list_value - measurement)
#   LHS_Measure = min(measurement_dictionary.keys(), key = absolute_difference) 
#   LHS_Constant = measurement_dictionary[LHS_Measure]
#   return {LHS_Measure:LHS_Constant}

# def interpolate(measurement, upper_measure, lower_measure, upper_of_result, lower_of_result):
#   return lower_of_result + (measurement - lower_measure)*((upper_of_result - lower_of_result)/(upper_measure-lower_measure))


# def interpolater(measurement, measurement_dictionary):
#   # check if measurement is in measurement list
#   if measurement in measurement_dictionary.keys():
#     return measurement_dictionary[measurement]
#   # - if yes, return constant
#   # - if no, find the values in the list before and after the measurement
#   else:
#     Max_Values = max_values(measurement, measurement_dictionary)
#     Min_Values = min_values(measurement, measurement_dictionary)
#     return interpolate(measurement, Max_Values.keys(), Min_Values.keys(), Max_Values.values(), Min_Values.values())
#   #   then get the corresponding constants 
#   #   then interpolate to find constant value 


"""RESEARCH LINEAR REGRESSION"""