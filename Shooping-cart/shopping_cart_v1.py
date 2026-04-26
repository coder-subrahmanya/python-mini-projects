#SHOPPING CART EASY MODE

cart = []

print("Welcome to my shop")
print()

print("""Menu
1. add item
2. remove item
3. show cart
4. exit""")
print()

while True:
    try:
        user_input = int(input("Choose your operation(1-4): "))
    except ValueError:
        print("Invalid entry - Please enter a number")
        print()
        continue

    if user_input == 1:
        add_item = input("Enter the item: ")

        cart.append(add_item)
        print(f"{add_item} added to cart successfully!")
        print()

    elif user_input == 2:
        remove_item = input("Enter the name of item to remove: ")

        if remove_item in cart:
            cart.remove(remove_item)
            print(f"{remove_item} removed successfully!")
            print()
        else:
            print("Item doesn't exist")

    elif user_input == 3:
        if len(cart) == 0:
            print("The cart is empty")
        else:
            for num, item in enumerate(cart):
                print(f"{num + 1}. {item}")

    elif user_input == 4:
        print("Thank you for visiting!")
        break
