# Define a class named Shoe to represent shoe objects
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        '''
        Initialize attributes for the Shoe class.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        '''
        Return the cost of the shoe.
        '''
        return self.cost

    def get_quantity(self):
        '''
        Return the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):
        '''
        Return a string representation of a shoe.
        '''
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"

# Shoe list to store objects of shoes
shoe_list = []

# Function to write shoe data to a file
def write_shoes_data():
    try:
        with open('inventory.txt', 'w') as file:
            # Write header
            file.write("Country,Code,Product,Cost,Quantity\n")
            # Write data for each shoe in the shoe_list
            for shoe in shoe_list:
                file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
        print("Data written to file successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to read shoe data from a file and populate the shoe_list
def read_shoes_data():
    try:
        with open('inventory.txt', 'r') as file:
            next(file)  # Skip the first line (header)
            # Iterate through each line in the file
            for line in file:
                # Split the line into individual data elements
                country, code, product, cost, quantity = line.strip().split(',')
                # Convert cost to float and quantity to integer
                cost = float(cost)
                quantity = int(quantity)
                # Create a Shoe object and add it to the shoe_list
                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)
        print("Data loaded successfully!")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to capture shoe data from user input and add a new Shoe object to shoe_list
def capture_shoes():
    country = input("Enter country: ")
    code = input("Enter code: ")
    product = input("Enter product: ")
    cost = float(input("Enter cost: "))
    quantity = int(input("Enter quantity: "))
    # Create a new Shoe object with user input and add it to the shoe_list
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    print("Shoe added successfully!")
    # Update the text file with the new shoe data
    write_shoes_data()

# Function to update an existing shoe in the shoe_list
def update_shoe(shoe_index):
    quantity_change = int(input("Enter the new quantity: "))
    # Update the quantity of the chosen shoe object
    shoe_list[shoe_index].quantity = quantity_change
    print(f"Quantity of {shoe_list[shoe_index].product} updated successfully!")
    # Update the text file with the modified shoe data
    write_shoes_data()

# Function to view all Shoe objects in the shoe_list
def view_all():
    for shoe in shoe_list:
        print(shoe)

# Function to find the shoe object with the lowest quantity and ask if the user wants to restock those shoes
def re_stock():
    if not shoe_list:
        print("No shoes in the inventory.")
        return

    # Find the shoe object with the lowest quantity
    lowest_quantity_shoe = min(shoe_list, key=lambda x: x.quantity)
    # Display information about the shoe with the lowest quantity
    print(f"Shoe with the lowest quantity: {lowest_quantity_shoe}")

    # Ask the user if they want to restock this shoe
    restock_choice = input("Do you want to restock this shoe? (yes/no): ").lower()

    if restock_choice == 'yes':
        # Get the quantity to restock from the user
        restock_quantity = int(input("Enter the quantity to restock: "))
        # Update the quantity of the chosen shoe object
        lowest_quantity_shoe.quantity += restock_quantity
        print(f"{restock_quantity} units of {lowest_quantity_shoe.product} have been restocked.")
        # Update the text file with the modified shoe data
        write_shoes_data()
    elif restock_choice == 'no':
        print("No restocking performed.")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")

# Function to search for a shoe by product name
def search_shoe():
    product_name = input("Enter the product name to search: ")
    found_shoes = [shoe for shoe in shoe_list if product_name.lower() in shoe.product.lower()]

    if found_shoes:
        print("Matching shoes found:")
        for shoe in found_shoes:
            print(shoe)
    else:
        print("No matching shoes found.")

# Function to calculate the value per item for each shoe
def value_per_item():
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"Value per item for {shoe.product}: {value}")

# Function to find the shoe with the highest quantity and mark it as on sale
def highest_qty():
    if not shoe_list:
        print("No shoes in the inventory.")
        return

    # Find the shoe object with the highest quantity
    highest_quantity_shoe = max(shoe_list, key=lambda x: x.quantity)
    # Display information about the shoe with the highest quantity
    print(f"Shoe with the highest quantity: {highest_quantity_shoe}")
    # Mark the shoe as on sale
    highest_quantity_shoe.product += " (On Sale)"
    print(f"{highest_quantity_shoe.product} marked as on sale.")

# Main menu function to provide options for user interaction
def main_menu():
    while True:
        print("\n=== Main Menu ===")
        print("1. Read Shoes Data")
        print("2. Capture Shoes")
        print("3. View All Shoes")
        print("4. Re-stock Shoes")
        print("5. Search for a Shoe")
        print("6. Value per Item")
        print("7. Highest Quantity Shoe")
        print("8. Quit")

        # Prompt user for choice
        choice = input("Enter your choice: ")

        # Perform actions based on user's choice
        if choice == '1':
            read_shoes_data()
        elif choice == '2':
            capture_shoes()
        elif choice == '3':
            view_all()
        elif choice == '4':
            re_stock()
        elif choice == '5':
            search_shoe()
        elif choice == '6':
            value_per_item()
        elif choice == '7':
            highest_qty()
        elif choice == '8':
            print("Exiting the program. Goodbye!")
            exit()  # Add exit condition
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

# Call the main_menu() function to start the program
main_menu()            
