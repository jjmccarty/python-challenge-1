# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered

# Instantiation of the order list for holding customer order selections. 
# Expected order format
'''
order_list = [
    {
        "Item name":"string value",
        "Price": float,
        "Quantity": int
    },
    {
        "Item name":"string value",
        "Price": float,
        "Quantity": int
    }
]
'''
order_list = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("The following menu categories are available to order from:")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Please enter the # for the category you wish to order from: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            #print(f"What {menu_category_name} item would you like to order?")
            print(f"The following are the items available from {menu_category_name}:")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_category_item_num = input(f"Please enter the # for the {menu_category_name} would you like to order: ")

            # 3. Check if the customer typed a number
            if menu_category_item_num.isdigit():
                # Convert the menu selection to an integer
                menu_category_item_num = int(menu_category_item_num)

                # 4. Check if the menu selection is in the menu items
                if menu_category_item_num < len(menu_items.keys()):
                    # Store the item name as a variable
                    menu_category_item_name = menu_items[menu_category_item_num]["Item name"]

                    # Ask the customer for the quantity of the menu item
                    menu_category_item_qty = input(f"How many of the {menu_category_item_name} items would you like to purchase? ")

                    # Check if the quantity is a number, default to 1 if not
                    if not menu_category_item_qty.isdigit():                        
                        print(f"Your entry of {menu_category_item_qty} was not valid.  A quantity of 1 {menu_category_item_name} has been selected for you.")
                        menu_category_item_qty = 1                    

                    # Add the item name, price, and quantity to the order list
                    # to just have quantiy updated.
                    new_order_item = dict()
                    new_order_item["Item name"] = menu_category_item_name
                    new_order_item["Quantity"] = int(menu_category_item_qty)
                    new_order_item["Price"] = menu_items[menu_category_item_num]["Price"]

                    #check to see if the order item is already on the order list
                    item_already_in_list = False
                    item_idx = 0
                    for item in order_list:
                        item_already_in_list = new_order_item["Item name"] == item["Item name"]
                        if item_already_in_list: 
                            print("item found")
                            break
                        item_idx = item_idx + 1

                    #if the order item is present simply retrieve the item and update the quantity
                    #otherwise append the new item to the order list
                    if not new_order_item["Quantity"] == 0:
                        if item_already_in_list:                                             
                            existing_item = order_list[item_idx]
                            new_qty = existing_item["Quantity"] + new_order_item["Quantity"]
                            existing_item.update({"Quantity": new_qty})
                            new_order_item["Quantity"] = existing_item["Quantity"]
                            print("The following item quantities were updated on your order")
                        else:    
                            order_list.append(new_order_item)
                            print("The following item was added to your order")

                        #print the additional item in a friendly manner                    
                        print("--------------------------------------------")
                        print(f"Item: {new_order_item["Item name"]}")
                        print(f"Price ea: ${new_order_item["Price"]}")
                        print(f"Qty: {new_order_item["Quantity"]}")
                        print("--------------------------------------------")
                    else:
                        print(f"You entered a quantity of 0 for {new_order_item["Item name"]}. Nothing was added or updated on your order")

                    # Tell the customer that their input isn't valid
                else:
                    print(f"The selection entered  ({menu_category_item_num}) is not a {menu_category_name} item. No items was added to the order.")

                # Tell the customer they didn't select a menu option
            else:
                print(f"The selection entered  ({menu_category_item_num}) is not a {menu_category_name} item. No items was added to the order.")

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} is not a valid menu option. No items were added to the order.")
    else:
        # Tell the customer they didn't select a number
        print(f"{menu_category} is not a valid menu option. No items were added to the order.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").lower()

        #friendly conversion if the user types in the entire word for yes or no. 
        match keep_ordering:
            case 'yes':
                keep_ordering = 'y'
            case 'no':
                keep_ordering = 'n'
        
        # 5. Check the customer's input
        match keep_ordering:
            case 'y':
                #break this loop and continue to order
                break
            case 'n':
                # Complete the order
                # Since the customer decided to stop ordering, thank them for
                # their order
                print("Thank you for your order. Please wait a moment while we calculate your order total.")

                # Exit the keep ordering question loop
                place_order = False
                break
            case _:
                print(f"Your response ({keep_ordering}) was not recognized.  Please specify (Y)es or (N)o")

# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
for item in order_list:

    # 7. Store the dictionary items as variables
    order_item_name = item["Item name"]
    order_item_qty = item["Quantity"]
    order_item_price = item["Price"]    

    # 8. Calculate the number of spaces for formatted printing
    item_spaces = 26 - len(order_item_name)
    price_spaces = 7 - len(str(order_item_price))
    
    # 9. Create space strings
    spaces_name = " " * item_spaces
    spaces_price = " " * price_spaces

    # 10. Print the item name, price, and quantity
    print(f"{order_item_name}{spaces_name}| {order_item_price}{spaces_price}| {order_item_qty} ")


# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.

#TODO make sure the float is set to the right decimal places. 
list_item_prices = [float(item["Quantity"]) * item["Price"] for item in order_list]
total_price = round(sum(list_item_prices),2)
print("----------------------------------------------")
print(f"Your Order Total is ${total_price}")
print("----------------------------------------------")

print("Thank you for your purchase.  Please visit us again!")

