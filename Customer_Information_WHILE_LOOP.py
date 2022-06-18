def toFixed(value, digits):
    return "%.*f" % (digits, value)

averagePurchase = 0.0
count = 0
totalAmount = 0.0

# Main Column Heading
print("===================================================================")
print("CUSTOMER PURCHASE INFORMATION")
print("===================================================================")
print("CUSTOMER NAME PURCHASE AMOUNT")
print("===================================================================")

# Initialize lcv "answer"
print("Do you wish to process a customer's information?[type 'y' or 'Y' otherwise enter 'no']")
answer = input()

# Display a blank line
print("")

# While
# Loop
# testing the lcv to enter more than one customer name and purchase amount
while answer == "y" or answer == "Y":
    
    # Input operations
    print("Enter Customer's name")
    customerName = input()
    print("How much did the customer spend on this item?")
    purchaseAmount = float(input())
    
    # keep a running total of the purchase amounts per customer
    totalAmount = totalAmount + purchaseAmount
    
    # count or tally the number of customers / purchases
    count = count + 1
    
    # Output each customer name and their purchase amount as a column
    print(customerName + " " + "$" + toFixed(purchaseAmount,2))
    
    # update lcv answer
    print("Do you wish to process a customer's information? [tyoe 'y' or 'Y' otherwise enter ' no]")
    answer = input()
    print("")
    
    # end while loop
# calculate the average purchase amount
averagePurchase = totalAmount / count

# Output operations
print("===================================================================")

# Displays the total amount of purchases for all the customers
print("Customer Total Purchases = " + "      " + "$" + toFixed(totalAmount,2))
print("===================================================================")

# Displays the Average of purchases for all the customers
print("THE AVERAGE PURCHASE PRICE = " + " " + "$" + toFixed(averagePurchase,2))
print("===================================================================")
print("THIS PROGRAM IS COMPLETE - EDITED BY firstName lastName")
print("===================================================================")

# END PROGRAM
