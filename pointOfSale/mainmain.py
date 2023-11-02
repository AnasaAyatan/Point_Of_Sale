# This variable is written all in caps to indicate it is a constant
# It is declared as a global so that it is easy to find in our code in case sales tax changes
SALES_TAX = 0.15

def get_prices():
    prices = []
    while True:
        try:
            price = float(input("Enter price of item (enter 0 to finish): "))
            if price == 0:
                break
            elif price < 0:
                print("Price cannot be negative. Please enter a valid price.")
            else:
                prices.append(price)
        except ValueError:
            print("Invalid input. Please enter a valid price.")
    return prices

def calculate_totals(prices):
    subtotal = sum(prices)
    sales_tax_due = subtotal * SALES_TAX
    total = subtotal + sales_tax_due
    return subtotal, sales_tax_due, total

def print_receipt(prices, subtotal, sales_tax_due, total):
    print("Receipt:")
    for i, price in enumerate(prices, start=1):
        print(f"Item #{i}: ${price:.2f}")
    print(f"{'Subtotal':10s} ${subtotal:.2f}")
    print(f"{'Sales Tax':10s} ${sales_tax_due:.2f}")
    print(f"{'Total':10s} ${total:.2f}")

def main():
    item_prices = get_prices()
    if not item_prices:
        print("No items entered. Exiting.")
        return
    subtotal, sales_tax_due, total = calculate_totals(item_prices)
    print_receipt(item_prices, subtotal, sales_tax_due, total)

main()

an example output would be:
enter price of item: 10
enter price of item: 12.55
enter price of item: 45.10
enter price of item: 10.05
enter price of item: blah
Error : Incorrect input. Please try again...
enter price of item: 0
--------------------
Item #1 $10.00
Item #2 $12.55
Item #3 $45.10
Item #4 $10.05
Subtotal: $77.70
Sales Tax: $11.65
Total: $89.36

the program is not prompting the user to enter another price