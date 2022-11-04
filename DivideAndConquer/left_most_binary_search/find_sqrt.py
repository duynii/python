# 69. Sqrt(x)  69. Sqrt(x)
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
#
# You must not use any built-in exponent function or operator.
#
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
# Hints
# Try exploring all integers. (Credits: @annujoshi)
# Use the sorted property of integers to reduced the search space. (Credits: @annujoshi)
class Solution:
    def mySqrt(self, x: int) -> int:

        def search():
            l, r = 0, (2 ** 31) - 1

            while l < r:
                m = (l + r) // 2
                if m * m < x:
                    l = m + 1
                else:
                    r = m
            return l

        n = search()

        return n if n * n == x else n - 1