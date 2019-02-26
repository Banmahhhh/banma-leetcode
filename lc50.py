# power algorithm
# although optimization is useless
# make sure po*(x**n) = answer
class Solution:
    def power(self, x, n):
        po = 1
        while n != 0:
            if (n%2) == 1:
                po *= x
            n = (n >> 1)
            x = x*x
        return po
    def myPow(self, x: float, n: int) -> float:
        sign = 1
        if n < 0:
            n = -n
            sign = -1
        return (self.power(x, n))**sign