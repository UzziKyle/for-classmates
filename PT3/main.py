import pizza

addOns = {
    "Cheese" : 100,
    "Mozzarella Cheese" : 150,
    "Pepper" : 80,
    "Bacon Ham" : 120,
    "Mushroom" : 130,
    "Onions Chili" : 110,
    "Tomato" : 90,
    "Pineapple" : 100,
    "Salami" : 120
    }

def finalOutput(finalPrice):
    finalPizzaChoice = {
        "Customer" : custName.capitalize(),
        "Pizza Preference": prefPizza.capitalize(),
        "Base": base
    }
    
    finalPizzaChoice.update(finalPrice)
    
    print("\nCustomer: " + finalPizzaChoice["Customer"])
    print("Pizza Preference: " + finalPizzaChoice["Pizza Preference"])
    print("Bill: " + str(finalPizzaChoice["Bill"]))

custName = input("*Enter the Customers Name: ").strip()
prefPizza = input("*Preferred Pizza: ").strip().lower()
base = 450
print("Details:\nBase: " + str(base))


if prefPizza == "deluxe":
    finalOutput(pizza.deluxeAddOns(base, addOns["Cheese"], addOns["Bacon Ham"], addOns["Onions Chili"]))

elif prefPizza == "special":
    finalOutput(pizza.specialAddOns(base, addOns["Cheese"], addOns["Pepper"], addOns["Bacon Ham"],addOns["Mushroom"], addOns["Onions Chili"]))

elif prefPizza == "primo":
    finalOutput(pizza.primoAddOns(base, addOns["Mozzarella Cheese"], addOns["Pepper"], addOns["Bacon Ham"], addOns["Mushroom"], addOns["Onions Chili"], addOns["Tomato"], addOns["Pineapple"], addOns["Salami"]))


