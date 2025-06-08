def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if not choice.isdigit():
            print("invalid input enter a number between 1 and 4")
            continue
        choice = int(choice)
        if choice == 1:
            # Prompt for and add an item
            item = input("Enter the item to add: ")
            if item:
                if item in shopping_list:
                    print("the item is already on the list")
                else:
                    shopping_list.append(item)
            else:
                print("you must enter an item")
            pass
        elif choice == 2:
            # Prompt for and remove an item
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print("item not found in the shopping list.")
            pass
        elif choice == 3:
            # Display the shopping list
            if shopping_list != []:
                print("shopping list items:")
                for item in shopping_list:
                    print(item)
            else:
                print("there are no items in the shopping list")
            pass
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()