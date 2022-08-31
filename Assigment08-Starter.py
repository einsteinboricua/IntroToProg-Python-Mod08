# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Dennis Negron-Rivera,26/Aug/22, Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name

        product_price: (float) with the product's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Dennis Negron-Rivera,26/Aug/22,Modified code to complete assignment 8
    """
    #pass
    # TODO: Add Code to the Product class

    #Product Variables
    __strPrName = ""
    __fltPrPrice = 0.00

    #Product Constructor
    def __init__(self, name, price):
        self.__strPrName = name
        self.__fltPrPrice = float(price)
    
    #Getters for access to product variables
    @property
    def getProductName(self):
        return self.__strPrName
    @property
    def getProductPrice(self):
        return float(self.__fltPrPrice)
    
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Dennis Negron-Rivera,26/Aug/2022,Modified code to complete assignment 8
    """
    #pass
    # TODO: Add Code to process data from a file
    def read_data_from_file(file_name):
        ''' Loads data from a file.
            Input: string file_name
            Returns: nothing'''
        #If the file exists, open it and load onto list
        try:
            fileHandler = open(file_name,"r")
            for line in fileHandler:
                lstRow = line.split(',')
                prod = Product(lstRow[0],float(lstRow[1]))
                lstOfProductObjects.append(prod)
            #File exists but it was empty
            if len(lstOfProductObjects) == 0:
                print("\nThere were no products to load.")
            #File exists and it had items
            else:
                print("\nProducts loaded.")
            fileHandler.close()
        #File does not exist; continue
        except:
            print("\nFile does not exist. No object loaded.")  

    # TODO: Add Code to process data to a file
    def save_data_to_file(file_name,list_of_product_objects):
        '''Saves the list onto the given file
           Input: string file_name, list list_of_product_objects
           Returns: nothing'''
        fileHandler = open(file_name,"w")
        print("Saving data to "+file_name)
        #Use a counter to know when to stop adding new lines
        counter = 1
        for row in list_of_product_objects:
            if counter != len(list_of_product_objects): 
                fileHandler.write(row.getProductName+","+str(row.getProductPrice)+"\n")
                counter += 1
            #If item is the last, no new line at the end    
            else: 
               fileHandler.write(row.getProductName+","+str(row.getProductPrice))
        print("Data saved")
        fileHandler.close()

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    ''' Performs Input and Output tasks'''
    #pass
    # TODO: Add code to show menu to user
    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current products on list
        2) Add product to list       
        3) Save data and exit program
        ''')
        print()  # Add an extra line for looks
    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def output_current_products_in_list(list_of_rows):
        """ Shows the current products in the list of Product rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Products are: *******")
        #if list is empty, print so.
        if len(list_of_rows)==0:
            print("List is currently empty.")
        #If not, then print products.
        else:
            counter = 1
            for row in list_of_rows:
                print(str(counter)+". "+row.getProductName + " ($" + '%.2f' %row.getProductPrice + ")" )
                counter+=1
        print("*******************************************")
        print()  # Add an extra line for looks

    # TODO: Add code to get product data from user
    @staticmethod
    def input_new_product_name_and_price():
        """  Gets product name and price values to be added to the list

        :return: (string, string) with product name and price
        """
        # Input validation, namely for the price
        try:
            strProduct = input("What product do you wish to add? ").strip()
            print()
            fltPrice = input("What is the product's price? ").strip()
            print()
            fltPrice = float(fltPrice)
        # The user did not enter a number; throw an exception and return a dummy value
        except ValueError:
            print("Price must be in numeric form.\n")
            return "zzzzz", 0.0
        #Everything is in order, return the name and price
        return strProduct, float(fltPrice)
        
# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body

# Load data from file into a list of product objects when script starts
FileProcessor.read_data_from_file(file_name=strFileName) 

# Show user a menu of options
while (True):
    IO.output_menu_tasks()  # Shows menu

# Get user's menu option choice
    choice_str = IO.input_menu_choice()  # Get menu option
    
    # Show user current data in the list of product objects   
    if choice_str=="1": 
        IO.output_current_products_in_list(list_of_rows=lstOfProductObjects)  # Show current data in the list/table
        continue
    
    # Let user add data to the list of product objects
    elif choice_str=="2":
        strName,fltPrice = IO.input_new_product_name_and_price() #Prompt for name and price
        # Was a dummy value returned? If not, add to list
        if strName.lower()!="zzzzz":
            lstOfProductObjects.append(Product(name=strName,price=fltPrice))
            print("Added "+strName+" to the list.")
        #Dummy value was returned; do not add to list
        else:
            print("Nothing was added. Returning to main menu.\n")

        continue

    # Let user save current data to file and exit program
    elif choice_str=="3":
        FileProcessor.save_data_to_file(file_name=strFileName,list_of_product_objects=lstOfProductObjects)
        print("Now exiting...")
        break

    # Wrong input; prompt to try again.
    else:
        print("Wrong input. Please select 1-3.\n")
        continue


# Main Body of Script  ---------------------------------------------------- #

