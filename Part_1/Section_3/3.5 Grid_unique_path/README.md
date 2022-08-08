Grid Unique Paths | Count paths from left-top to the right bottom of a matrix
Problem Statement: Given a matrix m X n, count paths from left-top to the right bottom of a matrix with the constraints that from each cell you can either only move to the rightward direction or the downward direction.

Example 1:

Input Format: m = 2, n= 2
Output: 2
Explanation: From the top left corner there are total 2 ways to reach the bottom right corner:

Step 1: Right ->> Down



Step 2: Down ->> Right



Example 2:

Input Format: m = 2, n= 3 
Ouput: 3
Explanation:  From the top left corner there is a total of 3 ways to reach the bottom right corner.

Step 1: Right ->> Right ->> Down



Step 2: Right ->> Down ->> Right



Step 3: Down ->> Right->> Right






There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:

1 <= m, n <= 100