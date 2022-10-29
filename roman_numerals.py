# XXVII
# XXIV
#
values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

from functools import reduce

class Solution:

    # Subtract or not
    def romanToInt(self, s: str) -> int:

        total = 0
        for i in range(len(s)):
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total

    def romanToIntLong(self, s: str) -> int:
        if not s:
            return 0

        total = 0

        def getTotal(s: str) -> int:
            return reduce(lambda a, b: a + values[b], s, 0)

        beg = 0
        end = 0
        part = s[0]
        i = 1
        while i < len(s):

            next = s[i]

            if part == "":
                part += next
            elif values[part[-1]] >= values[next]:
                part += next
            else:
                last = part[-1]
                total += getTotal(part[:-1]) + values[next] - values[last]
                part = ""

            i += 1

        return total + getTotal(part)


sol = Solution()
print( sol.romanToInt("XXVII"))