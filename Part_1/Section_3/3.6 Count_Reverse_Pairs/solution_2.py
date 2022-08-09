from typing import List 
from largeDs import lx,lx2

class Solution:


    def reversePairs(self, nums: List[int]) -> int:
        

        def merge_sorted_arr(nums: List[int], left, mid, right):

           

            if (right - left == 0) : return 0

            total = 0

            # [low,mid) [mid ,right]
            i = left
            j = mid

            for i in range(left , mid):
                while j <= right and nums[i] > 2*nums[j]:
                    j += 1
                total += (j - mid)

            # resuse var for store data
            i = left
            j = right


            while (mid <= right):
                if nums[left] >= nums[mid]:
                    nums.insert(left , nums.pop(mid))
                    left  += 1
                    mid += 1
                else:    
                    # nums[left] < nums[mid]
                    left  += 1
                    
                    
            

           

            return total

        def merg_sort(nums , left , right):

            n =  right - left + 1   # len(nums)

            if n < 2:

                return 0

            # if n == 2:

            #     return merge_sorted_arr(nums, 0, mid, 0)

            else:

                left    = left
                right   = right #n - 1
                mid     = (left + right) // 2  + 1  # very importand , yaad kar lena acche se 

                invs = merg_sort(nums , left,  mid - 1 )

                invs += merg_sort(nums , mid,  right )

                invs += merge_sorted_arr(nums, left, mid, right)

                return  invs



        return merg_sort(nums , 0, len(nums) - 1)

        
        



s1= Solution()

print(s1.reversePairs([1,3,2,3,1])) #2
print(s1.reversePairs([3,2,1,4])) #1
print(s1.reversePairs([2,4,3,5,1])) #3
print(s1.reversePairs([7,1,3,2,3,1])) #7

print(s1.reversePairs([38,99,45,52,1,9,2,4,5,88,45,658,27,43,3,9,82,10])) #60
print(s1.reversePairs([2147483647,2147483647,2147483647,2147483647,2147483647,2147483647])) # 0
# print(s1.reversePairs(lx)) #312836170 ##50k values
# print(s1.reversePairs(lx2)) #625284395  ##50k values
# print(lx2)

# still Time Limit Exceeds on leet code

