# Module 2 as merchandiser, the user is a Merchandiser - able to edit, add, and remove items on the list

# This function does what it does
def productChooser(action):
    dairy = ["Fresh Milk", "NAN Gold", "Promil Gold"]
    dairyPrice = [150.0, 1590.0, 1480.0]

    wetGoods = ["Ground Beef", "Chicken Wings", "Pork Knuckles"]
    wetGoodsPrice = [450.0, 280.0, 350.0]
    
    print("\n||DAIRY - 1|\t|WET GOODS - 2||")
    product = int(input("\n*Enter product category number: "))

    if product == 1:
        if action == 1:
            editProduct(dairy,dairyPrice)

        elif action == 2:
            addProduct(dairy,dairyPrice)

        elif action == 3:
            remProduct(dairy,dairyPrice)
    
        else:
            action()

    elif product == 2:

        if action == 1:
            editProduct(wetGoods,wetGoodsPrice)

        elif action == 2:
            addProduct(wetGoods,wetGoodsPrice)

        elif action == 3:
            remProduct(wetGoods,wetGoodsPrice)

        else:
            action()
        
    else:
        print("\nInvalid input.")
        productChooser()

# This function lets you edit product in a list
def editProduct(product,price):

    print("\nCurrent inventory")
    stockPrinter(0,product,price,len(product))

    index = int(input("*Enter the number code to be changed: ")) - 1
    changeProduct = input("*Enter new product: ")
    changeProductPrice = float(input("*Enter price: "))

    product.pop(index)
    price.pop(index)
    product.insert(index,changeProduct)
    price.insert(index,changeProductPrice)

    print("\nCurrent inventory")
    stockPrinter(0,product,price,len(product))

    endProgram()

# This function lets you add product in a list
def addProduct(product,price):

    newProduct = input("\n*Enter new product: ")
    newProductPrice = float(input("*Enter price: "))

    product.append(newProduct)
    price.append(newProductPrice)

    print("\nCurrent inventory")
    stockPrinter(0,product,price,len(product))

    endProgram()
            
# This function lets you remove product in a list
def remProduct(product,price):

    print("\nCurrent inventory")

    stockPrinter(0,product,price,len(product))

    index = int(input("*Enter the number code to be removed: ")) - 1

    product.pop(index)
    price.pop(index)

    print("\nCurrent inventory")
    stockPrinter(0,product,price,len(product))

    endProgram()
    
# This function lets you choose your action
def actions():
    print("\n||EDIT - 1|\t|ADD - 2|\t|REMOVE - 3||")
    action = int(input("\n*Enter inventory options: "))

    if action == 1 or 2 or 3:
        productChooser(action)

    else: 
        print("\nInvalid input.")
        actions()

# This function prints the lists 
def stockPrinter(num, product, price,len):
    while num != len:
        print("|", num+1 ,"|" + product[num] + ":\t\t₱", price[num])
        num += 1
        
def endProgram():
    input("\n*Press enter to end the program.\n")
    print("Program Ended")

# START of the module
print("\nWelcome, master!")
actions()