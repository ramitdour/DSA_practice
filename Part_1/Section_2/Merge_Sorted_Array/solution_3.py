from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # gap method 

        for k in range(m,n+m):
            nums1[k] =  nums2.pop(0)

        gap = (m + n) // 2 + (m + n) % 2

        i , j = 0 , gap

        while gap > 0:
            
            while j < m + n :
                print(gap,i,j,nums1)
                if nums1[j] < nums1[i]:
                    # swap
                    temp = nums1[j]
                    nums1[j] = nums1[i]
                    nums1[i] = temp
                i += 1
                j += 1
            
            # (gap = 0) if (gap == 1) else  (gap = (gap // 2) + (gap % 2)) 
            if gap == 1:
                gap = 0
            else : 
                gap = (gap // 2) + (gap % 2)

            # gap = (gap // 2) + (gap % 2) # culprit for infinte loop
            
            i , j = 0 , gap
            

            
                    
        return nums1
        
s1 = Solution()
print(s1.merge(nums1 = [1,4,7,8,10,0,0,0], m = 5, nums2 = [2,3,9], n = 3))
# print(s1.merge( nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
# print(s1.merge(nums1 = [1], m = 1, nums2 = [], n = 0))
# print(s1.merge(nums1 = [0], m = 0, nums2 = [1], n = 1))
# print(s1.merge(nums1 = [2,0], m = 1, nums2 = [1], n = 1))
# print(s1.merge(nums1 = [-1,0,0,3,3,3,0,0,0], m = 6, nums2 = [1,2,2], n = 3))
# print(s1.merge(nums1 = [-1,3,0,0,0,0,0], m = 2, nums2 = [0,0,1,2,3], n = 5))

# gap method , but time sol2 = sol3


