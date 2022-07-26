class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        c0 = 0
        c1 = 0
        c2 = 0
        
        for i in nums:
            if i == 2:
                c2 += 1
            elif i == 1:
                c1 += 1
            else: 
                c0 += 1
                
        return ([0] * c0) + ([1] * c1) + ([2] * c2)

        


s1 = Solution()

print(s1.sortColors([2,0,2,1,1,0]))
print(s1.sortColors([2,0,1]))
print(s1.sortColors([1,1,1]))




#  the popular Dutch National flag algorithm 