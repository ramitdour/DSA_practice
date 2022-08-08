from http.client import ImproperConnectionState
from tkinter import N
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)

        def swap(a,b):
            temp = nums[a]
            nums[a] = nums[b]
            nums[b] = temp

        # bubble sort Worst O(n^2) best  O(n)
        for i in range( n - 2 , -1 ,-1):
            for j in range(i):
                if nums[j] > nums[j + 1]:
                    swap(j,j+1)

        print(nums)
        # #pointer 
        # i = 0 
        # p = 0

        

        # while(p < n - 2):
        #     # bubble sort
        
            
        #     if (nums[i] > nums[i+1]):
        #         print(nums)
        #         swap(i , i + 1)

               

        #     else:
        #         p = i 


        #     i += 1


       
            

s1 = Solution()

# print(s1.majorityElement(nums = [3,2,3])) #3
# print(s1.majorityElement(nums = [2,2,1,1,1,2,2])) #2

print(s1.majorityElement(nums = [4,4,2,4,3,4,4,3,2,4])) #4
# print(s1.majorityElement(nums = [])) #3
# print(s1.majorityElement(nums = [0])) #3