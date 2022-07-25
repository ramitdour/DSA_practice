class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        zero_cords = []
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0 :
                    zero_cords.append(tuple((i,j,)))
        
        # print("zero cords=" , zero_cords)
        
        made_zero_r = set()
        made_zero_c = set()
        
        for k in range(len(zero_cords)):
            r = zero_cords[k][0]
            c = zero_cords[k][1]
            
            if r not in made_zero_r:
                made_zero_r.add(r)
                
                matrix[r] = [0] * n
                
                 
            
            if c not in made_zero_c:
                made_zero_c.add(c)
                
                for row in matrix:
                    row[c] = 0;
           
        
        # print("matrix cords=" , matrix)
        
        return matrix


