# python-challenge-1
First python homework assignment to create a simple menu ordering system

Repository Location: [https://github.com/jjmccarty/python-challenge-1.git](https://github.com/jjmccarty/python-challenge-1.git)


## Welcome to the variety food truck!
This basic python ordering system provides a simple interface for allowing customers to order from a pre-determined dictionary menu.  

### Initial Menu Category Selections

Users are initially asked to select **by number** from a list menu item categories.  For example:
```
From which menu would you like to order?  
1: Snacks  
2: Meals  
3: Drinks  
4: Dessert  
```
### Menu Category Item Selection

Successful selection of a menu category will provide the listing of menu items with pricing options for the user to select from.  For example if the **1: Meals** category was selected the user might see the following *example* options. 
```
Item # | Item name        | Price  
-------|------------------|-------  
1      | Burrito          | $4.49  
2      | Teriyaki Chicken | $9.99  
3      | Sushi            | $7.49  
4      | Pad Thai         | $6.99  
5      | Pizza - Cheese   | $10.99
6      | Pizza - Chicken  | $8.49  
```
As with menu category selection the user will be prompted to select their desired menu item by number.  Entry of any menu category item  that does not match a listed item number will result in a message to the user and the system will ask the user if they wish to continue ordering menu items.  

Successful selection will prompt the user to enter the quantity desired for that menu item.  Handling for the quantity selection is as follows.  

1. The system will only accept valid numbers as defined by `isdigit()`.  If the entry fails the `isdigit()` check a quantity of 1 will be entered for the user by the system
2. Entry of a quantity for an item already added to the order list will update the quanity of that item instead of producing another order list entry
3. Entry of 0 for the quanity will result in the order item not being added or updated. 

>*Please note that the requirements in #2 and #3 of the above rules were not specified in the original instructions, but inferred to better streamline the input by the user and simplification of the order summarization*

User selected menu items are stored in a list of dictionary items with the following expected format and types of key/value pairs

```
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
```

Users will continue to be asked if they will to continue ordering menu items until they select 'No' when prompted.  For example:

> Would you like to keep ordering? (Y)es or (N)o: Y  
 
The system will accept 'Y' or 'N' and either keep iterating through the order selection process for a 'Y' response, or move to the order summary process for a 'N' response.  Note responses are not case sensistive.

### Order summarization and Total calculation
Once the user has confirmed the order selection is complete the system will caluculate the order total based on the following. 

```
    for each order item in the order item list      
        multiple the order item price by the quantity selected      
    
    Total = the sum of all price/quantity selections  
```
Taxation was not specified for the exercise.

Once calculated the order summary and title will be presented to customer in a formatted manner
For example:

```
Item name       | Price        | Qty  
----------------|--------------|-------  
Burrito       | $4.49        | 1  
Soda - Medium | $0.89        | 2
---------------------------------------
Your Order Total is $6.27
---------------------------------------
Thank you for your purchase. Please visit us again!
```