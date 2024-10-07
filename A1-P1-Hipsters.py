#Program 1 – Hipster's Local Vinyl Records
#Hipster’s Local Vinyl Records sell and hand-deliver vinyl records to their customers.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # seting tax to a constant of 14% and the other vars to 0 for clean numbers
    TAX                 = 0.14  # <--- 14%                ] <---
    DELIVERY_REATE       = 15   # <--- 15$ per kilometer  ]    |--- THESE VALUES ARE CONSTANTS

    kilometersCost      = 0 # ]
    recordsCost         = 0 # ] <--- These values are going to change as they will be entered by the user. Setting to 0 for clean calculations

    # custom shop welcom message
    print("Hipster's Local Vinyl Records - Customer Order Details")

    """
    getting the user input for the name. I am using a while loop with a func ' if customerName.replace(' ', '').isalpha(): ' the breakdown of this is we are using the replace() func to remove any and all spaces from the name value. 
    We need this because names have spaces and are not considerd alphabetic chars. Then .isalpha(): runs to check if the input only contains letters. Ex. a, b, c... if there are numbers found it prints the error message and has the user enter again till it reads a letter only name
    If nothing wrong is found it breaks and contuines the prog.

    for the format of ' replace(' ', '')' to help you understand my understanding. its like a way to replace old with new. so when a name is enterd it checks the text thats stored in memoury from the customerName var and looks for every instance of a space it can find.
    it then removes and replaces with with an empty string ''. so Joe Cool would become JoeCool. it does this so the string can become fully alphabetic and isalpha() can check for any numbers in the string.
    """

    # getting user input for the name of the customer. controlling it in a while loop with a func to check if the input is a letter only name
    while True:
        customerName = input("\nEnter the customer's name: ")
        if customerName.replace(' ', '').isalpha(): # <--- removeing spaces from entered name, and checking for any numbers that could have been entered.
            break
        else:
            print("Invalid input. Please enter a valid name.")

    """ 
    getting the user input for the kilometers and records cost. I am using a while loop with a try: func in both inputs to make sure the user enters a valid number and not a text value. 
    If they do it is caught by the ValueError exception and the user is asked to enter a valid number with a error message and it will be satisfed when a number is entered.
    """

    # getting user input for the kilometers and records cost. controlling it in a while loop with a try: func in both inputs to make sure the user enters a valid number and not a text value.
    while True:
        try:
            kilometersCost = float(input("Enter the distance in kilometers for the delivery ( Ex. 4.5 ): "))  # <-- this value is in kilometers
            break  # <--- the loop will exit if the input is valid ( does the same for the other recordsCost value below )
        except ValueError:
            print("Invalid input. Please enter a valid number for the 'Delivery Distance' in kilometers. ( Ex. 4.5 ).")

    while True:
        try:
            recordsCost = float(input("Enter the cost of the records purchased ( Ex. 129.95 ): "))
            break  
        except ValueError:
            print("Invalid input. Please enter a valid number for the 'Cost of the records purchased' ( Ex. 129.95 ).")

    # Calcs from the user input
    deliveryCost = kilometersCost * DELIVERY_REATE
    totalReccordsCost = recordsCost + (recordsCost * TAX) # <--- getting the total cost of the records with tax
    totalCost = deliveryCost + totalReccordsCost


    # printing the summary of the values calc from the user input
    print(f"\nPurchase summary for {customerName}")
    print(f"Develivery cost : $""{:.2f}".format(deliveryCost))
    print(f"Purchase cost   : $""{:.2f}".format(totalReccordsCost))
    print(f"Total cost      : $""{:.2f}".format(totalCost))

    # YOUR CODE ENDS HERE

main()