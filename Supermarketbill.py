# Build a Python-based supermarket billing system that allows users to view a list of products, add items to their cart, calculate the total bill with tax, and display a receipt.
# Functional Requirements:

#     User Interaction:
#         The system should ask for the customer’s name.
#         Display a list of available products with their prices.
#         Allow users to add multiple items to their cart.
#         Validate that the quantity entered is a valid number.
#         Display an itemized bill with total and tax before exiting.

#     Product Catalog:
#         Maintain a dictionary of products and their prices.
#         Display the product list when requested.

#     Billing and Calculations:
#         Compute the total price based on item quantities.
#         Apply a 12% tax on the total amount.
#         Display a detailed invoice with:
#             Item name
#             Quantity
#             Price per unit
#             Total price for each item
#             Total amount before and after tax

#     Receipt Format:
#         Display a well-formatted bill with store name, location, and transaction details.

#     Exit Mechanism:
#         Allow users to exit the purchase process at any time.
#         Display a "Thank you" message upon exiting.


Name=input("Enter your name:")
Lists = '''
   Apple       Rs 100/Kg
   Carrot      Rs 20/Kg
    Salt       Rs 25/kg
    Paneer     Rs 40/kg
    Maggie     Rs 12/pack
    Boost      Rs 200/bottle'''

price=0
pricelist = []
totalprice = 0
Finalprice = 0
ilist = []
qlist = []
plist = []

# Rate for each item
items = {'apple': 10, 'carrot': 8, 'salt': 25, 'paneer': 40, 'maggie': 12, 'boost': 200}

while True:
    option = input("press 1 to get item list or press 2 to exit")
    if option == '2':
        print("Thank you for shopping")
        break
    elif option == '1':
        print(Lists)

        while True:
            option = input("press 1 to get item list or press 2 to exit")
            if option == '2':
                print("Thank you for shopping")
                break
            elif option =='1':
                item=input("Enter the item:").lower()
                while True:
                    quantity_input=input("Enter the quantity:")
                    if quantity_input.isdigit():
                        quantity=int(quantity_input)
                        break
                    else:
                        print("Please enter a valid quantity.")

                if item in items:
                    price=quantity*items[item]
                    pricelist.append((item,quantity,items[item],price))
                    totalprice+=price
                    ilist.append(item)
                    qlist.append(quantity)
                    plist.append(price)
                else:
                    print("Selected item is not available. Sorry for the inconvenience.")

        if totalprice > 0:
            tax = (totalprice * 12) / 100
            finalamount = tax + totalprice

            print(25 * "=", "SK Supermarket", 25 * "=")
            print(28 * " ", "Hyderabad")
            print("Name:", Name, 30 * " ")
            print(75 * "-")
            print("sno", 10 * " ", 'items', 8 * " ", 'quantity', 8 * " ", 'price')
            for i in range(len(pricelist)):
                print(i, 13 * " ", ilist[i], 8 * " ", qlist[i], 8 * " ", plist[i])
            print(75 * "-")
            print(50 * " ", 'Total amount:', 'Rs', totalprice)
            print("Tax amount", 50 * " ", 'Rs', tax)
            print(75 * "-")
            print(50 * " ", 'Final amount:', 'Rs', finalamount)
            print(75 * "-")
            print(20 * " ", "Thank you & Visit again")
            print(75 * "-")



                



 
