# Module 1 as customer, the user is a customer - able to buy from the lists below

# This function lets me print product lists easily
def stockPrinter(num, product, price):
    while num != len(dairy):
        print("|", num+1 ,"|" + product[num] + ":\t\t₱", price[num])
        num += 1

dairy = ["Fresh Milk", "NAN Gold", "Promil Gold"]
dairyPrice = [150.0, 1590.0, 1480.0]

wetGoods = ["Ground Beef", "Chicken Wings", "Pork Knuckles"]
wetGoodsPrice = [450.0, 280.0, 350.0]

print("\nWelcome, our dear customer!")

custCart = []

# This function is for taking user's order
def custBuying(custCart):

    print("\nAVAILABLE PRODUCTS:")
    print("\n(0)Dairy:")
    stockPrinter(0,dairy,dairyPrice)
    print("\n(1)Wet Goods:")
    stockPrinter(0,wetGoods,wetGoodsPrice)

    while True:
        productGroup = input("Enter the number code of product category: ")

        if productGroup == '0':
            order = int(input("Enter the number code of your order: "))
            order -= 1
            custCart.append([dairy[order],dairyPrice[order]])

            print("You added " + dairy[order] + " to your cart")
            print(custCart)


        elif productGroup == '1':
            order = int(input("Enter the number code of your order: "))
            order -= 1
            custCart.append([wetGoods[order],wetGoodsPrice[order]])

            print("You added " + wetGoods[order] + " to your cart")
            print(custCart)

        else:
            print("\nInvalid input.")
            custBuying(custCart)

        nextStep = input("\nEnter \'b\' to proceed to checkout\n\tor\npress any key to add another product:\n")

        if nextStep == 'b':
            custCheckout(custCart)

        else:
            custBuying(custCart)
            
# This function is to finalize user's orders
def custCheckout(custCart):
    print(custCart)

custBuying(custCart)