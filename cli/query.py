"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import warehouse1, warehouse2

# YOUR CODE STARTS HERE

# Get the user name
user= input("Username: ")
# Greet the user
print(f"Halo and welcome {user}, to our site!")
# Show the menu and ask to pick a choice
def start():
    print(f"You can choose what you want to do here.\n1 List items by warehouse\n2 Search an item and place an order\n3 Quit")
    choise= int(input("Put here the number what you like to do: "))
# If they pick 1
    choise_true = False # Checling if they choose nummbers from the menu
    while not choise_true:
        
        if choise == 1: 
            print(warehouse1)
            print(warehouse2)
            start()
            
# Else, if they pick 2
        elif choise == 2:
            search = input("What are you looking for?: ")
            search_item(search)
            
        
# Else, if they pick 3
        elif choise == 3:
            print("Bye!")
            exit()
# Else
        else:
            print("Invalid input")
            start()

# Thank the user for the visit



# Search an item 
def search_item(search):
    total_count = 0
    local = []

    if search in warehouse1:
        total_count += warehouse1.count(search)
        local.append("Warehouse 1")
                
    if search in warehouse2:
        total_count += warehouse1.count(search)
        local.append("Warehouse 1")

    if total_count == 0:
        print("Not in stock")
    elif len(local) == 2:
        print("Both warehouses in stock", local)
        print("Do you want to place an order?\n1 Yes\n2 No")
        buy= int(input("Put here the number what you like to do: "))
        if buy == 1:
            shopping()
        elif buy == 2:
            print("Bye!")
            exit()
        else:
            print("Invalid input you will go back to the previous")
            search_item()

    else:
        print(local[0])

# Place an order
def shopping():
    print("How many")
    quantity = int(input("Put here the number what you like to buy: "))
    if quantity > 0 and quantity <= len(warehouse1):
        print(f"You bought {quantity} items")
        print("Do you want to place an order?\n1 Yes\n2 No\n3 Go back")
        buy= int(input("Put here the number what you like to do: "))
        if buy == 1:
            shopping()
        elif buy == 2:
            print("Bye!")
            exit()
        elif buy == 3:
            start()
        else:
            print("Invalid input")
            shopping()




start()