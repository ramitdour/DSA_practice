class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascle_list = [[1]]
        
        if(numRows == 1) : return pascle_list
        if(numRows == 2) : return [[1],[1,1]]
        else:
            pascle_list = [[1],[1,1]]

        for i in range(numRows - 2 ):
            pascle_list.append([1])

            # print(pascle_list)

            for k in range( (len(pascle_list[i + 1])) - 1):

                pascle_list[i + 2].append( pascle_list[i + 1][k] +  pascle_list[i + 1][k + 1 ] )

            pascle_list[i + 2].append(1)


        return(pascle_list)



s1 = Solution()

# s1.generate(5)
# s1.generate(1)
p1 = s1.generate(4)

print(p1)