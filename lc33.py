'''
I love python
100% and 100%
python lets people lazy
'''
class Solution:
    def search(self, nums: 'List[int]', target: 'int') -> 'int':
        if target in nums:
            return nums.index(target)
        else:
            return -1