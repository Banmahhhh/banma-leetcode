'''
use log!!!! then exp!!!! range is -2^32 ~ 2^32-1!!!!!!!
kao!!!!!!!!
'''
import math
class Solution:
    def divide(self, dividend: 'int', divisor: 'int') -> 'int':
        if dividend == 0:
            answer = 0
        else: 
            positive=0
            if (dividend>0 and divisor>0) or (dividend<0 and divisor<0):
                positive = 1
            divident_log = math.log(abs(dividend))
            divisor_log = math.log(abs(divisor))
            answer = int(math.exp(divident_log - divisor_log))
            if positive == 0:
                answer = -answer
            print(answer)
        return answer
        

dividend = 7
divisor = -3
s = Solution()
s.divide(dividend, divisor)