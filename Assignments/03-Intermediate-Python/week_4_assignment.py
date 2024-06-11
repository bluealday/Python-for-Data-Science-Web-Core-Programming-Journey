#################################################
# ASSIGNMENT:                                   #
#################################################
# PROBLEM 1: Generators                         #
#################################################
# Write a generator function named "book_autograph()".  The function takes in a full book text, a generic autograph message, and a list of readers' names, and yields back the full book autographed with a message customized to each reader's name.
# 
# Parameters:
#   full_book_text (dict): A dictionary that contains the full book text translated into multiple languages.  The keys for this dictionary are two-letter language codes.  For example, full_book_text["en"] provides the full English version of the book.  week_4_assignments_data has this dictionary which contains the book in all of these languages: English (en), German (de), Finnish (fi), French (fr), Polish (pl), Greek (el) and Dutch (nl).
#   autograph_message (dict): A dictionary that has a generic autograph message available in multiple languages.  Like full_book_text, to access the message in a particular language, we can use that language code as the key like this: autograph_message[<2-letter-language-code>].  week_4_assignments_data has this dictionary which contains the same autograph message in all of these languages: English (en), German (de), Finnish (fi), French (fr), Polish (pl), Greek (el) and Dutch (nl).
#   readers_info (list): A list that contains the reader's firstname along with their desired language.  The data is organized as tuples inside the list.  Each tuple contains the reader's firstname and their 2-letter language code.
# 
# The function will yield the full book text autographed with a personalized message that uses the reader's firstname.  It will do this for all the readers passed.  The language of the personalized autographed book shall be according to the user's language code as present in "readers_info" argument.
# For example, this is what the function will yield for a reader whose name is "John" and his language is English:
# 
#    John,
#
#    It was a pleasure to meet you and to sign your copy of my book. I appreciate your support and your interest in my work. I hope you find the book engaging and inspiring. You have a great sense of humor and a warm personality, which I admire. Keep smiling and keep reading.
#
#    Sincerely,
# 
#    *** FULL BOOK's TEXT GOES HERE ***
# 
# Ensure your code is documented properly with comments and/or docstrings
# Use week_4_assignment_test.py file to test your work.  Import the function there, call it by passing to it the data present in input_data/week_4_assignment_data.py, and verify the results are correct.  Only submit week_4_assignment.py (do not submit week_4_assignment_test.py)
#################################################

def book_autograph(full_book_text, autograph_message, readers_info):

  """
    Generator function that yields copies of full_book_text with the autographed message applied for readers, one reader at a time

    Parameters:
    full_book_text (dict): A dictionary that contains the full book text translated into multiple languages.
    autograph_message (dict): A dictionary that has a generic autograph message available in multiple languages.
    readers_info (list): A list that contains the reader's firstname along with their desired language.
  """

  for firstname, language in readers_info:
        # get the authographed message based on the reader's language and form the autographed message
        autographed_message = firstname + ", \n" + autograph_message[language]

        # get the full book's text based on the reader's language
        book_text = full_book_text[language] 

        # create the autographed book
        single_authographed_book = autographed_message + "\n" + book_text
        # checked memory while testing function and verified it did not increase per the lesson
        # adjusted vs code settings to show more lines in terminal
  yield single_authographed_book        

#################################################
# ASSIGNMENT:                                   #
#################################################
# PROBLEM 2: Regular Expressions                #
#################################################
# A copy of the exercises' yellow pages file is placed at "assignments/input_data/yellow_pages.txt".  Follow same approach used in the exercises to create the functions:
#   - parse_all_names()         ->          returns a list containing all businesses' names.  Business names can have diverse set of characters including periods, ampersands, dashes and spaces (but not newlines)
#   - parse_all_addresses()     ->          returns a list containing all businesses' addresses.  Each address should be broken into 5 subgroups (Street Number, Street Name, City, State and Zip).  The returned list should contain 100 tuples for the 100 addresses, with each tuple containing all the 5 parts of the address (Street Number, Street Name, City, State and Zip).  For example, the tuple for the first business address should be ("1234", "Coral Way", "Miami", "FL", "33145").  Keep in mind that some of the address parts may have spaces (like Street Name and City)
#   - parse_all_phones()        ->          returns a list containing all businesses' phone numbers.  Similarly, each phone number should be broken into 2 subgroups, Area Code and the remaining 7-digit number
#   - parse_all_emails()        ->          returns a list containing all businesses' emails.  An empty string should be stored for businesses without email
#   - parse_all_categories()    ->          returns a list containing all businesses' categories
# 
# Ensure your code is documented properly with comments and/or docstrings
# Use week_4_assignment_test.py file to test your work.  Import the function there along with the input data that goes with it (if any), and make calls to it to verify the results are correct.  Only submit week_4_assignment.py (do not submit week_4_assignment_test.py)
#################################################

import re

# Global list that will be used to store the yellow pages text file, each item represents one line of the file
YELLOW_PAGES_LINES_LIST = []

# Function to read the yellow pages text file and store its lines in the global list YELLOW_PAGES_LINES_LIST
def read_file(yellow_pages_path):
  """
  Read the yellow pages text file and store its lines in the global list YELLOW_PAGES_LINES_LIST

  Parameters:
  yellow_pages_path (str): path to text file to be read

  returns:
  None
  This function however will append the lines of the text file to the global list YELLOW_PAGES_LINES_LIST
  """

  # "global" keyword is used to indicate that the identifier YELLOW_PAGES_LINES_LIST refers to the global list.  Without the "global" keyword, a local identifier named YELLOW_PAGES_LINES_LIST would be created instead and would get destroyed immediately upon finishing the execution of the function
  global YELLOW_PAGES_LINES_LIST

  # Open the yellow pages text file, read its content line-by-line, and store each line as an item in the global list YELLOW_PAGES_LINES_LIST
  with open(yellow_pages_path) as yellow_pages_file_obj:
    YELLOW_PAGES_LINES_LIST = [line for line in yellow_pages_file_obj.readlines()]

