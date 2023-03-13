# 5% discount
def paymentMode1(unitsPrice, misc):
    
    tuition = unitsPrice - (0.05 * unitsPrice) + misc
    return tuition


# 3% discount
def paymentMode2(unitsPrice, misc):

    tuition = unitsPrice - (0.03 * unitsPrice) + misc
    return tuition


def paymentMode3(unitsPrice, misc):

    tuition = unitsPrice + misc
    return tuition