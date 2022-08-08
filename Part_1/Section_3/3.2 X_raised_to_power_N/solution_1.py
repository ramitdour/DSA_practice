class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        
        ans = 1
        
        for i in range(abs(n)):
            ans = ans * x

        if n < 0  : return (1 / ans)

        return ans

s1 = Solution()

print(s1.myPow(x = 2.00000, n = 10)) # 1024.00000
print(s1.myPow(x = 2.10000, n = 3))  # 9.26100
print(s1.myPow(x = 2.00000, n = -2)) # 0.25
print(s1.myPow(x = 2.00000, n = 0))  # 1