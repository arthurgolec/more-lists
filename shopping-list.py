"""
Goal: Create code to allow a user to create a shopping list
Minimum requirements:
  * User can enter items which will be stored in the shopping list
  * User can exit item entry mode, which will cause the program to print the contents of the list
Stretch goals:
  * User can delete an item from the list
  * A command user can enter at any time to display the contents of the list

Advice:
  * You want to continue doing this for an unknown number of repetitions - what sort of loop would you use?
  * Remember that break will take you out of a loop, so you could say that if some string were entered - for instance 'exit' - you would do something and exit the loop
  * You're probably going to want to use input() and shopping_list.append()
  * Remember to do this one step at a time.
    * Make sure you can add a single item before you try to loop it.
    * Make sure the loop is working before you worry about how to do more advanced things

There is no automated checking on this one
"""

shopping_list = []
def shopping_listp():
    print("To see all commands, type 'help'")
    while True:
        new_item = input("What do you wanna add to the list?  ")
        if new_item.lower() == "list":
            print(shopping_list)
        elif new_item.lower() == "help":
            print("'list' prints the list you made, 'delete' deletes the next item you input, 'exit' exits the program, and 'help' brings up this text")
        elif new_item.lower() == "delete":
            print(shopping_list)
            delete_item = input("What do you want to delete?  ")
            shopping_list.remove(delete_item)
        elif new_item.lower() == "exit" or new_item == "escape":
            break
        else:
            shopping_list.append(new_item)
    again = input("Do you want to run this program again?  ").lower()
    if again == "yes":
        shopping_listp()
    else:
        again = input("Well, I don't know what to do, so I'll ask again. Do you want to run this program again?  ")

shopping_listp()
