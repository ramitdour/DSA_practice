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

        for i in range(n//2 + n % 2):
            for j in range(n // 2):
                # temp = matrix[i][j]
                # matrix[i][j] = matrix[n - 1 - i][j]
                # matrix[n - 1 - i][j] = matrix[n - 1 - i][n - 1 - j]
                # matrix[n - 1 - i][n - 1 - j] = matrix[i][n - 1 - j]
                # matrix[i][n - 1 - j] = temp

                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp

        return matrix


s1 = Solution()

print(s1.rotate([[5, 1, 9, 11], [2, 4, 8, 10],
      [13, 3, 6, 7], [15, 14, 12, 16]]))
# print(s1.rotate([[1, 2, 3, 4], [5, 6, 7, 8],      [9, 10, 11, 12], [13, 14, 15, 16]]))

# HINT : transpose then reverse rows
