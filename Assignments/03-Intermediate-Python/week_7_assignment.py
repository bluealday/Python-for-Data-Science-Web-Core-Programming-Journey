#################################################
# ASSIGNMENT:                                   #
#################################################
# PROBLEM 1: Data Analysis with Pandas          #
#################################################
# Modify the "<White/Yellow/Company>PagesParser" classes to use a DataFrame for the attribute "._pages_tbl" instead of a list
# 
# Requirements:
#   - The "__init__()" method should set the attribute "._pages_tbl" to an empty DataFrame
#   - The decorated ".pages_tbl()" method should populate the DataFrame "._pages_tbl" and return it.  Be sure to have the sub-parts of address and phone data (e.g. street number, street name, city, state & zip) expanded so that each part resides in its own column.  This is how one yellow pages record should look like in the final DataFrame:
# 
#                   name                        address_street_number   address_street_name     address_city    address_state   address_zip     phone_area_code     phone_local_exchange    email                       website                         category
#       99          Boca Raton Vietnamese Pho   707                     Palmetto Park Road      Boca Raton      FL              33487           561                 555-2345                info@bocaratonpho.com       http://www.bocaratonpho.com     restaurants
# 
#   - The ".pages_tbl_filter_by()" method should apply the requested filters by making the appropriate subsetting operation on the "._pages_tbl" DataFrame.  It should maintain the case-insensitivity feature
#   - The ".to_csv()" method of the parent "WhitePagesParser" class should be simplified to take advantage of the DataFrame ".to_csv()" method (no need to use the "csv" module anymore).  Row indices should not be exported to the output csv file
#     Additionally, the old ".to_csv()" parent class method relied on the class attribute list "header_row" to write the appropriate column names to the output csv file.  But now since you'll re-implementing this method using Pandas DataFrame "to_csv()" method, column names will be automatically written correctly to the csv output file as long as they are set correctly in the DataFrame object.  So, ensure the "._pages_tbl" DataFrame has the correct column names (this should be done in each of the 3 versions of the decorated ".pages_tbl()" method)
# 
# 
# Ensure your code is documented properly with comments and/or docstrings
# Use week_7_assignment_test.py file to test your work.  Import the class there, and create object(s) from it while providing the path for the company pages text file in the "input_data" directory.  Test the various methods and verify the results are correct.  Only submit week_7_assignment.py (do not submit week_7_assignment_test.py)
#################################################

import re
import pandas as pd
import copy  # use this to make a shallow copy of the locals() variables 

