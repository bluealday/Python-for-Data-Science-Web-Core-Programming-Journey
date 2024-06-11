import week_6_assignment_ver2 as w6a
# import input_data.week_6_assignments_data as data_in


# PROBLEM 1: Object-Oriented Programming - Part 2
#################################################
# Instantiate parser objects:
my_white_pages_parser = w6a.WhitePagesParser("./course_2_intermediate_python/week_6/assignments/input_data/white_pages.txt")
my_yellow_pages_parser = w6a.YellowPagesParser("./course_2_intermediate_python/week_6/assignments/input_data/yellow_pages.txt")
my_company_pages_parser = w6a.CompanyPagesParser("./course_2_intermediate_python/week_6/assignments/input_data/company_pages.txt")

# Parse entire all 3 pages text files and write all 100/20/20 records to csv files:
my_white_pages_parser.to_csv(my_white_pages_parser.pages_tbl, "./course_2_intermediate_python/week_6/assignments/output_data/white_pages.csv")
my_yellow_pages_parser.to_csv(my_yellow_pages_parser.pages_tbl, "./course_2_intermediate_python/week_6/assignments/output_data/yellow_pages.csv")
my_company_pages_parser.to_csv(my_company_pages_parser.pages_tbl, "./course_2_intermediate_python/week_6/assignments/output_data/company_pages.csv")

# Look for employees with the title "Software Engineer" in the company pages.  Write results to csv files:
title_software_engineer_list = my_company_pages_parser.pages_tbl_filter_by(title="software engineer")
my_company_pages_parser.to_csv(title_software_engineer_list, "./course_2_intermediate_python/week_6/assignments/output_data/company_pages_titles_software_engineer.csv")  

# Look for employees with the organization "SecureNet Innovations" in the company pages.  Write results to csv files:
organization_securenet_innovations_list = my_company_pages_parser.pages_tbl_filter_by(organization="SecureNEt INNovations")
my_company_pages_parser.to_csv(organization_securenet_innovations_list, "./course_2_intermediate_python/week_6/assignments/output_data/company_pages_organizations_securenet_innovations.csv")  
