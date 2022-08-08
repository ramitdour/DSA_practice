from http.client import ImproperConnectionState
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        dict1 = {}

        for i in range(len(nums)):
            if nums[i] not in dict1:
                dict1[nums[i]] = 1
            else:
                dict1[nums[i]] += 1

        maxk,maxv = 0,0

        # print(dict1)

        for k,v in dict1.items():
            if v > maxv :
                maxv = v
                maxk = k
            elif v == maxv :
                if k > maxk:
                    maxk = k

        return maxk
            

s1 = Solution()

print(s1.majorityElement(nums = [3,2,3])) #3
print(s1.majorityElement(nums = [2,2,1,1,1,2,2])) #2

print(s1.majorityElement(nums = [4,4,2,4,3,4,4,3,2,4])) #4
print(s1.majorityElement(nums = [])) #3
print(s1.majorityElement(nums = [0])) #3