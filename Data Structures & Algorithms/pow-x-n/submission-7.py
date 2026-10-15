import functools

class Solution:
    def myPow(self, x: float, n: int) -> float:

        res = 1

        if n == 0:
            return 1

        if n < 0:
            n = - n
            x = 1/x

        def pow(x, n):

            if n == 1:
                return x

            if n % 2 == 1:
                return (pow(x, n // 2) ** 2) * x

            return (pow(x, n // 2) ** 2)

        return pow(x, n)        