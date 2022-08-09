from typing import List 
from largeDs import lx

class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        n = len(nums)
        reverse_pair = []

        for i in range(n):
            for j in range(i,n):
                if i < j and nums[i] > 2*nums[j]:
                    reverse_pair.append((nums[i],nums[j],))

        # print(reverse_pair)

        return len(reverse_pair)



s1= Solution()

print(s1.reversePairs([1,3,2,3,1])) #2
print(s1.reversePairs([3,2,1,4])) #1
print(s1.reversePairs([2,4,3,5,1])) #3

print(s1.reversePairs([38,99,45,52,1,9,2,4,5,88,45,658,27,43,3,9,82,10])) #60
# print(s1.reversePairs(lx)) #3 ##50k values


# Time Complexity: O (N^2) ( Nested Loops )

# Space Complexity:  O(1)