#################################################
# ASSIGNMENT:                                   #
#################################################
# PROBLEM 1: String Formatting                  #
#################################################
# Binary data (True/False or 1/0) can be used to designate that a particular option or setting is present (True/1) or not (False/0).  Let's take this practical example. a manufacturer that sells RC toy cars,
# gives its customers 8 possible add-on options that they can add when making an order.  These options could anything like bigger wheels, stronger motor, larger antenna...etc
# When a customer places an order, the add-on options are captured as binary True/False (1/0) values.  So an order that has 4 add-on options chosen would have the the add-on's represented as 00001111, while an order with all 8 add-on's
# chosen would have the add-on's reprsented as 11111111.  To save memory, the manufacture's backend systems store the add-on value as a number ranging from 0-255 (with 8 bits, one can store positive numbers from 0 up to 255).
# The manufacture is interested in analyzing past order data to see how many orders have 0,1,2...up to 8 add-ons associated with them.  For the two edge cases, that is 0 add-on's and 8 add-on's, this is fairly easy..all that is needed is to
# check if the add-on value is equal to 0 and 255, respectively.  But for the rest of the cases this may not be very intuitive.
# Complete the code for the function below "get_number_of_add_ons()" which should take in a positive integer as an argument and return the total number of add-ons represented by that integer.  
#################################################

def get_number_of_add_ons(add_on_int):
    """
    returns number of add-ons by determining the number of bits set to 1 in the parameter add_on_int

    Parameters:
    add_on_int (int): A positive integer

    Returns:
    int: Number of add-ons
    """
    
    # Replace ? in the line below with the correct string format specification to convert from decimal to a binary format.  Refer to the documentation here: https://docs.python.org/3/library/string.html#format-specification-mini-language
    
    ## based on the link above, use 0b to convert value to binary
    
    add_on_str = f"{add_on_int:0b}"
    
    number_of_add_ons = add_on_str.count('1')
    return number_of_add_ons

#################################################
# ASSIGNMENT:                                   #
#################################################
# PROBLEM 2: Debugging                          #
#################################################
# You work for a company that manufactures drills.  The company recently discovered a severe quality issues in some of its drills and decided to launch a re-call campaign for the affected products that were sold 1 year ago.
# The company sells several drill models, but only those that have an electric current rating of 30 Amperes are targeted in the re-call campaign.  You were given data of all drills that were purchased by customers covering the 1-year period.
# The data includes all purchased drills of all models made, and you were asked to filter the data to find only the serial numbers of the affected drill models.  The problem with the data is that it doesn't include the electric current rating of the drills.
# (The data is given as a python list named "p2_purchased_drills_list" in the file "./input_data/week_1_assignments_data.py")
# Instead of electric current, it includes the Power Rating and Operating Voltage (as well as the Serial Number).  One can back-calculate the electric current from power and voltage using the formula:
# I = P / V , where P is Power in Watts, and V is Voltage in Volts
# So you wrote the function below which should return a list containing the affected s/n's..but when you ran it, you got zero matches!  You know for certian this can't be the case, since you yourself have purchased one drill last year that has a current rating of 30 A
# Therefore, you expect a minimum of one match.  You've also verified that the s/n of the drill you purchased is present in the data (s/n: 198300001)
# Debug the code in the function below, find_recall_serial_number(), find out where the issue is, & correct it
#################################################

def find_recall_serial_number(purchased_drills_list, recall_current_rating):
    """
    Finds serial numers of products that have a specific current rating

    Parameters:
    purchased_drills_list (list): This should be a list that containts nested lists in it.  Each nested list should contain 3 products' data:
        1. (int): Product's Power Rating in Watts
        2. (int): Prodcut's Operating Voltage in Volts
        3. (str): Product's Serial Number
    recall_current_rating (int or float): Current Rating in Amperes for which the re-call campaign is targeting

    Returns:
    list: Contains serial numbers (str) of found product(s) that have a current rating that matches recall_current_rating
    """

    # Create an empty list that will store the serial numbers of any found sold products that have the current rating targeted by the campaign
    serial_number_to_recall_list = []

    # Loop through all the products, back-calculate each product's current rating using the formual Current = Power / Voltage, 
    # and see if calculated current matches recall_current_rating.  If so, add found product's serial number to serial_number_to_recall_list
    
    ## bug exists when product_current_rating is a float but recall_current_rating can be an int
    ## fixed by changing "is" to "==" and converting recall_current_rating to a float

    ## also change format of SN to include only number so print statement does not repeat "product with s/n s/n:"
    for product in purchased_drills_list:
        product_current_rating = product[0] / product[1]
        if product_current_rating == float(recall_current_rating):
            serial_number_to_recall_list.append(product[2].split()[1])
    
    # return the list of products that should be re-called
    return serial_number_to_recall_list