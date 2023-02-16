# Module 1 as customer, the user is a customer - able to buy from the lists below

# This function lets me print product lists easily
def stockPrinter(num, product, price,len):
    while num != len:
        print("|", num+1 ,"|" + product[num] + ":\t\t₱", price[num])
        num += 1

dairy = ["Fresh Milk", "NAN Gold", "Promil Gold"]
dairyPrice = [150.0, 1590.0, 1480.0]

wetGoods = ["Ground Beef", "Chicken Wings", "Pork Knuckles"]
wetGoodsPrice = [450.0, 280.0, 350.0]

print("\nWelcome, our dear customer!")

custCart = []
cartValue = []
multiplier = []

# This function is for taking user's order
def custBuying(custCart,cartValue,multiplier):

    print("\nAVAILABLE PRODUCTS:")
    print("\n(0) DAIRY\n")
    stockPrinter(0,dairy,dairyPrice,len(dairy))
    print("\n(1) WET GOODS\n")
    stockPrinter(0,wetGoods,wetGoodsPrice,len(wetGoods))

    while True:
        productGroup = input("*Enter the number code of product category: ")

        if productGroup == '0':
            order = int(input("*Enter the number code of your order: "))
            quantity = int(input("*Enter quantity of products: "))
            order -= 1
            custCart.append(dairy[order])
            cartValue.append(dairyPrice[order])
            multiplier.append(quantity)

            print("You added ", quantity ," " + dairy[order] + " to your cart")
            print(multiplier[-1], custCart[-1],":\t₱", cartValue[-1]*quantity)


        elif productGroup == '1':
            order = int(input("*Enter the number code of your order: "))
            quantity = int(input("*Enter quantity of products: "))
            order -= 1
            custCart.append(wetGoods[order])
            cartValue.append(wetGoodsPrice[order])
            multiplier.append(quantity)

            print("You added ", quantity ," " + wetGoods[order] + " to your cart")
            print(multiplier[-1], custCart[-1],":\t₱", cartValue[-1]*quantity)

        else:
            print("\nInvalid input.")
            custBuying(custCart,cartValue,multiplier)

        nextStep = input("\nEnter \'b\' to proceed to checkout\n\tor\npress any key to add another product:\n")

        if nextStep == 'b':
            custCheckout(custCart,cartValue,multiplier)

        else:
            custBuying(custCart,cartValue,multiplier)
            
# This function is to finalize user's orders
def custCheckout(product,price,multiplier):
    num = 0
    totalPrice = 0
    print("\n")

    while num != len(product):
        print("|",multiplier[num],"|" + product[num] + ":\t\t₱", price[num]*multiplier[num])
        totalPrice = totalPrice + (price[num]*multiplier[num])
        num += 1

    print("Total Price: ₱", totalPrice)
    input("*Press any key to end the program.")

custBuying(custCart,cartValue,multiplier)