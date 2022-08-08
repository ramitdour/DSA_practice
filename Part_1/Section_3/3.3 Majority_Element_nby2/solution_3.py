from typing import List

# Moore’s Voting Algorithm

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)

        count = 0
        candidate = nums[0]

        for i in range(n):
            if(count == 0):
                candidate = nums[i]
               
            if nums[i] == candidate :
                count += 1
            else:
                #if  nums[i] != candidate
                if count > 0:
                    count -= 1
                else:
                    candidate = nums[i]

        return candidate
        

       
            

s1 = Solution()

# print(s1.majorityElement(nums = [3,2,3])) #3
# print(s1.majorityElement(nums = [2,2,1,1,1,2,2])) #2

# print(s1.majorityElement(nums = [4,4,2,4,3,4,4,3,2,4])) #4
print(s1.majorityElement(nums = [6,5,5])) #5
# print(s1.majorityElement(nums = [0])) #0