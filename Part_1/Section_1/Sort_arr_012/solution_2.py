class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)

        low = 0
        mid = 0
        high = l - 1

        def swap_arr(index_a, index_b):
            temp = nums[index_a]
            nums[index_a] = nums[index_b]
            nums[index_b] = temp

        # for i in range(l):
        while (mid <= high):

            if nums[mid] == 0:
                swap_arr(low, mid)
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:
                swap_arr(high, mid)
                high -= 1

        return nums


s1 = Solution()

print(s1.sortColors([2, 0, 2, 1, 1, 0]))
print(s1.sortColors([2, 0, 1]))
print(s1.sortColors([1, 1, 1]))


#  the popular Dutch National flag algorithm
