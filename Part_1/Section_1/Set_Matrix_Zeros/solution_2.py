from calendar import firstweekday


def print_m(mat):
    for r in mat:
        print(r)
    print("")

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        print_m(matrix)


        m = len(matrix)
        n = len(matrix[0])
        
        first = matrix[0][0]
        
        for i in range(0,m):

            if matrix[i][0] == 0 : first = matrix[i][0]

            for j in range(1,n):

                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # print("zero cords=" , zero_cords)

        print_m(matrix)

        # matrix[0][0] = first

        
        for k in range(m - 1 , -1 , -1):
            for l in range (n - 1 , 0 , -1 ):
                if matrix[0][l] == 0 or matrix[k][0] == 0 :
                    matrix[k][l] = 0
            if(first == 0):
                matrix[k][0] = 0

        return matrix


s1 = Solution()

# print_m(s1.setZeroes([
#     [1,1,1,1],
#     [1,0,1,1],
#     [1,1,1,1],
#     [1,1,1,0],
# ]))
# print("-------")
# print_m(s1.setZeroes([
#     [0,1,1,1],
#     [1,1,1,1],
#     [1,1,1,1],
#     [1,1,1,0],
# ]))

# print("-------")
# print_m(s1.setZeroes([
#     [0,1]
# ]))
# print("-------")
# print_m(s1.setZeroes([
#     [1,0]
# ]))

print_m(s1.setZeroes(
    [[1,2,3,4],
    [5,0,7,8],
    [0,10,11,12],
    [13,14,15,0]
]))
