from typing import List


# (Extended Boyer Moore’s Voting Algorithm


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n  = len(nums)
        nf = n // 3
        
        num1 = -110
        num2 = -110

        count1 = 0
        count2 = 0

        for i in range(n):

            if num1 == nums[i] :
                count1 += 1

            elif num2 == nums[i] :
                count2 += 1


            elif count1 == 0 :
                num1 = nums[i]
                count1 = 1


            elif count2 == 0 :
                num2 = nums[i]
                count2 = 1

            else:
                count1 -= 1
                count2 -= 1


        count1 = 0
        count2 = 0


        for i in range(n):
            if nums[i] == num1:
                count1 += 1
            elif nums[i] == num2:
                count2 += 1
        return_arr = []
        if count1 > nf : return_arr.append(num1) 
        if count2 > nf : return_arr.append(num2) 

        return return_arr

        


s1 = Solution()

print(s1.majorityElement(nums = [3,2,3]))   # [3]

print(s1.majorityElement(nums = [1]))       # [1]

print(s1.majorityElement(nums = [1,2]))     # [1,2]

print(s1.majorityElement(nums = [1,2,3,3]))   # [3]

print(s1.majorityElement(nums = [1,1,1,3,3,2,2,2]))   # [1,2]