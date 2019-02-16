'''
efficient way to implement combination
'''
import operator
import functools
class Solution:
    def ncr(self, n, r):
        r = min(r, n-r)
        numer = functools.reduce(operator.mul, range(n, n-r, -1), 1)
        denom = functools.reduce(operator.mul, range(1, r+1), 1)
        return numer / denom

    def climbStairs(self, n: 'int') -> 'int':
        answer = 0
        for i in range(int(n/2)+1):
            # print(self.ncr(n-i, n-2*i))
            answer += self.ncr(n-i, n-2*i)
        return int(answer)
