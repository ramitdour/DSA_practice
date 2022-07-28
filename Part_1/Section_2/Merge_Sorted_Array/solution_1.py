from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1

        # for i in range(m + n):
        #     print(i,nums1 , nums2)
        #     if (len(nums2) > 0):
        #         if nums1[i] >= nums2[0]:
        #             print( "a",i,nums1[i])
        #             nums1.pop(-1)
        #             nums1.insert(i , nums2.pop(0))
        #         elif(nums1[i] < nums2[0] and nums1[i] == 0 and i <= m):
        #             nums1.pop(-1)
        #             nums1.insert(i + i , nums2.pop(0))

        #         elif(nums1[i] < nums2[0] and nums1[i] == 0 ):
        #             print("b",i,nums1[i])
        #             nums1.pop(-1)
        #             nums1.insert(i , nums2.pop(0))

        i_n1 = 0

        # while len(nums2) > 0:
        #     print(i_n1 , nums1 ,nums2)
        #     if nums1[i_n1] >= nums2[0]:
        #         nums1.pop(-1)
        #         nums1.insert( i_n1, nums2.pop(0))
        #     if nums1[i_n1] == 0 and (i_n1  > m - 1):
        #         nums1.pop(-1)
        #         nums1.insert( i_n1  , nums2.pop(0))

        #     i_n1 = i_n1 + 1

        while len(nums2) > 0:
            print(i_n1 , nums1 ,nums2)
            if nums2[0] <= nums1[i_n1]:
                nums1.pop(-1)
                nums1.insert( i_n1, nums2.pop(0))
            if i_n1 > len(nums1) - len(nums2) - 1:
                nums1.pop(-1)
                nums1.insert( i_n1, nums2.pop(0))

            i_n1 = i_n1 + 1
                    
        return nums1
        
s1 = Solution()

print(s1.merge( nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
print(s1.merge(nums1 = [1], m = 1, nums2 = [], n = 0))
print(s1.merge(nums1 = [0], m = 0, nums2 = [1], n = 1))
print(s1.merge(nums1 = [2,0], m = 1, nums2 = [1], n = 1))
print(s1.merge(nums1 = [-1,0,0,3,3,3,0,0,0], m = 6, nums2 = [1,2,2], n = 3))
print(s1.merge(nums1 = [-1,3,0,0,0,0,0], m = 2, nums2 = [0,0,1,2,3], n = 5))

# did too many mistakes

