#################################################
# ASSIGNMENT:                                   #
#################################################
# PROBLEM 1: Functions                          #
#################################################
# For this problem you are tasked to complete the code below for a function named "convert", which converts a measurement from one unit to another.  The function has these 4 parameters:
#   value: this is the numerical value to be converted
#   from_unit: this is the unit for the "value" parameter from which the conversion is to be done
#   to_unit: this is the target unit for the conversion
#   category: this instructs the function which measurement category for which the conversion is requested.  3 categories are supported: "length", "weight" and "speed"
# For example, to convert 10 kg to xx lb, the function would be called like this:
#   convert(value=10.0, from_unit="kilogram", to_unit="pound", category="weight")
# 
# Another example, to convert 5 miles to xx km, the function would be called like this:
#   convert(value=5.0, from_unit="mile", to_unit="kilometer", category="length")
# 
# All the supported categories along with the units and their base conversions are provided in a dictionary called "categories_and_base_conversions".
# This dictionary contains 3 sub-dictionaries, each for one of the three supported categories ("length", "weight" and "speed").
# When the "convert" function is called, the arguments passed for "category", "from_unit" and "to_unit" must be keys in the "categories_and_base_conversions"
# 
# The approach to do the unit conversion involves these two steps:
#   Step 1: Calculate the conversion factor
#       For example, if we are converting from lb to oz, the conversion factor is 16 (1 lb is 16 oz)
#   Step 2: Finish the conversion
#       multiply the value to be converted by the conversion factor
#   To obtain the conversion factor, you can look up the base conversion numbers in the provided "categories_and_base_conversions" dictionary.
#   The conversion factor is obtained by dividing the number of the "from_unit" over the number of the "to_unit".  In the lb to oz scenaior, this would be 453.592/28.3495=16
# 
# Other requirement(s):
#   - if "convert" function is called w/o passing "category" argument, it should be assumed to be "weight"
# 
# Ensure your code is documented properly with comments and/or docstrings
# Use week_2_assignment_test.py file to test your work.  Import the function there along with the input data that goes with it (if any), and make calls to it to verify the results are correct.  Only submit week_2_assignment.py (do not submit week_2_assignment_test.py)
#################################################

# Define a dictionary of categories and their corresponding units and conversion factors
categories_and_base_conversions = {
    "length": {
        "meter": 1,
        "centimeter": 0.01,
        "kilometer": 1000,
        "inch": 0.0254,
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.34
    },
    "weight": {
        "gram": 1,
        "kilogram": 1000,
        "tonne": 1000000,
        "ounce": 28.3495,
        "pound": 453.592,
        "stone": 6350.29
    },
    "speed": {
        "meter per second": 1,
        "kilometer per hour": 0.277778,
        "mile per hour": 0.44704,
        "knot": 0.514444
    }
}


def convert(value, from_unit, to_unit, category="weight"):

    """
    Convert one measurement to another.

    Parameters:
    value (float): Numerical value to be converted
    from_unit (str): Unit for the "value" parameter from which the conversion is to be done
    to_unit (str): Target unit for the conversion
    category (str): Measurement category for which the conversion is requested

    Returns:
    float: Converted value
    """

    # get the subcategories from the dictionary based on the category passed to retrieve the from_unit and to_unit values using a nested get
    # there is no error checking as it assumes that the user entered the correct keys from the dictionary when the function is called
    
    from_unit_value = (categories_and_base_conversions.get(category)).get(from_unit)
    to_unit_value = (categories_and_base_conversions.get(category)).get(to_unit)
    
    # calculate the conversion factor
    conversion_factor = from_unit_value / to_unit_value

    # calculate the converted value and return it
    converted_value = value * conversion_factor

    return(converted_value)
        

#################################################
# ASSIGNMENT:                                   #
#################################################
# PROBLEM 2: Command-Line Interface             #
#################################################
# Use argparse module to provide command-line interface capability to this code file.  Goal is to be able to execute this python file as a stand-alone program and pass to it arguments to request unit conversion
# Add code directly before and after the "convert" function above in problem 1 (i.e do not create another "convert" function just for this problem.  Use the function already coded in problem 1)
# 
# Requirements:
#   - Command-line arguments to be supported (use exact names):
#       1. "value" -> float -> positional argument
#       2. "from_unit" -> str -> positional argument
#       3. "to_unit" -> str -> positional argument
#       4. "--category" (with short-hand version "-c") -> str -> optional argument -> default= "weight"
#   - Program should print out the conversion result in fixed point with 2 digits precision (example of the printed text: "1.0 pound is equal to 16.00 ounce")
#   - Add help documentation string to each command-line argument above
# 
# Ensure your code is documented properly with comments and/or docstrings
# Test your work by directly executing this file from the OS shell (Command Prompt in Windows).  Pass various command-line arguments and verify results are correct
#################################################

import argparse

#create parser object
parser = argparse.ArgumentParser()

# add arguments as described above
# any arguments that are strings won't need a type declaration per the lectures

parser.add_argument("value", type=float, help="This is the numerical value to be converted")
parser.add_argument("from_unit", help="Unit for the 'value' parameter from which the conversion is to be done")
parser.add_argument("to_unit", help="Target unit for the conversion")
parser.add_argument("-c", "--category", default="weight", help="Measurement category for which the conversion is requested")

# declare the global variable 'args'
args = parser.parse_args()

# test the code using command line arguments and printing out the result, with the value set to 2 decimal places
# user must know to pass the correct values as there is no error checking

print(f"{args.value} {args.from_unit}(s) to {args.to_unit}(s) ->", f"{convert(args.value, args.from_unit, args.to_unit, args.category):.2f}")

