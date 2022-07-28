from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)

        loww = intervals[0][0]
        highh = intervals[0][1]

        x = [[loww , highh]]

        intervals.sort(key = lambda x : x[0])
        #try to avoid in build sort function
        # print( "S =",intervals)

        for i in range(n):
            if intervals[i][0] <= highh :
                if intervals[i][1] > highh:
                    highh = intervals[i][1]
                x[-1][1] = highh
            else:
                loww = intervals[i][0]
                if intervals[i][1] > highh:
                    highh = intervals[i][1]
                x.append([loww,highh])

        return x

s1 = Solution()

print(s1.merge([[1,3],[2,6],[8,10],[15,18]]))
print(s1.merge([[1,4],[4,5]]))

print(s1.merge([[1,4],[0,4]]))
print(s1.merge([[1,4],[2,3]]))

