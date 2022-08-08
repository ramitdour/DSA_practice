from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n  = len(nums)
        nf = n // 3
        
        dict1 = {}
        ret_list = []

        for i in range(len(nums)):
            if nums[i] not in dict1:
                dict1[nums[i]] = 1
            else:
                dict1[nums[i]] += 1

       

        # print(dict1)

        for k,v in dict1.items():
            if v > nf:
                ret_list.append(k)
           

        return ret_list

        pass


s1 = Solution()

print(s1.majorityElement(nums = [3,2,3]))   # [3]

print(s1.majorityElement(nums = [1]))       # [1]

print(s1.majorityElement(nums = [1,2]))     # [1,2]

print(s1.majorityElement(nums = [1,2,3,3]))   # [1,2,3]