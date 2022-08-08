from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n_rows = len(matrix)
        n_cols = len(matrix[0])

        if target < matrix[0][0] or target > matrix[n_rows - 1][n_cols - 1]:
            print("out of range")
            return False

        def find_cord(n):
            x = n // n_rows
            y = n % n_rows
            print("nxy",n,x,y)
            return (x ,y,)

        low  = 0
        high = (n_rows*n_cols)  - 1
        mid  = (high + low) // 2

        def print_tillx(st , end):
            # counter = st

            for r in range(n_rows):
                for c in range(n_cols):
                    if r*(n_cols) + c <= end  and r*(n_cols) + c >= st :
                        print (matrix[r][c] , end="\t")
            print("")

        x , y  = find_cord(mid)


        while not( low == high ):
            print_tillx(low,high)
            print("123",low ,mid,high)

            x , y = find_cord(mid)
            print("xy0" ,x,y)

            if (target > matrix[x][y] ):
                low = mid + 1
                mid  = (high + low) // 2
                x , y = find_cord(mid)
                print("xy1" ,x,y)
            elif (target < matrix[x][y] ):
                high = mid - 1
                mid  = (high + low) // 2
                x , y = find_cord(mid)
                print("xy2" ,x,y)
            else:
                if matrix[x][y] == target :
                    return True
        
        if matrix[x][y] == target :
            return True

        return False
        

s1 = Solution()

# print(s1.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))  # True
# print(s1.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)) # False



# print(s1.searchMatrix(matrix = [[1]], target = 1))
print(s1.searchMatrix(matrix = [[1,3]], target = 3))
# print(s1.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
# print(s1.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
