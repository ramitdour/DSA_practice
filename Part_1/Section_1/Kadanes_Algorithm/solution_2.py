class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest_sum = nums[0]
        len_arr = len(nums)
 
        for i in range(len_arr):
            current_sum = 0
            
            # print(nums[i:])

            for j in range(i,len_arr):
                current_sum +=  nums[j]
                
                if current_sum > largest_sum:
                    largest_sum = current_sum

        return largest_sum




s1 = Solution()

print(s1.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(s1.maxSubArray([1]))
print(s1.maxSubArray([5,4,-1,7,8]))
print(s1.maxSubArray([-1,0,-2]))


# print(s1.maxSubArray(lx))

# Definition of lexicography
# 1 : the editing or making of a dictionary. 