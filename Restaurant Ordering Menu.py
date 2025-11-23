name = input("Enter your Name Please! :")

print(f"Welcome to MAXILIA MR/MRs:{name}")

# Restaurant Menu System

def show_menu():
    print("==========--MENU--===========")
    print("1. MALAI BOTI PIZZA - $1780")
    print("2. AMERICAN PIZZA  - $2200")
    print("3. SPECIAL SHAWARMA  - $260")
    print("4. Drinks - $190")
    print("5. Total Bill")
    print("==========^_^===========")

def restaurant():
    total_bill = 0
    while True:
        show_menu()
        choice = input("Please select Your choice According to the Menu: ")

        if choice == "1":
            print("You ordered a MALAI BOTI PIZZA.")
            total_bill += 1780
        elif choice == "2":
            print("You ordered a AMERICAN PIZZA.")
            total_bill += 2200
        elif choice == "3":
            print("You ordered SPECIAL SHAWARMA.")
            total_bill += 260
        elif choice == "4":
            print("You ordered Drinks.")
            total_bill += 190
        elif choice == "5":
            print("\nThank you for visiting!")
            print(f"Your total bill is: ${total_bill}")
            break
        else:
            print("Invalid choice. Please try again.")

restaurant()



