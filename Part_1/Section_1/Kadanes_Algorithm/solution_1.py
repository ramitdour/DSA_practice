class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest_sum = nums[0]
        len_arr = len(nums)
        sub_arr = []

        # for i in range(len_arr):
        #     for k in range(len_arr - i):
        #         x = nums[k: (len_arr - ( len_arr - i) + 1)]
        #         sub_arr_sum = sum(x)
        #         if (largest_sum < sub_arr_sum): 
        #             largest_sum = sub_arr_sum
        #             sub_arr = x

        for i in range(len_arr , -1 , -1):
            for k in range(len_arr - i):
                # print(nums[k : k + i +1])
                x = nums[k : k + i +1]
                sub_arr_sum = sum(x)
                if (largest_sum < sub_arr_sum): 
                    largest_sum = sub_arr_sum
                    sub_arr = x

        return largest_sum




s1 = Solution()

print(s1.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(s1.maxSubArray([1]))
print(s1.maxSubArray([5,4,-1,7,8]))
print(s1.maxSubArray([-1,0,-2]))


# print(s1.maxSubArray(lx))

# Definition of lexicography
# 1 : the editing or making of a dictionary. 