# binary search
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # length = len(nums)
        lower_bound = 0
        upper_bound = len(nums)-1
        found = False
        while lower_bound <= upper_bound:
            midpoint = (lower_bound+upper_bound) // 2
            if target == nums[midpoint]:
                print(midpoint)
                lower_bound = midpoint
                upper_bound = midpoint
                found = True
                break
            elif target < nums[midpoint]:
                upper_bound = midpoint - 1
            else:
                lower_bound = midpoint + 1
        if found:
            while nums[upper_bound] == target:
                upper_bound += 1
            while nums[lower_bound] == target:
                lower_bound -= 1
            print(upper_bound, lower_bound)
        else:
            return [-1, -1]
