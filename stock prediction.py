import numpy as np
import math
import cPickle as pickle
import os


def stochastic_oscillator(prices, period):
    min_p = prices[-period:].min()
    max_p = prices[-period:].max()

    if min_p == max_p:
        return 0.

    return abs(100. * (prices[-1] - min_p) / (max_p - min_p))

# Head ends here
def printTransactions(m, k, d, name, owned, prices):
    output = []

    prices = np.array(prices)
    deviations = prices.std(1)

    to_buy = []
    for i in reversed(np.argsort(deviations)):
        sa = stochastic_oscillator(prices[i], 3)

        if sa >= 80. and owned[i]:
            output.append("%s %s %s" % (
                name[i], 'SELL', owned[i]))

        elif sa <= 20. and m:
            to_buy.append((i, sa, prices[i][-1]))

    #to_buy.sort(key=lambda v: v[-2], reverse=True)

    for i, sa, price in to_buy:
        num = int(m / int(math.ceil(price)))
        if num:
            output.append("%s %s %s" % (
                name[i], 'BUY', num))
            m -= (num * int(math.ceil(price)))

    return output

def parse_step():
    m, k, d = [float(i) for i in raw_input().strip().split()]

    k = int(k)
    d = int(d)
    names = []
    owned = []
    prices = []
    for data in range(k):
        temp = raw_input().strip().split()
        names.append(temp[0])
        owned.append(int(temp[1]))
        prices.append([float(i) for i in temp[2:7]])

    return m, k, d, names, owned, prices

def load_history():
    prices_history = {}
    try:
        with open('prices_history.pkl', 'r') as f:
            prices_history = pickle.load(f)
    except IOError:
        pass

    return prices_history

def save_history(k, d, names, prices):
    prices_history = {}

    for i in range(k):
        prices_history[names[i]] = prices[i]

    prices_history['_days'] = d

    with open('prices_history.pkl', 'w') as f:
        pickle.dump(prices_history, f)

def add_history(k, d, names, prices):
    prices_history = load_history()

    if prices_history and prices_history['_days'] > d:
        for i in range(k):
            hprices = prices_history.get(names[i])
            if hprices:
                hprices.append(prices[i][-1])
                prices[i] = hprices

    return prices

def remove_history():
    try:
        os.remove('prices_history.pkl')
    except:
        pass

# Tail starts here
if __name__ == '__main__':

    m, k, d, names, owned, prices = parse_step()
    #prices = add_history(k, d, names, prices)

    output = printTransactions(m, k, d, names, owned, prices)

    #save_history(k, d, names, prices)

    print len(output)
    for line in output:
        print line