'''
Sort, then from first number to the first non-negative number, set the number as new target
then use 2Sum, from the target to the end of nums, find the target from both sides
''' 
class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        answer = []
        nums.sort()
        print(nums)
        for n in range(len(nums)):
            if nums[n] >= 0 :
                break
        zero_ind = n
        print("zero index is ", n)
        for i in range(zero_ind+1):
            print("i is ", i)
            if i>0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while(j<k):
                print("j, k are ", j, k)
                if (nums[j]+nums[k]) == -nums[i]:                  
                    answer.append([nums[i], nums[j], nums[k]])
                    while j<len(nums)-2 and nums[j+1] == nums[j]:
                        j += 1
                    j += 1
                    while k>i and nums[k-1] == nums[k]:
                        k -= 1
                    k -= 1
                elif (nums[j]+nums[k] > -nums[i]):
                    k-=1
                else:
                    j+=1
        print(answer)
        return answer
                
        

num = [0,0,0]
s = Solution()
s.threeSum(num)