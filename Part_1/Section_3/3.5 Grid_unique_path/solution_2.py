# from itertools import permutations


# recursion , not that much exponential time , kind of brute force 
# better time complexity
# more space fot firrect path table

# time O(nxm)
# space O(nxm)

class Solution:

    def recursive_path(self,i,j,m,n,dp_table) -> int:
        if i >= m or j >= n :
            return 0

        if i == m - 1 and j == n -1 : 
            return 1

        if dp_table[i][j] != -1 : return dp_table[i][j]
        else :return (self.recursive_path(i + 1,j,m,n,dp_table) + self.recursive_path(i,j + 1,m,n,dp_table))
 
    def uniquePaths(self, m: int, n: int) -> int:
        # m = rows 
        # n = cols
        #(permutations of m forward and n downwards)
        #  m-1 D and n-1 F
        dp_table = [[-1]*n]*m
        return self.recursive_path(0,0,m,n,dp_table) # self keyword


s1 = Solution()

print(s1.uniquePaths(m = 3, n = 7)) #28

print(s1.uniquePaths(m = 3, n = 2)) #3