class WhitePagesParser():
    """
    Class that parses data from white pages text files and stores them into a dataframe
    """

    # Class Attribute(s):    
    # None


    def __init__(self, pages_path):
        """
        Initialization method that reads the pages text file and stores its lines in the instance attribute list .pages_lines_list

        Parameters:
        pages_path (str): path to text file to be read

        returns:
        None
        This method however will append the lines of the text file to the instance attribute list .pages_lines_list
        """

        ############### MODIFY THIS METHOD ##############

        # # Attribute to hold parsed pages data in tabulated format.  This will be a dataframe that engulfs all the data, with each row representing all the data for one business.  Initialized to empty list for now
        self._pages_tbl = pd.DataFrame()
        

        # # Attribute list that will be used to store the pages text file, each item represents one line of the file
        self.pages_lines_list = []

        # Open the pages text file, read its content line-by-line, and store each line as an item in the attribute pages_lines_list
        with open(pages_path) as pages_file_obj:
            self.pages_lines_list = [line for line in pages_file_obj.readlines()]

        

    def parse_all_names(self, fieldname = "name"):
        """
        Returns all records' names (or titles or organizations)

        Parameters:
        fieldname (str): string that represents name of the field with which the pages text file line starts with.  This should be "name", "title" or "organization"

        returns:
        list: All records' names (or titles or organizations)
        """

        # Create the list that'll store all records names
        names_list = []

        # Loop through each line of the pages file
        for line in self.pages_lines_list:

            # Check if the line is the "name" line
            if line.startswith(f"{fieldname}: "):

                # Search for the name pattern using regex
                regex_result = re.findall(r"{}: (.+)".format(fieldname), line)

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
        Returns all records' addresses, with each address broken into a tuple consisting of (Street Number, Street Name, City, State, Zip)

        Parameters:
        None

        returns:
        list: All records' websites.  Each address is captured in a tuple that consists of (Street Number, Street Name, City, State, Zip)
        """

        # Create the list that'll store all records addresses
        addresses_list = []

        # Loop through each line of the pages file
        for line in self.pages_lines_list:

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
        Returns all records' phone numbers

        Parameters:
        None

        returns:
        list: all records' phone numbers
        """

        # Create the list that'll store all records phone numbers
        phones_list = []

        # Loop through each line of the pages file
        for line in self.pages_lines_list:

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
    

    @property
    def pages_tbl(self):
        """
        Parses all pages data (names, addresses & phones) and stores them in tabulated format in the private instance attribute self._pages_tbl

        Parameters:
        None

        returns:
        dataframe: A dataframe that engulfs all records data, with each row representing all the data for one record
        """

        ############### MODIFY THIS METHOD ##############

        # To save time, only parse pages text file if this hasn't been done yet
        if self._pages_tbl is None or self._pages_tbl.empty:
            
            # Parse all records names
            names = self.parse_all_names()

            # Parse all records addresses
            addresses = self.parse_all_addresses()

            # Parse all records phones
            phones = self.parse_all_phones()

            # Re-arrange all data in the dataframe and write it to the self._pages_tbl attribute  
            self._pages_tbl = pd.DataFrame(list(zip(names, addresses, phones)), columns=["name", "address", "phone"])
        
            # Expand the "address" column to: 
            # "address_street_number", "address_street_name", "address_city" , "address_state", and "address_zip"
            self._pages_tbl[ ["address_street_number", "address_street_name", "address_city", "address_state", "address_zip" ] ] =\
            self._pages_tbl.address.to_list()

            # Expand the "phone" column to "phone_area_code" and "phone_local_exchange": 
            self._pages_tbl[ ["phone_area_code", "phone_local_exchange" ] ] = self._pages_tbl.phone.to_list()
        
            # Re-organize the DataFrame columns to match the format provided by previous assignments
            self._pages_tbl = self._pages_tbl[ ["name", "address_street_number", "address_street_name", "address_city",\
                                                "address_state", "address_zip", "phone_area_code", "phone_local_exchange"] ]

        return self._pages_tbl

    def get_criteria(self, keys_dict):
        
        """
        Takes in a dictionary and returns a criteria string (used in method pages_tbl_filter_by)
        
        Parameters:
        keys_dict: Dictionary of search fields and values

        returns:
        criteria: String used for search criteria in other methods
        """

        criteria = ""

        for my_key, my_value in keys_dict.items():
        
            # Only get the variables that are part of the search criteria
            if my_key != "self" and not my_key.startswith('__') and not my_value.lower() == "any":
                criteria += my_key + ".str.lower() == '" +  my_value.lower() + "' and "        
            
        # remove the trailing connector
            
        if criteria:
            criteria = criteria[:-5]
        
        return criteria
           

    def pages_tbl_filter_by(    self,                         
                                name="any",
                                address_street_number="any", address_street_name="any", address_city="any", address_state="any", address_zip="any",
                                phone_area_code="any", phone_local_exchange="any"   ):
        """
        Filters records by any combination of the 8 criteria described below in parameters.  Exact match is required.  Case-Insensitive.  If no value provided for a given criterion, "any" is assumed which results in no filtering

        
        Parameters:
        name (str): Exact match of the full record name
        
        address_street_number (str): Exact match of address street number
        address_street_name (str): Exact match of address street name
        address_city (str): Exact match of the address city
        address_state (str): Exact match of the address state (in 2-letter format)
        address_zip (str): Exact match of the address zip
        
        phone_area_code (str):
        phone_local_exchange (str): Exact match of the phone area code (in 3-digit format without any pre/post-fixes)

        
        returns:
        Dataframe: A dataframe that engulfs all records data for which the filter criteria is matched, with each row representing all the data for one record
        """

        self.filtered_dataframe = pd.DataFrame()

        ############### MODIFY THIS METHOD ##############
        # Populate ._pages_tbl if it's empty
        # Make a copy of the locals() dictionary
        # Form the search critiria for matching items with variables passed into the function using the query() method

        if not self._pages_tbl:
            self.pages_tbl
            keys_dict = copy.copy(locals())
            match_criteria = self.get_criteria(keys_dict) 
            if match_criteria:
                self.filtered_dataframe = self.pages_tbl.query(match_criteria)

        return self.filtered_dataframe

  
    def to_csv(self, tbl_data, pages_csv_path):
        """
        Writes records (received in a dataframe) to a .csv file in the provided location

        Parameters:
        tbl_data (dataframe): A dataframe that engulfs all records data, with each row representing all the data for one record
        pages_csv_path (str): path (including the filename and extension) of the location desired for the output .csv file

        returns:
        None
        """
        
        ############### MODIFY THIS METHOD ##############
        # Write the dataframe contents into a csv file without indexes
        
        self._pages_tbl = tbl_data.to_csv(pages_csv_path, index=False)
        
