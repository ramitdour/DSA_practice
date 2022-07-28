from os import *
from sys import *
from collections import *
from math import *

def getInversions(arr, n) :
    # Write your code here.
    # print(arr,n)
    counter = 0
    for i in range(n):
        for j in range(i, n ):
            if (arr[i] > arr[j]):
                counter += 1
    return counter

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# 3
# 3 2 1

# Main.
arr, n = [3,2,1] , 3


print(getInversions(arr, n))

# 5
# 2 5 1 3 4

# Main.
arr, n = [2, 5 ,1 ,3 ,4] ,5
print(getInversions(arr, n))


# above solution uses brute froce , too long to solve