def deluxeAddOns(base,a,b,c):
    print("Cheese\nBacon Ham\nOnions Chili ")
    addOnsPrice = a + b + c
    finalPrice = base + addOnsPrice

    update = {
        "addOns Prices": [a,b,c],
        "Bill": finalPrice
    }

    return update
  
    
def specialAddOns(base,a,b,c,d,e):
    print("Cheese\nPepper\nBacon Ham\nMushroom\nOnions Chili")
    addOnsPrice = a + b + c + d + e
    finalPrice = base + addOnsPrice

    update = {
        "addOns Prices": [a,b,c,d,e],
        "Bill": finalPrice,
    }

    return update


def primoAddOns(base,a,b,c,d,e,f,g,h):
    print("Mozzarella Cheese\nPepper\nBacon Ham\nMushroom\nOnions Chili\nTomato\nPineapple\nSalami")
    addOnsPrice = a + b + c + d + e + f + g + h
    finalPrice = base + addOnsPrice

    update = {
        "addOns Prices": [a,b,c,d,e,f,g,h],
        "Bill": finalPrice
    }

    return update