class YellowPagesParser(WhitePagesParser):
    """
    Class that parses data from yellow pages text files and stores them into a dataframe
    """

    # Class Attribute(s):
    # None
    
    
    def parse_all_emails(self):
        """
        Returns all records' emails

        Parameters:
        None

        returns:
        list: All records' emails
        """

        # Create the list that'll store all records emails
        emails_list = []

        # Loop through each line of the pages file
        for line in self.pages_lines_list:

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
        Returns urls for all records' websites

        Parameters:
        None

        returns:
        list: URLs for all records' websites
        """

        # Create the list that'll store all found URLs
        urls_list = []

        # Loop through each line of the pages file
        for line in self.pages_lines_list:

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
        Returns all records' categories

        Parameters:
        None

        returns:
        list: Categories for all records
        """

        # Create the list that'll store all records categories
        categories_list = []

        # Loop through each line of the pages file
        for line in self.pages_lines_list:

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
    

    @property
    def pages_tbl(self):
        """
        Parses all pages data (names, addresses, phones, emails, websites & categories) and stores them in tabulated format in the private instance attribute self._pages_tbl

        Parameters:
        None

        returns:
        dataframe: A dataframe that engulfs all records data, with each row representing all the data for one record
        """

        ############### MODIFY THIS METHOD ##############

        # # To save time, only parse pages text file if this hasn't been done yet
        if self._pages_tbl is None or self._pages_tbl.empty:

        
            # Parse all records names
            names = self.parse_all_names()

            # Parse all records addresses
            addresses = self.parse_all_addresses()

            # Parse all records phones
            phones = self.parse_all_phones()

            # Parse all records emails
            emails = self.parse_all_emails()

            # Parse all records websites
            websites = self.parse_all_urls()

            # Parse all records categories
            categories = self.parse_all_categories()

            # Re-arrange all data for the dataframe 0and write it to the self._pages_tbl attribute  
            self._pages_tbl = pd.DataFrame(list(zip(names, addresses, phones, emails, websites, categories)),\
                                           columns=["name", "address", "phone", "email", "website", "category"])
        
            # Expand the "address" column to: 
            # "address_street_number", "address_street_name", "address_city" , "address_state", and "address_zip"
            self._pages_tbl[ ["address_street_number", "address_street_name", "address_city", "address_state", "address_zip" ] ] =\
            self._pages_tbl.address.to_list()

            # Expand the "phone" column to "phone_area_code" and "phone_local_exchange": 
            self._pages_tbl[ ["phone_area_code", "phone_local_exchange" ] ] = self._pages_tbl.phone.to_list()
        
            # Re-organize the DataFrame columns to match the format provided by previous assignments
            self._pages_tbl = self._pages_tbl[ ["name", "address_street_number", "address_street_name", "address_city",\
                                                "address_state", "address_zip", "phone_area_code", "phone_local_exchange",\
                                                "email", "website", "category"] ]

        return self._pages_tbl


    def pages_tbl_filter_by(    self,
                                    
                                name="any",
                                address_street_number="any", address_street_name="any", address_city="any", address_state="any", address_zip="any",
                                phone_area_code="any", phone_local_exchange="any",
                                email="any",
                                website="any",
                                category="any"  ):
        """
        Filters records by any combination of the 11 criteria described below in parameters.  Exact match is required.  Case-Insensitive.  If no value provided for a given criterion, "any" is assumed which results in no filtering

        
        Parameters:
        name (str): Exact match of the full record name
        
        address_street_number (str): Exact match of address street number
        address_street_name (str): Exact match of address street name
        address_city (str): Exact match of the address city
        address_state (str): Exact match of the address state (in 2-letter format)
        address_zip (str): Exact match of the address zip
        
        phone_area_code (str):
        phone_local_exchange (str): Exact match of the phone area code (in 3-digit format without any pre/post-fixes)

        email (str): Exact match of the full email address

        website (str): Exact match of website

        category (str): Exact match of the category

        
        returns:
        Dataframe: A dataframe that engulfs all records data for which the filter criteria is matched, with each row representing all the data for one record
        """

        ############### MODIFY THIS METHOD ##############

        if not self._pages_tbl:
            self.pages_tbl
            keys_dict = copy.copy(locals())
            match_criteria = self.get_criteria(keys_dict) 
            if match_criteria:
                self.pages_tbl.query(match_criteria, inplace=True)

        return self.pages_tbl
    


