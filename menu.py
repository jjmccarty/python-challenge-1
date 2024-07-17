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

# TODO Setting up as a placeholder, dictionary values will be replaced by customer order process
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
    print("From which menu would you like to order? ")

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
    menu_category = input("Type menu number: ")

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
            print(f"The following are the available {menu_category_name} items available:")
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
            menu_category_item_num = input(f"Please enter the # for the {menu_category_name} would you like to order:")
            print(f"DEBUG selected {menu_category_item_num}")

            # 3. Check if the customer typed a number
            if menu_category_item_num.isdigit():
                # Convert the menu selection to an integer
                print(f"DEBUG {menu_category_item_num} is a digit")
                menu_category_item_num = int(menu_category_item_num)

                # 4. Check if the menu selection is in the menu items
                if menu_category_item_num < len(menu_items.keys()):
                    # Store the item name as a variable
                    menu_category_item_name = menu_items[menu_category_item_num]["Item name"]
                    print(f"DEBUG selected {menu_category_item_name} ")

                    # Ask the customer for the quantity of the menu item
                    menu_category_item_qty = input(f"How many of the {menu_category_item_name} items would you like to purchase?")
                    print(f"DEBUG {menu_category_item_qty}")

                    # Check if the quantity is a number, default to 1 if not
                    # TODO provide a message to user in this situation
                    # TODO what if the customer enters 0 or negative 
                    if not menu_category_item_qty.isdigit():
                        menu_category_item_qty = 1

                    # Add the item name, price, and quantity to the order list
                    # TODO need to format the output in a more friendly manner
                    # TODO - check if an order item is already selected and needs
                    # to just have quantiy updated.
                    new_order_item = dict()
                    new_order_item["Item name"] = menu_category_item_name
                    new_order_item["Quantity"] = menu_category_item_qty
                    new_order_item["Price"] = menu_items[menu_category_item_num]["Price"]
                    order_list.append(new_order_item)
                    print(f"Added {new_order_item["Quantity"]} of {new_order_item["Item name"]} for {new_order_item["Price"]} each to order")

                    # Tell the customer that their input isn't valid
                else:
                    print(f"The selection entered  ({menu_category_item_num}) is not a {menu_category_name} item.")

                # Tell the customer they didn't select a menu option
            else:
                print(f"The selection entered  ({menu_category_item_num}) is not a {menu_category_name} item.")

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").lower()
        
        # 5. Check the customer's input
        match keep_ordering:
            case 'y':
                #break this loop and continue to order
                break
            case 'n':
                # Complete the order
                # Since the customer decided to stop ordering, thank them for
                # their order
                print("Thank you for your order")

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

list_item_prices = [float(item["Quantity"]) * item["Price"] for item in order_list]
total_price = sum(list_item_prices)
print(f"Order Total ${total_price}")

print("Thank you for your purchase.  Please visit us again!")

