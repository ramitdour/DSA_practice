class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        temp_x = x
        ans = 1
        iterrations = abs(n)

        # n can be + - interger 
        # –2147483648
        # +2147483647
        # difference of 1 , if made it positive 

        # Sol1 : make data type long 
        # Sol2 : adjust 

        
        while(iterrations > 0 ):
            if (iterrations % 2 != 0):
                iterrations // 2
                ans = ans * temp_x
                
                temp_x = temp_x * temp_x
     
                iterrations = iterrations // 2
                
            else:
                temp_x = temp_x * temp_x
     
                iterrations = iterrations // 2


        if n < 0  : return (1 / ans)

        return ans

s1 = Solution()

print(s1.myPow(x = 2.00000, n = 10)) # 1024.00000
print(s1.myPow(x = 2.10000, n = 3))  # 9.26100
print(s1.myPow(x = 2.00000, n = -2)) # 0.25
print(s1.myPow(x = 2.00000, n = 0))  # 1