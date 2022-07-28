from tempfile import tempdir
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # def print_m(matrix):
        #     for q in matrix:
        #         print(q)
        #     print("-----")

        # print_m(matrix)

        def swap(a, b):
            temp = matrix[a[0]][a[1]]
            matrix[a[0]][a[1]] = matrix[b[0]][b[1]]
            matrix[b[0]][b[1]] = temp

        def reverse_array(array_to_be_rev):

            l_ar = len(array_to_be_rev)

            for k in range(l_ar // 2):
                temp_r = array_to_be_rev[k]
                array_to_be_rev[k] = array_to_be_rev[l_ar - k - 1]
                array_to_be_rev[l_ar - k - 1] = temp_r


        for i in range(0 , n - 1 ):
            for j in range( i + 1 , n):
                # swap((i,j),(n -i ,n -j))
                #((n-1)-j ) -i          ((n-1)-j ) - j
                swap((i, j), (j , i ))
                # print(i,j ,end="\t" ,sep=":")
                # print(matrix[i][j], end="\t")
            # print("")

        # print_m(matrix)

        for row in matrix:
            reverse_array(row)

        # print_m(matrix)

        return matrix


s1 = Solution()

print(s1.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
# print(s1.rotate([[1, 2, 3, 4], [5, 6, 7, 8],      [9, 10, 11, 12], [13, 14, 15, 16]]))

# HINT : transpose then reverse rows
