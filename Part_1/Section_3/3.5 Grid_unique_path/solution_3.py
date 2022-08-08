# from itertools import permutations


# recursion , not that much exponential time , kind of brute force 
# better time complexity
# more space fot firrect path table

# time O(nxm)
# space O(nxm)

class Solution:

    
    def uniquePaths(self, m: int, n: int) -> int:
        # m = rows 
        # n = cols
        #(permutations of m forward and n downwards)
        #  m-1 D and n-1 F
        #  m-1 + n-1 = m + n -2
        # (m + n -2 C n - 1) or (m + n -2 C m - 1)
        #   nCr = n!/(n-r!)(r!)
        # combination from Pascle triangle  (n*n-1*...(n-r + 1) / r !)
        # 7 C 3     8 9 10
        #           3 2  1  
        #

        NN = m + n -2
        rr = m - 1

        ncr = 1

        for i in range(1, rr + 1 ):
            ncr = (ncr * ( NN - rr + i)) / i
        
        return int(ncr)
        


s1 = Solution()

print(s1.uniquePaths(m = 3, n = 7)) #28

print(s1.uniquePaths(m = 3, n = 2)) #3

