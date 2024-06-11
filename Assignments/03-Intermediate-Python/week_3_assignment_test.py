import week_3_assignment as w3a
import input_data.week_3_assignments_data as data_in


# PROBLEM 1: Namespaces & Scopes
#################################################
# First we call the generic function which creates and returns the functions that do the actual USD to XXX conversion for us.  We will assign "usd_to_xxx" as the identifier name for the returned functions:
usd_to_cad = w3a.create_currency_conversion_function(conversion_factor=1.25)
usd_to_cny = w3a.create_currency_conversion_function(conversion_factor=7.00)

# Pick a USD amount to be converted:
usd_to_cad_conversion_amt = 10.00
usd_to_cny_conversion_amt = 100.00

# Perform and print the conversion results using fixed point presentation with 2 digits after the decimal point and '0' as the backfill character:
print(f"{usd_to_cad_conversion_amt:.02f} USD = {usd_to_cad(usd_to_cad_conversion_amt):.02f} CAD") # The answer should be "12.5 CAD"
print(f"{usd_to_cny_conversion_amt:.02f} USD = {usd_to_cny(usd_to_cny_conversion_amt):.02f} CNY") # The answer should be "700.00 CNY"
print()






# PROBLEM 2: Looping Techniques
#################################################
# Show top 3 best performing employees along with their annual sales numbers
for name, sale in w3a.find_employees_with_highest_sales(data_in.p2_employees_list, data_in.p2_sales_list, number_of_employees=50):
    print(name, sale)