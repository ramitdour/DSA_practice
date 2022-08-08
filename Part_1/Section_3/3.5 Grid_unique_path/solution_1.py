# from itertools import permutations


# recursion , exponential time , kind of brute force 

class Solution:

    def recursive_path(self,i,j,m,n) -> int:
        if i >= m or j >= n :
            return 0

        if i == m - 1 and j == n -1 : 
            return 1

        return (self.recursive_path(i + 1,j,m,n) + self.recursive_path(i,j + 1,m,n))
 
    def uniquePaths(self, m: int, n: int) -> int:
        # m = rows 
        # n = cols
        #(permutations of m forward and n downwards)
        #  m-1 D and n-1 F

        return self.recursive_path(0,0,m,n) # self keyword


s1 = Solution()

print(s1.uniquePaths(m = 3, n = 7)) #28

print(s1.uniquePaths(m = 3, n = 2)) #3

