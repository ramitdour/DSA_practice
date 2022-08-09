from typing import List 
from largeDs import lx,lx2





class BIT:
    def __init__(self, n):
        self.n = n + 1
        self.sums = [0] * self.n
    
    def update(self, i, delta):
        while i < self.n:
            self.sums[i] += delta
            i += i & (-i)
    
    def query(self, i):
        res = 0
        while i > 0:
            res += self.sums[i]
            i -= i & (-i)
        return res

class Solution:


    def reversePairs(self, nums: List[int]) -> int:
  
        """
        :type nums: List[int]
        :rtype: int
        """
        # BIT O(nlogn)
        new_nums = nums + [x * 2 for x in nums]
        sorted_set = sorted(list(set(new_nums)))
        tree = BIT(len(sorted_set))
        res = 0
        ranks = {}
        for i, n in enumerate(sorted_set):
            ranks[n] = i + 1
            
        for n in nums[::-1]:
            res += tree.query(ranks[n] - 1)
            tree.update(ranks[n * 2], 1)
        
        return res

        
        



s1= Solution()

print(s1.reversePairs([1,3,2,3,1])) #2
print(s1.reversePairs([3,2,1,4])) #1
print(s1.reversePairs([2,4,3,5,1])) #3
print(s1.reversePairs([7,1,3,2,3,1])) #7

print(s1.reversePairs([38,99,45,52,1,9,2,4,5,88,45,658,27,43,3,9,82,10])) #60
print(s1.reversePairs([2147483647,2147483647,2147483647,2147483647,2147483647,2147483647])) # 0
print(s1.reversePairs(lx)) #312836170 ##50k values
print(s1.reversePairs(lx2)) #625284395  ##50k values
# print(lx2)

# cant understand