def parse_all_urls():
  """
  Go through global YELLOW_PAGES_LINES_LIST to extract URLs
  
  Parameters:
  None
  
  returns:
  Return a list of URLs found from the global YELLOW_PAGES_LINES_LIST

  """

  global YELLOW_PAGES_LINES_LIST
  
  # initialize the URL list
  found_url_list = []
  
  # define the pattern to find the URL
  pat = r"^website: +(\S+)$"
  
  for line in YELLOW_PAGES_LINES_LIST:
    # if the current line starts with "website"
    # add the value to the list. If the value is empty, add an empty string 
    if re.findall(r"^website: ", line):
      match = re.findall(pat, line)
      if match:
        found_url_list.append(match[0])
      else:
        found_url_list.append("")
  return found_url_list

def parse_all_names():
  """
  Go through global YELLOW_PAGES_LINES_LIST to find business names
  
  Parameters:
  None
  
  returns:
  Return a list of business names found from the global YELLOW_PAGES_LINES_LIST

  """

  global YELLOW_PAGES_LINES_LIST
  
  # initialize the business names list
  business_names_list = []
  
  # define the pattern to get the business name except for any newline 
  pat = r"^name: (.+)$"
  
  for line in YELLOW_PAGES_LINES_LIST:
    # if the current line starts with "name: "
    # add the value to the list.
     
    if re.findall(r"^name: ", line):
      name_match = re.findall(pat, line)
      if name_match:
        business_names_list.append(name_match[0])
  return business_names_list

def parse_all_addresses():
  """
  Go through global YELLOW_PAGES_LINES_LIST to find the business address
  
  Parameters:
  None
  
  returns:
  Return a list of addresses broken down into tuples consisting of:
  - Street Number
  - Street Name
  - City
  - State
  - Zip
  
  """

  global YELLOW_PAGES_LINES_LIST
  
  # initialize the business address list
  address_list = []
  
  # define the pattern to get the business address
  
  pat = r"^address: (?P<streetnumber>\S+) (?P<streetname>.*) - (?P<city>.*), (?P<state>\S\S) (?P<zip>\S+)"
  
  for line in YELLOW_PAGES_LINES_LIST:
    # if the current line starts with "address: "
    # add the 5 tuple values to the list.
     
    if re.findall(r"^address: ", line):
      address = re.findall(pat, line)
      if address:
        address = re.search(pat, line)
        address_list.append(tuple([address.group('streetnumber'), address.group('streetname'), address.group('city'), address.group('state'), address.group('zip')]))
  return address_list


def parse_all_phones():
  """
  Go through global YELLOW_PAGES_LINES_LIST to find area code and 7 digit numbers
  
  Parameters:
  None
  
  returns:
  Return a list of phone nummbers broken down into tuples consisting of:
  - Area Code
  - 7 digit number
  """

  global YELLOW_PAGES_LINES_LIST
  
  # initialize the business address list
  phone_list = []

  # define the pattern to get the business phone
  pat = r"^phone: \((?P<areacode>\d\d\d)\) (?P<sevendigit>\d\d\d-\d\d\d\d)"
  
  for line in YELLOW_PAGES_LINES_LIST:
    # if the current line starts with "phone: "
    # add the tuple values for areacode and sevendigit to the list.
     
    if re.findall(r"^phone: ", line):
      phone = re.findall(pat, line)
      if phone:
        phone = re.search(pat, line)
        phone_list.append(tuple([phone.group('areacode'), phone.group('sevendigit')]))
  return phone_list


def parse_all_emails():
  """
  Go through global YELLOW_PAGES_LINES_LIST to extract email addresses
  
  Parameters:
  None
  
  returns:
  Return a list of email addresses found from the global YELLOW_PAGES_LINES_LIST

  """
  global YELLOW_PAGES_LINES_LIST
  
  # initialize the email address list
  email_address_list = []
  
  # define the pattern to find the URL
  pat = r"^email: +(\S+)$"
  
  for line in YELLOW_PAGES_LINES_LIST:
  
    # if the current line starts with "email"
    # add the value to the list. If the value is empty, add an empty string 
  
    if re.findall(r"^email: ", line):
      email_match = re.findall(pat, line)
      if email_match:
        email_address_list.append(email_match[0])
      else:
        email_address_list.append("")
  return email_address_list

def parse_all_categories():
  """
  Go through global YELLOW_PAGES_LINES_LIST to find business categories
  
  Parameters:
  None
  
  returns:
  Return a list of business categories found from the global YELLOW_PAGES_LINES_LIST

  """

  global YELLOW_PAGES_LINES_LIST
  
  # initialize the category list
  category_names_list = []
  
  # define the pattern to get the business name except for any newline 
  pat = r"^category: (.+)$"
  
  for line in YELLOW_PAGES_LINES_LIST:
    # if the current line starts with "category: "
    # add the value to the list.
     
    if re.findall(r"^category: ", line):
      category_match = re.findall(pat, line)
      if category_match:
        category_names_list.append(category_match[0])
  return category_names_list
