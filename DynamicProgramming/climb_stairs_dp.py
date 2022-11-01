# You are climbing a staircase . It takes n steps to reach the
# top
# You can take 1 step or 2 steps. Find how many distinct way to get to the top


# Draw the binary tree


class Soln:

    @staticmethod
    def climb(n: int) -> int:

        # dp =
        def step(i: int, ways: int):
            if i == n:
                return 1
            elif i > n:
                return 0

            ways = step(i + 1, ways) + step(i + 2, ways)
            return ways

        return step(0, 0)


    @staticmethod
    def climbDP(n: int) -> int:

        dp = {}

        def step(i: int, ways: int):
            if i == n:
                return 1
            elif i > n:
                return 0

            if i in dp:
                return dp[i]
            else:
                dp[i] = step(i + 1, ways) + step(i + 2, ways)
            return dp[i]

        return step(0, 0)

    @staticmethod
    def climbFactorial(n: int) -> int:

        one, two = 0, 1

        for i in range(n+1):
            tmp = one
            one = one + two
            two = tmp

        return one


print(Soln.climb(1))
print(Soln.climb(2))
print(Soln.climb(3))
print(Soln.climb(5))

print(Soln.climbDP(1))
print(Soln.climbDP(2))
print(Soln.climbDP(3))
print(Soln.climbDP(5))

print(Soln.climbFactorial(1))
print(Soln.climbFactorial(2))
print(Soln.climbFactorial(3))
print(Soln.climbFactorial(5))
