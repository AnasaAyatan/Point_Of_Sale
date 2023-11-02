# this variable is written all in caps to indicate it is a constant
# it is declared as a global so that it is easy to find in our code in case sales tax changes
SALES_TAX = 0.15

def getPrice():
    price = float(input("Enter price of item: "))
    return price

def printReceipt(price):
    # calculate totals
    subTotal = price
    salesTaxDue = subTotal * SALES_TAX
    total = salesTaxDue + subTotal

    # Display output to user
    print(f"{'Subtotal':10s} ${subTotal:1.2f}")
    print(f"{'Sales Tax':10s} ${salesTaxDue:1.2f}")
    print(f"{'Total':10s} ${total:1.2f}")


def main():
    price = getPrice()
    printReceipt(price)

main()

#start with the provided point of sale application (/challenge-pointOfSale)

#modify the program so that the user can enter in as many items as they want instead of just one item

#the program will continue to ask for item prices until the user enters in 0 for a price, indicating they are finished

#the program will then output each item entered, the subtotal or all entered items, the total sales tax (at 15%), and the total price

#if the user enters in anything that is incorrect input (letters, negative numbers, etc.) the program will display an error message and allow the user to try again

#an example output would be:
#enter price of item: 10
#enter price of item: 12.55
#enter price of item: 45.10
#enter price of item: 10.05
#enter price of item: blah
#Error : Incorrect input. Please try again...
#enter price of item: 0
#--------------------
#Item #1 $10.00
#Item #2 $12.55
#Item #3 $45.10
#Item #4 $10.05
#Subtotal: $77.70
#Sales Tax: $11.65
#Total: $89.36
