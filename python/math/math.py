import math
def depositProfit(deposit, rate, threshold):

    '''
    Basically it is log(ratioOfProfit, ratioOfGrowth)
    '''

    return math.ceil(math.log(threshold * 1.0 / deposit, 1.0 + rate / 100.0))

print(depositProfit(100, 20, 170))