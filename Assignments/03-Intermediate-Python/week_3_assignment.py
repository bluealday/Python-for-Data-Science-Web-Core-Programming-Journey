#################################################
# ASSIGNMENT:                                   #
#################################################
# PROBLEM 1: Namespaces & Scopes                #
#################################################
# We would like to have an efficient way to perform foreign currency exchange conversions, with USD as the base currency and EUR (Euro), CAD (Canadian Dollar), GBP (British Pound),
# CHF (Swiss Frank), YEN (Japanese Yen), CNY (Chinese Yuan)..etc as the target currency.  There are multiple ways to do this.  One way would be to create one function to handle the conversion for each currency pair, but this would
# be a lot of repetitive coding.  Instead, I would like you to create one generic function named "create_currency_conversion_function()".  This function takes one float parameter (conversion_factor) and uses it to
# "manufacture" another inner function (which you can name it anything you like) that does the actual conversion for a given currency pair.  The inner function takes 1 float parameter which represents the USD ammount to be converted.
# For example, if I want to convert from 10 USD to CAD (assume current going rate is 1.00 USD = 1.25 CAD), this is how I can use the generic outer function:
# 
#   # First we call the generic function which creates and returns a function that does the actual USD to CAD conversion for us.  We will assign "usd_to_cad" as the identifier name for the returned function:
#   usd_to_cad = create_currency_conversion_function(conversion_factor=1.25)
# 
#   # Now we can perform the actual conversion by calling the created function using the identifier that we chose:
#   usd_to_cad(10.00) # this should evaluate to 12.5 CAD
# 
#   # Similarly, if we want to convert 100.00 USD to CNY (assume current going rate is 1.00 USD = 7.00 CNY):
#   usd_to_cny = create_currency_conversion_function(conversion_factor=7.00)
#   usd_to_cny(100.00) # this should evaluate to 700.00 CNY
# 
# Ensure your code is documented properly with comments and/or docstrings
# Use week_3_assignment_test.py file to test your work.  Import the function there along with the input data that goes with it (if any), and make calls to it to verify the results are correct.  Only submit week_3_assignment.py (do not submit week_3_assignment_test.py)
#################################################

def create_currency_conversion_function(conversion_factor):
    
    """
    Enclosing function that creates inner function convert_amount   

    Parameters:
    conversion_factor (float): factor used to convert one currency to another

    Returns:
    function: convert_amount
    """

    def convert_amount(amount):
        
        """
        Local/Inner function that returns the converted amount from one currency type to another 

        Parameters:
        amount (float): amount to be converted

        Returns:
        float
        """
	
        return amount * conversion_factor
    
    return convert_amount


#################################################
# ASSIGNMENT:                                   #
#################################################
# PROBLEM 2: Looping Techniques                 #
#################################################
# In the file "./input_data/week_3_assignments_data.py" you're given data for employee names and their annual sale numbers ("p2_employees_list" and "p2_sales_list")
# The "p2_employees_list" and "p2_sales_list" are index-locked..so the 1st sale number in the "p2_sales_list" list corresponds to the 1st employee in the "p2_employees_list" list...and so on.
# Write code for a function named "find_employees_with_highest_sales()" that accepts 3 parameters, "employees" (list of employee names), "sales" (list of annual sale numbers),
# and "number_of_employees" (a number).
# The function should find the number of employees (given by the argument "number_of_employees") with the highest annual sales and return a list comprised of tuples, each tuple containing 2 items,
# emplyee name and their annual sales number
# 
# Ensure your code is documented properly with comments and/or docstrings
# Use week_3_assignment_test.py file to test your work.  Import the function there along with the input data that goes with it (if any), and make calls to it to verify the results are correct.  Only submit week_3_assignment.py (do not submit week_3_assignment_test.py)
#################################################

def find_employees_with_highest_sales(employees, sales, number_of_employees):
    
    """
    Enclosing function creates inner function employee_to_sales and returns a list of tuples of employees and their higest sales numbers up to number of employees
	  

    Parameters:
    employees (list): list of employees
	sales (list): list of sales figures for employees
	number_of_employees (int): return data for this number of employees

    Returns:
    list of tuples: containing employees and sales
    """

    # since the employees and sales lists are index locked, create the appropriate dictionary 
    employees_to_sales_dict = dict(zip(employees, sales))

    def employee_to_sales(employee):
        """
        Local/Inner function that returns the sales figures for a given employee 

        Parameters:
        employee: employee name

        Returns:
        employee sales value
        """
        return employees_to_sales_dict[employee]

    # create a sorted list of employees based on their highest sales values
    # using the key value produced by the inner function employee_to_sales 
    employee_sorted_list = sorted(employees, key=employee_to_sales, reverse=True)

    # create a sorted list of sales values 
    sales_sorted_list = sorted(sales, reverse=True)
	
    # create the list of tuples
    result_tup_list = []

    # for each employee, sales pair up to the number of specified employees, add to the resulting list
    for employee_counter, (employee, sales) in enumerate(zip(employee_sorted_list, sales_sorted_list), start=1):
	    
        if employee_counter > number_of_employees:
            break

        result_tup_list.append((employee, sales))

    # retun the list of tuples
    return result_tup_list
