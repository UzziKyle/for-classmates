# Module 1 as customer, the user is a customer - able to buy from the lists below

#Lists of product and their respective prices
dairy = ["Fresh Milk", "NAN Gold", "Promil Gold"]
dairyPrice = [150.0, 1590.0, 1480.0]
wetGoods = ["Ground Beef", "Chicken Wings", "Pork Knuckles"]
wetGoodsPrice = [450.0, 280.0, 350.0]

# List for customer's purchase
custCart = []
cartValue = []
multiplier = []

# This function lets me print product lists easily
def stockPrinter(num, product, price,len):
    while num != len:
        print("|", num+1 ,"|" + product[num] + ":\t\t₱", price[num])
        num += 1

# This function is for taking user's order
def custBuying(custCart,cartValue,multiplier):

    print("\nAVAILABLE PRODUCTS:")
    print("\n(1) DAIRY\n")
    stockPrinter(0,dairy,dairyPrice,len(dairy))
    print("\n(2) WET GOODS\n")
    stockPrinter(0,wetGoods,wetGoodsPrice,len(wetGoods))

    while True:
        productGroup = input("*Enter the number code of product category: ")

        if productGroup == '1':
            order = int(input("*Enter the number code of your order: "))
            quantity = int(input("*Enter quantity of products: "))
            order -= 1
            custCart.append(dairy[order])
            cartValue.append(dairyPrice[order])
            multiplier.append(quantity)

            print("\nYou added ", quantity ," " + dairy[order] + " to your cart")
            print(multiplier[-1], custCart[-1],":\t₱", cartValue[-1]*quantity)


        elif productGroup == '2':
            order = int(input("*Enter the number code of your order: "))
            quantity = int(input("*Enter quantity of products: "))
            order -= 1
            custCart.append(wetGoods[order])
            cartValue.append(wetGoodsPrice[order])
            multiplier.append(quantity)

            print("\nYou added ", quantity ," " + wetGoods[order] + " to your cart")
            print(multiplier[-1], custCart[-1],":\t₱", cartValue[-1]*quantity)

        else:
            print("\nInvalid input.")
            custBuying(custCart,cartValue,multiplier)

        nextStep = input("\nEnter \'b\' to proceed to checkout\n\tor\npress any key to add another product:\n")

        if nextStep == 'b':
            custCheckout(custCart,cartValue,multiplier)

        else:
            custBuying(custCart,cartValue,multiplier)
            
# This function is shows the total price of the products ordered
def custCheckout(product,price,multiplier):
    num = 0
    totalPrice = 0
    print("\nHere are your purchases:")

    while num != len(product):
        print("|",multiplier[num],"|" + product[num] + ":\t\t₱", price[num]*multiplier[num])
        totalPrice = totalPrice + (price[num]*multiplier[num])
        num += 1

    print("Total Price: \t₱", totalPrice)
    input("\n*Press any key to end the program.")
    print("\nProgram Ended")


# START of this module
print("\nWelcome, our dear customer!")
custBuying(custCart,cartValue,multiplier)