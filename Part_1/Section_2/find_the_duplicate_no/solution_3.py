from typing import List
from large_ds import l1


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

 
        for i in range(len(nums)):
            if nums[abs(nums[i])] < 0 :
                return abs(nums[i])
            nums[abs(nums[i])] *= -1

            



s1 = Solution()

print(s1.findDuplicate([1, 3, 4, 2, 2]))
print(s1.findDuplicate([3, 1, 3, 4, 2]))
print(s1.findDuplicate([2, 5, 9, 6, 9, 3, 8, 9, 7, 1]))

print(s1.findDuplicate(l1))
