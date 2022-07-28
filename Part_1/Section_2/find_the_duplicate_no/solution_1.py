from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        temp = nums[0]
        for j in range(len(nums) - 1):
            for i in range(0,len(nums) - 1 - j):
                if (nums[i] == nums[i + 1]):
                    return nums[i]
                elif(nums[i] > nums[i + 1]):
                    temp = nums[i]
                    nums[i] = nums[i + 1]
                    nums[i + 1] = temp
           

s1 = Solution()

print(s1.findDuplicate([1,3,4,2,2]))
print(s1.findDuplicate([3,1,3,4,2]))