#################################################
# ASSIGNMENT:                                   #
#################################################
# PROBLEM 1: Object-Oriented Programming - Part1#
#################################################
# For the class in this week's exercise, "YellowPagesParser", add these 2 methods:
# 
# .yellow_pages_tbl():
#   - Method would return all businesses data in a list.  The list will have records for all businesses organized like a table, with each row representing data for one entire business.
#     This is method should achieve this by executing all the 6 parse_all_xxx() methods and use returned data to populate a private instance attribute, named "._yellow_pages_tbl", which is going to be a list that contains all the parsed yellow pages data.  Inside this list, the data will be organized in tuples.
#     For example, the 1st tuple would correspond to the data of the 1st business in the yellow pages file ("Miami Plumbing experts").  This 1st tuple would contain all 6 field data for a this single business, with the sub data for address (and phone) stored also as items inside an inner tuple.  This is how the 1st business record item in "._yellow_pages_tbl" should look like:
#       
#       ("Miami Plumbing Experts", ("1234", "Coral Way", "Miami", "FL", "33145"), ("305", "555-1111"), "contact@miamiplumbingexperts.com", "https://www.miamiplumbingexperts.com/search?q=query+term&sort=asc", "plumbers")
# 
#   - The class initialization method should initialize the instance attribute "._yellow_pages_tbl" to an empty list, while this method, ".yellow_pages_tbl()", should only attempt to populate the attribute "._yellow_pages_tbl" if it is still an empty list (i.e. no need to waste time by re-running the 6 parsing methods if this was already done once before)
#   - This method should return the private instance attribute "._yellow_pages_tbl".  It should be set up to work at a "getter" so that if an object of this class attempts to access the attribute like this:
#     
#       "some_yellow_pages_class_object.yellow_pages_tbl"
#
#     then the ".yellow_pages_tbl()" method would execute
# 
# 
#   .yellow_pages_tbl_filter_by():
#     - Method would return records data that match the "filter by" criteria provided as arguments to this method.  The method accepts 11 parameters corresponding to all field data in the yellow pages file (parameter names already provided for you in the method's signature).
#     - The data returned should be in a list.  The format is identical to the data in the method above.
#     - All "filter by" criteria must match for a given record to be deemed as a match (if the request is to find businesses with address_zip=x, category=y, address_area_code=z, then all 3 must be found in a record for it to be considered a match).  When a record is matched, all its 11 data fields should be returned as part of the output of this method.
#     - A simple equality check (i.e. "==") should be used to determine if there's a match.  However, comparison should be case-insensitive (be sure to apply string .lower() method to any two strings being compared for equality)
#     - Every parameter of this method must have a default value of "any", which means that it shouldn't be considered in finding matching records if no explicit value is passed in the call (this also means that if none of the 11 parameters receive any arguments, the returned list should match exactly the list returned by the method above i.e. all 100 records in the yellow pages should be returned).
# 
# Test both methods above in the assignment test file (week_5_assignment_test.py) by passing their returned lists to the method ".to_csv()", which will save the passed data to a .csv file (you will specify the path/directory for where you want the .csv file to be saved at).  This method is already coded for you.  Read its docstring to understand how to call it
# Let's assume you want to approach businesses with no websites and offer to build one for them.  Your strategy is to target clients that are high-paying close to your local area.
# So, search for attorney businesses that have no website in your local area.  Assume local area to you means zip code "32501" or phone area code of "954" (so do 2 separate searches one for the zip code and the other for the phone area code).
# What are the businsess that you've found?  No need to turn in any answers for these questions but keep what you find in mind as we will try to re-visit this task using a different technique in a subsequent week. 
# 
# Ensure your code is documented properly with comments and/or docstrings
# Use week_5_assignment_test.py file to test your work.  Import the class there, and create object(s) from it while providing the path for the yellow pages text file in the "input_data" directory.  Test the 2 methods above and verify the results are correct.  Only submit week_5_assignment.py (do not submit week_5_assignment_test.py)
#################################################

import re, csv

