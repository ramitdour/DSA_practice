from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
#        class Solution {
# public:
#     void merge(vector<int>& nums1, int n, vector<int>& nums2, int m) {
#         int i = n-- + m-- - 1;
#         while(m >= 0){
#             if(n == -1 || nums2[m] >= nums1[n]) nums1[i--] = nums2[m--];
#             else nums1[i--] = nums1[n--];
#         }
#     }
# };
       
        
        # i = n + m - 1

        # n -= 1
        # m -= 1

        # while(m >= 0):
            
        #     if(n == -1 or nums1[m] >= nums2[n]):
                
        #         nums1[i] = nums2[m];
        #         i -= 1
        #         m -= 1
                
        #     else :
                
        #         nums1[i] = nums1[n];

        #         i -= 1
        #         n -= 1
                
        

        # return nums1

        last = m + n -1 
        n, m = n-1, m-1  

        while m >= 0  and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[last] = nums1[m]
                m -= 1
            else:
                nums1[last] = nums2[n]
                n -= 1
            last -= 1
        
        while n >= 0: 
            nums1[last] = nums2[n]
            last, n = last-1, n-1
        return nums1
        
s1 = Solution()
print(s1.merge(nums1 = [1,4,7,8,10,0,0,0], m = 5, nums2 = [2,3,9], n = 3))
# print(s1.merge( nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
# print(s1.merge(nums1 = [1], m = 1, nums2 = [], n = 0))
# print(s1.merge(nums1 = [0], m = 0, nums2 = [1], n = 1))
# print(s1.merge(nums1 = [2,0], m = 1, nums2 = [1], n = 1))
# print(s1.merge(nums1 = [-1,0,0,3,3,3,0,0,0], m = 6, nums2 = [1,2,2], n = 3))
# print(s1.merge(nums1 = [-1,3,0,0,0,0,0], m = 2, nums2 = [0,0,1,2,3], n = 5))

# least time solution , revisit


