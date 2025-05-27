#init
shoppinglist= []


def dorm_shopping():
#main
    print("Welcome to your Generic dorm shopping target list!")

    while True:
        try:
            option = int(input("Choose an option 1-4 from the menu to get started. 1.View \n2.Add \n3.Remove \n4.Quit \n5. Alphabeticalize_list \n6.Count_items"))

            if option == 1:
                print("Here is your list: ")
                print(shoppinglist)

            elif option == 2:
                print("you've chosen to add to your dorm list!")
                additem = input("enter item to be added:")
                shoppinglist.append(additem)
                print("successfully added " + additem)

            elif option == 3:
                print("you have chosen to remove something from your list")
                deleted = input ("enter the item you want to remove")
                shoppinglist.remove(deleted)
                print ("successfully removed " + deleted)

            elif option == 4:
                print("thanks good luck shopping!")
                break

            elif option ==5:
                shoppinglist.sort()
                print(shoppinglist)

            elif option ==6:
                count  = len(shoppinglist)
                print ("you have " + str(count) + " items on your list:)")

        except:
            print("ERROR: Must enter a number")

dorm_shopping()
