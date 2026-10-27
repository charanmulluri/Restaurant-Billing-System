# Restaurant Billing System
# Using Lists, Tuples, Loops and Functions

# Food menu using a list of tuples
menu = [
    (1, "Idli", 30),
    (2, "Dosa", 50),
    (3, "Poori", 40),
    (4, "Veg Meals", 100),
    (5, "Fried Rice", 120),
    (6, "Biryani", 150),
    (7, "Tea", 15),
    (8, "Coffee", 20)
]

# Store daily sales and receipts
daily_sales = []
bill_number = 1


# Function to display the food menu
def display_menu():
    print("\n========== RESTAURANT MENU ==========")
    print("Item No.   Food Name          Price")
    print("-------------------------------------")

    for item in menu:
        print(f"{item[0]:<11}{item[1]:<18}Rs.{item[2]}")

    print("-------------------------------------")


# Function to find an item in the menu
def find_item(item_number):
    for item in menu:
        if item[0] == item_number:
            return item
    return None


# Function to add a new food item
def add_food_item():
    name = input("Enter food name: ").strip()

    if name == "":
        print("Food name cannot be empty.")
        return

    try:
        price = float(input("Enter food price: "))

        if price <= 0:
            print("Price must be greater than zero.")
            return

        new_number = max(item[0] for item in menu) + 1
        menu.append((new_number, name, price))

        print("Food item added successfully!")

    except ValueError:
        print("Please enter a valid price.")


# Function to take customer orders
def take_order():
    order = []

    display_menu()

    print("\nEnter item number and quantity.")
    print("Enter 0 as item number to finish ordering.")

    while True:
        try:
            item_number = int(input("\nEnter item number: "))

            if item_number == 0:
                break

            item = find_item(item_number)

            if item is None:
                print("Invalid item number. Try again.")
                continue

            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue

            # Store item details as a tuple
            order.append((item[1], item[2], quantity))

            print(item[1], "added to order.")

        except ValueError:
            print("Please enter valid numbers.")

    return order


# Function to calculate the bill
def calculate_bill(order):
    subtotal = 0

    print("\n============= BILL DETAILS =============")
    print(f"{'Item':<18}{'Price':>8}{'Qty':>6}{'Total':>10}")
    print("-----------------------------------------")

    for item in order:
        name, price, quantity = item
        total = price * quantity
        subtotal += total

        print(f"{name:<18}{price:>8.2f}{quantity:>6}{total:>10.2f}")

    # Apply discount when subtotal is Rs.500 or more
    if subtotal >= 500:
        discount = subtotal * 0.10
    else:
        discount = 0

    final_bill = subtotal - discount

    print("-----------------------------------------")
    print(f"Subtotal:          Rs.{subtotal:.2f}")
    print(f"Discount:          Rs.{discount:.2f}")
    print(f"Final Bill:        Rs.{final_bill:.2f}")
    print("=========================================")

    return subtotal, discount, final_bill


# Function to generate the receipt
def generate_receipt(order, subtotal, discount, final_bill, number):
    print("\n================================")
    print("       RESTAURANT RECEIPT")
    print("================================")
    print("Bill Number:", number)

    for item in order:
        name, price, quantity = item
        print(f"{name} x {quantity} = Rs.{price * quantity:.2f}")

    print("--------------------------------")
    print(f"Subtotal:   Rs.{subtotal:.2f}")
    print(f"Discount:   Rs.{discount:.2f}")
    print(f"Final Bill: Rs.{final_bill:.2f}")
    print("================================")
    print("       Thank You! Visit Again")
    print("================================")


# Function to display daily sales
def show_daily_sales():
    print("\n========== DAILY SALES REPORT ==========")

    if len(daily_sales) == 0:
        print("No sales recorded today.")
        return

    total_bills = len(daily_sales)
    total_revenue = 0

    for sale in daily_sales:
        print(
            "Bill No:", sale[0],
            "| Subtotal: Rs.", f"{sale[1]:.2f}",
            "| Discount: Rs.", f"{sale[2]:.2f}",
            "| Final: Rs.", f"{sale[3]:.2f}"
        )

        total_revenue += sale[3]

    print("----------------------------------------")
    print("Total Bills:", total_bills)
    print(f"Total Revenue: Rs.{total_revenue:.2f}")
    print("========================================")


# Main function
def main():
    global bill_number

    while True:
        print("\n========== RESTAURANT BILLING SYSTEM ==========")
        print("1. Display Food Menu")
        print("2. Add Food Item")
        print("3. Take Customer Order")
        print("4. View Daily Sales")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_menu()

        elif choice == "2":
            add_food_item()

        elif choice == "3":
            order = take_order()

            if len(order) == 0:
                print("No items ordered.")
                continue

            subtotal, discount, final_bill = calculate_bill(order)

            generate_receipt(
                order,
                subtotal,
                discount,
                final_bill,
                bill_number
            )

            # Store sales information as a tuple
            daily_sales.append(
                (bill_number, subtotal, discount, final_bill)
            )

            bill_number += 1

        elif choice == "4":
            show_daily_sales()

        elif choice == "5":
            print("Thank you for using Restaurant Billing System!")
            break

        else:
            print("Invalid choice. Please select 1 to 5.")


# Start the program
if __name__ == "__main__":
    main()