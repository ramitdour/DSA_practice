from largeDS import lx

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest_sum = nums[0]

        sub_arr_sum = 0

        l = len(nums)

        for i in range(l):

            sub_arr_sum += nums[i]

            if(sub_arr_sum > largest_sum):
                largest_sum = sub_arr_sum

            if(sub_arr_sum < 0):
                sub_arr_sum = 0
        
        return largest_sum




s1 = Solution()

print(s1.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(s1.maxSubArray([1])) #1
print(s1.maxSubArray([5,4,-1,7,8])) #23
print(s1.maxSubArray([-1,0,-2])) #0
print(s1.maxSubArray(lx)) #11081

# print(s1.maxSubArray(lx))

# Definition of lexicography
# 1 : the editing or making of a dictionary. 