class CompanyPagesParser(YellowPagesParser):
    """
    Class that parses data from company pages text files and stores them into a dataframe
    """

    # Class Attribute(s):
    # None
    

    def parse_all_titles(self):
        """
        Returns all records' titles

        Parameters:
        None

        returns:
        list: Titles for all records
        """

        # Get all titles by relying on the parent class ".parse_all_names()" method
        return self.parse_all_names(fieldname="title")


    def parse_all_organizations(self):
        """
        Returns all records' organizations

        Parameters:
        None

        returns:
        list: Titles for all organizations
        """

        # Get all organizations by relying on the parent class ".parse_all_names()" method
        return self.parse_all_names(fieldname="organization")
  

    @property
    def pages_tbl(self):
        """
        Parses all pages data (names, titles, organizations, addresses, phones, emails, websites) and stores them in tabulated format in the private instance attribute self._pages_tbl

        Parameters:
        None

        returns:
        dataframe: A dataframe that engulfs all records data, with each row representing all the data for one record
        """

        ############### MODIFY THIS METHOD ##############

        # # To save time, only parse pages text file if this hasn't been done yet
        if self._pages_tbl is None or self._pages_tbl.empty:


            # Parse all records names
            names = self.parse_all_names()

            # Parse all records titles
            titles = self.parse_all_titles()

            # Parse all records organizations
            organizations = self.parse_all_organizations()

            # Parse all records addresses
            addresses = self.parse_all_addresses()

            # Parse all records phones
            phones = self.parse_all_phones()

            # Parse all records emails
            emails = self.parse_all_emails()

            # Parse all records websites
            websites = self.parse_all_urls()

            # Re-arrange all data for the dataframe 0and write it to the self._pages_tbl attribute  
            self._pages_tbl = pd.DataFrame(list(zip(names, titles, organizations, addresses, phones, emails, websites)),\
                                           columns=["name", "title", "organization", "address", "phone", "email", "website"])
        
            # Expand the "address" column to: 
            # "address_street_number", "address_street_name", "address_city" , "address_state", and "address_zip"
            self._pages_tbl[ ["address_street_number", "address_street_name", "address_city", "address_state", "address_zip" ] ] =\
            self._pages_tbl.address.to_list()

            # Expand the "phone" column to "phone_area_code" and "phone_local_exchange": 
            self._pages_tbl[ ["phone_area_code", "phone_local_exchange" ] ] = self._pages_tbl.phone.to_list()
        
            # Re-organize the DataFrame columns to match the format provided by previous assignments
            self._pages_tbl = self._pages_tbl[ ["name", "title", "organization", "address_street_number", "address_street_name",\
                                                "address_city", "address_state", "address_zip", "phone_area_code",\
                                                "phone_local_exchange", "email", "website"] ]
        
        return self._pages_tbl


    def pages_tbl_filter_by(    self,
                                  
                                name="any",
                                title="any",
                                organization="any",
                                address_street_number="any", address_street_name="any", address_city="any", address_state="any", address_zip="any",
                                phone_area_code="any", phone_local_exchange="any",
                                email="any",
                                website="any"   ):
        """
        Filters records by any combination of the 12 criteria described below in parameters.  Exact match is required.  Case-Insensitive.  If no value provided for a given criterion, "any" is assumed which results in no filtering

      
        Parameters:
        name (str): Exact match of the full record name
      
        title (str): Exact match of the full record title

        organization (str): Exact match of the full record organization

        address_street_number (str): Exact match of address street number
        address_street_name (str): Exact match of address street name
        address_city (str): Exact match of the address city
        address_state (str): Exact match of the address state (in 2-letter format)
        address_zip (str): Exact match of the address zip
      
        phone_area_code (str):
        phone_local_exchange (str): Exact match of the phone area code (in 3-digit format without any pre/post-fixes)

        email (str): Exact match of the full email address

        website (str): Exact match of website

      
        returns:
        Dataframe: A dataframe that engulfs all records data for which the filter criteria is matched, with each row representing all the data for one record
        """
        
        ############### MODIFY THIS METHOD ##############
        
        # # To save time, only parse pages text file if this hasn't been done yet

        if not self._pages_tbl:
            self.pages_tbl
            keys_dict = copy.copy(locals())
            match_criteria = self.get_criteria(keys_dict) 
            if match_criteria:
                self.pages_tbl.query(match_criteria, inplace=True)

        return self.pages_tbl

