# This variable is written all in caps to indicate it is a constant
# It is declared as a global so that it is easy to find in our code in case sales tax changes
SALES_TAX = 0.15

# Function to get prices and store it in a list
def get_prices():
    prices = []
    item_number = 1
    while True:
        try:
            price_input = input(f"Enter price of item {item_number} (enter 0 to finish): ")
            price = float(price_input)
            if price == 0:
                break
            elif price < 0:
                print("Price cannot be negative. Please enter a valid price.")
            else:
                prices.append(price)
                item_number += 1
        except ValueError:
            print("Error: Incorrect input. Please try again...")
    return prices

# Calculate the subtotal, sales tax and total
def calculate_totals(prices):
    subtotal = sum(prices)
    sales_tax_due = subtotal * SALES_TAX
    total = subtotal + sales_tax_due
    return subtotal, sales_tax_due, total

# function to to print out the list of items and the subtotal, tax and total
def print_receipt(prices, subtotal, sales_tax_due, total):
    print("\n------------------")
    for i, price in enumerate(prices, start=1):
        print(f"Item #{i} ${price:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Sales Tax: ${sales_tax_due:.2f}")
    print(f"Total: ${total:.2f}")

# if no input found end program
def main():
    item_prices = get_prices()
    subtotal, sales_tax_due, total = calculate_totals(item_prices)
    print_receipt(item_prices, subtotal, sales_tax_due, total)

main()