class YellowPagesParser:
  """
  Class that parses data from yellow pages text files and stores them into lists
  """

  def __init__(self, yellow_pages_path):
    """
    Initialization method that reads the yellow pages text file and stores its lines in the instance attribute list .yellow_pages_lines_list

    Parameters:
    yellow_pages_path (str): path to text file to be read

    returns:
    None
    This method however will append the lines of the text file to the instance attribute list .yellow_pages_lines_list
    """

    # Attribute to hold parsed yellow pages data in tabulated format.  This will be an outer list that engulfs all the data, with each row representing all the data for one business.  Initialized to empty list for now
    self._yellow_pages_tbl = []
    
    # Attribute list that will be used to store the yellow pages text file, each item represents one line of the file
    self.yellow_pages_lines_list = []

    # Open the yellow pages text file, read its content line-by-line, and store each line as an item in the attribute yellow_pages_lines_list
    with open(yellow_pages_path) as yellow_pages_file_obj:
      self.yellow_pages_lines_list = [line for line in yellow_pages_file_obj.readlines()]


  def parse_all_names(self):
    """
    Returns all businesses' names

    Parameters:
    None

    returns:
    list: All businesses' names
    """

    # Create the list that'll store all business names
    names_list = []

    # Loop through each line of the yellow pages file
    for line in self.yellow_pages_lines_list:

      # Check if the line is the "name" line
      if line.startswith("name: "):

        # Search for the name pattern using regex
        regex_result = re.findall(r"name: (.+)", line)

        # If match found, append the found name to "names_list"
        if regex_result:
          names_list.append(regex_result[0])
        
        # If no match, append empty string
        else:
          names_list.append('')

    # Return "names_list"
    return names_list

  def parse_all_addresses(self):
    """
    Returns all businesses' addresses, with each address broken into a tuple consisting of (Street Number, Street Name, City, State, Zip)

    Parameters:
    None

    returns:
    list: All businesses' websites.  Each address is captured in a tuple that consists of (Street Number, Street Name, City, State, Zip)
    """

    # Create the list that'll store all business addresses
    addresses_list = []

    # Loop through each line of the yellow pages file
    for line in self.yellow_pages_lines_list:

      # Check if the line is the "address" line
      if line.startswith("address: "):

        # Search for the address pattern using regex
        regex_result = re.findall(r"address: (\d+) ([A-Za-z ]+) - ([A-Za-z ]+), ([A-Z]{2}) (\d{5})", line)

        # If match found, append the found address to "addresses_list"
        if regex_result:
          addresses_list.append(regex_result[0])

        # If no match, append empty string
        else:
          addresses_list.append('')

    # Return "addresses_list"
    return addresses_list


  def parse_all_phones(self):
    """
    Returns all businesses' phone numbers

    Parameters:
    None

    returns:
    list: all businesses' phone numbers
    """

    # Create the list that'll store all business phone numbers
    phones_list = []

    # Loop through each line of the yellow pages file
    for line in self.yellow_pages_lines_list:

      # Check if the line is the "phone" line
      if line.startswith("phone: "):

        # Search for the phone number pattern using regex
        regex_result = re.findall(r"phone: \((\d{3})\) (\d{3}-\d{4})", line)

        # If match found, append the found phone number to "phones_list"
        if regex_result:
          phones_list.append(regex_result[0])
        
        # If no match, append empty string
        else:
          phones_list.append('')

    # Return "phones_list"
    return phones_list

  def parse_all_emails(self):
    """
    Returns all businesses' emails

    Parameters:
    None

    returns:
    list: All businesses' emails
    """

    # Create the list that'll store all business emails
    emails_list = []

    # Loop through each line of the yellow pages file
    for line in self.yellow_pages_lines_list:

      # Check if the line is the "email" line
      if line.startswith("email: "):

        # Search for the email pattern using regex
        regex_result = re.findall(r"email: (\S+@\S+\.\S+)", line)

        # If match found, append the found email to "emails_list"
        if regex_result:
          emails_list.append(regex_result[0])
        
        # If no match, append empty string
        else:
          emails_list.append('')

    # Return "emails_list"
    return emails_list
    

  def parse_all_urls(self):
    """
    Returns urls for all businesses' websites

    Parameters:
    None

    returns:
    list: URLs for all businesses' websites
    """

    # Create the list that'll store all found URLs
    urls_list = []

    # Loop through each line of the yellow pages file
    for line in self.yellow_pages_lines_list:

      # Check if the line is the "website" line
      if line.startswith("website: "):

        # Search for the URL pattern using regex
        regex_result = re.findall(r"website: (https?://www\.\S+)", line)

        # If match found, append the found URL to "urls_list"
        if regex_result:
          urls_list.append(regex_result[0])
        
        # If no match, append empty string
        else:
          urls_list.append('')

    # Return "urls_list"
    return urls_list
  

  def parse_all_categories(self):
    """
    Returns all businesses' categories

    Parameters:
    None

    returns:
    list: Categories for all businesses
    """

    # Create the list that'll store all business categories
    categories_list = []

    # Loop through each line of the yellow pages file
    for line in self.yellow_pages_lines_list:

      # Check if the line is the "category" line
      if line.startswith("category: "):

        # Search for the category pattern using regex
        regex_result = re.findall(r"category: ([a-z]+)", line)

        # If match found, append the found category to "categories_list"
        if regex_result:
          categories_list.append(regex_result[0])
        
        # If no match, append empty string
        else:
          categories_list.append('')
        
    # Return "categories_list"
    return categories_list

  
  def to_csv(self, tbl_data, yellow_pages_csv_path):
    """
    Writes business records (received in a list) to a .csv file in the provided location

    Parameters:
    tbl_data (list): An outer list that engulfs all businesses data, with each row representing all the data for one business
    yellow_pages_csv_path (str): path (including the filename and extension) of the location desired for the output .csv file

    returns:
    None
    """

    # Open the file for write mode and get a writer object:
    with open(yellow_pages_csv_path, mode='w', newline='') as yellow_pages_csv_file_obj:
        writer = csv.writer(yellow_pages_csv_file_obj)

        # Write header row that has all column names
        header_row = ["name", "address_street_number", "address_street_name", "address_city", "address_state", "address_zip", "phone_area_code", "phone_local_exchange", "email", "website", "category"]
        writer.writerow(header_row)

        # Grab all the data in a given row and store it in the list "row_flattened".  Ensure all the data is "flattened" (i.e. data grouped as tuples like address/phone is handled individually)
        for row in tbl_data:
          row_flattened = []
          for data_or_tup in row:
            if isinstance(data_or_tup, tuple):
              for data in data_or_tup:
                row_flattened.append(data)
            else:
                row_flattened.append(data_or_tup)

          # Write the data record
          writer.writerow(row_flattened)

  
  # make the method below as a getter        
  @property
  def yellow_pages_tbl(self):
    """
    Method converts previous weeks' exercise functions to use the class, reading a data file containing businesses' information
    And storing the records accordingly into a table, each row representing a business.

    The returned list of tuples will be used to populate a private instance attribute "._yellow_pages_tbl"
    
    Returns:
    A list of tuples "_yellow_pages_tbl"
    """
    # set the list to nothing  
    _yellow_pages_tbl = []
  
    # if the private attribute is empty, populate it
    if not self._yellow_pages_tbl:
      
      # get the six sublists
      names = self.parse_all_names()
      addresses = self.parse_all_addresses()
      phones = self.parse_all_phones()
      emails = self.parse_all_emails()
      urls = self.parse_all_urls()
      categories = self.parse_all_categories()

      # Add each item into the list as a tuple containing information for all 6 parts in a business per line/row after unpacking

      for name, address, phone, email, url, category in zip(names, addresses, phones, emails, urls, categories):   
        _yellow_pages_tbl.append((name, address, phone, email, url, category))
      return _yellow_pages_tbl
  

  def yellow_pages_tbl_filter_by(self,
                                 
                                  name="any",
                                  address_street_number="any", address_street_name="any", address_city="any", address_state="any", address_zip="any",
                                  phone_area_code="any", phone_local_exchange="any",
                                  email="any",
                                  website="any",
                                  category="any"  ):
    
    """
    Method returns a filtered list of all businesses found in ._yellow_pages_tbl or data generated from method yellow_pages_tbl
    Based on what is passed as argument values to the method

    The returned filtered list of tuples contains only matching records
    
    Returns:
    A list of tuples "_filtered_list" that match the search related argument values from the method call
    """
    
    # initialize the filtered list
    _filtered_list = []

    # if the class level table is empty, call method yellow_pages_tbl
    if not self._yellow_pages_tbl:
      self.yellow_pages_tbl

    # go through each line in the the yellow pages and see if there are a match
    # set the bol_match flag to false if there is no match and do not add the current line to the filtered list
        
    for line in self.yellow_pages_tbl:
      
      #initialize the match flag
      bol_match = True
      
      # get any argument value passed into the function that is not set to "any" and compare to the current line's value
      # make strings lowercase in the comparisons

      if name.lower() != "any" and name.lower() != line[0].lower():
        bol_match = False
      
      if address_street_number != "any" and address_street_number != line[1][0]:
        bol_match = False

      if address_street_name.lower() != "any" and address_street_name.lower() != line[1][1].lower():
        bol_match = False

      if address_city.lower() != "any" and address_city.lower() != line[1][2].lower():
        bol_match = False

      if address_state.lower() != "any" and address_state.lower() != line[1][3].lower():
        bol_match = False

      if address_zip != "any" and address_zip != line[1][4]:
        bol_match = False

      if phone_area_code != "any" and phone_area_code != line[2][0]:
        bol_match = False

      if phone_local_exchange != "any" and phone_local_exchange != line[2][1]:
        bol_match = False

      if email.lower() != "any" and email.lower() != line[3].lower():
        bol_match = False

      if website.lower() != "any" and website.lower() != line[4].lower():
        bol_match = False

      if category.lower() != "any" and category.lower() !=  line[5].lower():
        bol_match = False

      if bol_match:
        _filtered_list.append(line)
    return _filtered_list