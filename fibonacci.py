

def findFib(n):
    print("n is {0}".format(n))
    if n <= 1:
        return n
    else:
        return findFib(n-1) + findFib(n-2)


print(findFib(9))

info = {}
def memoize(func):
    def inner(num):
        if num in info:
            print("%d is already cached" % num)
            return info[num]
        else:
            info[num] = func(num)
            return info[num]

    return inner

@memoize
def fibDP(n):
    if n <= 1:
        return n
    else:
        return fibDP(n-1) + fibDP(n-2)

print(fibDP(9))

def fibArrayDP(num):
    # First number is 1 and not 0
    fib_series = [0, 1]

    for n in range(2, num+1):
        fib_series.append(fib_series[n-1] + fib_series[n-2])

    # import pdb; pdb.set_trace()
    return fib_series[num]

print("Array DP", end=' ')
print(fibArrayDP(9))
