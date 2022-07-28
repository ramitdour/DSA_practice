from typing import List
from large_ds import l1

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow_pointer = nums[0]
        fast_pointer = nums[0]

        while True:
            slow_pointer = nums[slow_pointer]
            fast_pointer = nums[nums[fast_pointer]]

            if slow_pointer == fast_pointer:
                print("s f b",slow_pointer,fast_pointer)
                break
        
        
        fast_pointer = nums[0]

        print("s f z",slow_pointer,fast_pointer)

        while slow_pointer != fast_pointer :
            slow_pointer = nums[slow_pointer]
            fast_pointer = nums[fast_pointer]  # made mistake here of moving fast counter by speed of 2x

        print("s f r",slow_pointer,fast_pointer)

        return slow_pointer

s1 = Solution()

print(s1.findDuplicate([1,3,4,2,2]))
print(s1.findDuplicate([3,1,3,4,2]))
print(s1.findDuplicate([2,5,9,6,9,3,8,9,7,1]))

print(s1.findDuplicate(l1))

# tortoise method
# proof re try  https://youtu.be/32Ll35mhWg0?t=469