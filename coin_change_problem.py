import sys


mem = {}
def memoize(func):
    def inner(coins, m, V):
        if V in mem:
            return mem[V]
        else:
            result = func(coins, m, V)
            print("V: %d, m: %d, sub_res: %d" % (V, m, result))
            mem[V] = result
            return result
    return inner


# m is size of coins array (number of different coins)
@memoize
def minCoins(coins, m, V):
    # base case
    if V == 0:
        return 0

    res = sys.maxsize

    for i in range(m):
        if coins[i] <= V:
            sub_res = minCoins(coins, m, V-coins[i])


            if sub_res != sys.maxsize and sub_res + 1 < res:
                res = sub_res + 1

    return res



# Driver program to test above function
coins = [9, 6, 5, 1]
m = len(coins)
V = 11
print("Minimum coins required is", minCoins(coins, m, V))