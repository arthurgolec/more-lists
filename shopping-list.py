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
def shopping_list():
    print("Hey pal! I'm not very good at this, so if you want to delete something, type in 'delete', and if you want to leave, type 'escape', ok? Have fun!")
    while True:
        new_item = input("What do you wanna add to the list?  ")
        if new_item == "delete":
            delete_item = input("What do you want to delete?  ")
            shopping_list.remove(delete_item)
        if new_item == "escape":
            print(shopping_list)
        else:
            shopping_list.apprend(new_item)