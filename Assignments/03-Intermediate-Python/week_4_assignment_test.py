import week_4_assignment as w4a
import input_data.week_4_assignments_data as data_in


# PROBLEM 1: Generators
#################################################
# Call book_autograph and pass to it the book text, the generic autograph message and the list of readers for which we wish to created the personalized autographed full version of the book based on their desired language:
for autographed_book in w4a.book_autograph(data_in.p1_full_book_text, data_in.p1_autograph_message, data_in.p1_readers_info):
    print(autographed_book)





# PROBLEM 2: Regular Expressions
#################################################
# Call "read_file()" function which will populate the global list YELLOW_PAGES_LINES_LIST with all the lines of the yellow pages file
w4a.read_file("./course_2_intermediate_python/week_4/assignments/input_data/yellow_pages.txt")

# Parse all business names
business_names = w4a.parse_all_names()
print("Business Names" + "\n")
print(business_names)
print("\n\n")

# Parse all business addresses
business_addresses = w4a.parse_all_addresses()
print("Business Address" + "\n")
print(business_addresses)
print("\n\n")

# Parse all business phones
business_phones = w4a.parse_all_phones()
print("Business Phones" + "\n")
print(business_phones)
print("\n\n")

# Parse all business emails
business_emails = w4a.parse_all_emails()
print("Business Emails" + "\n")
print(business_emails)
print("\n\n")
# Parse all business websites
business_websites = w4a.parse_all_urls()
print("Business Websites" + "\n")
print(business_websites)
print("\n\n")

# Parse all business categories
business_categories = w4a.parse_all_categories()
print("Business Categories" + "\n")
print(business_categories)
print("\n\n")

# Re-print the entire yellow pages
for name, addr, phone, email, web, category in zip(business_names, business_addresses, business_phones, business_emails, business_websites, business_categories):
  print(f"name: {name}")
  print(f"address: {addr[0]} {addr[1]} - {addr[2]}, {addr[3]} {addr[4]}")
  print(f"phone: ({phone[0]}) {phone[1]}")
  print(f"email: {email}")
  print(f"website: {web}")
  print(f"category: {category}")
  print()
