import week_5_assignment as w5a
# import input_data.week_5_assignments_data as data_in


# PROBLEM 1: Object-Oriented Programming - Part 1
#################################################
# Instantiate a new "YellowPagesParser" object:
my_yellow_pages_parser = w5a.YellowPagesParser("./course_2_intermediate_python/week_5/assignments/input_data/yellow_pages.txt")

# Parse entire yellow pages and write all 100 business entries to a csv file:
my_yellow_pages_parser.to_csv(my_yellow_pages_parser.yellow_pages_tbl, "./course_2_intermediate_python/week_5/assignments/output_data/yellow_pages.csv")

# Look for attorney businesses with no websites in zip 32501 or aread code 954. Write results to csv files:
# zip 32501:
zip_23501_list = my_yellow_pages_parser.yellow_pages_tbl_filter_by(category="attorneys", website='', address_zip="32501")
my_yellow_pages_parser.to_csv(zip_23501_list, "./course_2_intermediate_python/week_5/assignments/output_data/yellow_pages_attorneys_no_website_zip_32501.csv")  

# area code 954
area_code_954_list = my_yellow_pages_parser.yellow_pages_tbl_filter_by(category="attorneys", website='', phone_area_code="954")
my_yellow_pages_parser.to_csv(area_code_954_list, "./course_2_intermediate_python/week_5/assignments/output_data/yellow_pages_attorneys_no_website_area_code_954.csv")      

any_list = my_yellow_pages_parser.yellow_pages_tbl_filter_by()
my_yellow_pages_parser.to_csv(any_list, "./course_2_intermediate_python/week_5/assignments/output_data/yellow_pages_everything_any.csv")      