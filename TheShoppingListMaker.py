#Objective: The aim of this assignment is to create a program that helps users make a shopping list.

#Task 1 Write a function that lets the user add items to a list
store_trip = []

def add_list(food_list):
   item = input("What item would you like to add? ")
   food_list.append(item)
   
#Task 2 Include a function to remove items from the list

def remove_list(food_list):
    item = input("Which item would you like to remove? ")
    if item in food_list:
        food_list.remove(item)
    print(f"The item {food_list} has been removed from your list")


#Task 3 Add a function that prints out the entire list in a formatted way 

def print_list(food_list):
    if not food_list:
        print("The list is empty")
    else:
        print("List items: ")
        for i, item in enumerate(food_list):
            print(f"{i+1}.{item}")
 

while True:

    print("Action Items are \n"\
            "add item\n"\
            "remove item\n"\
            "print list\n"\
            "exit \n")

    action = input("Please select an action: ")

    if action.lower() == "Add item":
        add_list(store_trip)

    elif action.lower() == "Remove item":
        remove_list(store_trip)

    elif action.lower() == "Print list":
        print_list(store_trip)
        
    elif action.lower() == "Exit":
        print("Thank you for using our list maker!")
        break
    else:
        print("Invalid action: please select a valid action.")
        