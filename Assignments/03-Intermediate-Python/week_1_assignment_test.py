import week_1_assignment as w1a
import input_data.week_1_assignments_data as data_in


# PROBLEM 1: String Formatting
#################################################
print("number of add-ons:", w1a.get_number_of_add_ons(170))

#edge cases
print("number of add-ons:", w1a.get_number_of_add_ons(0))
print("number of add-ons:", w1a.get_number_of_add_ons(255))

# bits are all 1
print("number of add-ons:", w1a.get_number_of_add_ons(1))
print("number of add-ons:", w1a.get_number_of_add_ons(3))
print("number of add-ons:", w1a.get_number_of_add_ons(7))
print("number of add-ons:", w1a.get_number_of_add_ons(15))
print("number of add-ons:", w1a.get_number_of_add_ons(31))
print("number of add-ons:", w1a.get_number_of_add_ons(95))
print("number of add-ons:", w1a.get_number_of_add_ons(223))


# PROBLEM 2: Debugging
#################################################
print("s/n's of products to be re-called:")
for sn in w1a.find_recall_serial_number(data_in.p2_purchased_drills_list, 20.0):
    print(f"product with s/n {sn} must be re-called")