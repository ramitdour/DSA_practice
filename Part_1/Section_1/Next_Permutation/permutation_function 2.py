import itertools as it
from typing import List


def swap (a,b,liist):
    temp = liist[a]
    liist[a] = liist[b]
    liist[b] = temp

def do_per( index:int,nums:List[int] ,return_arr: List[List[int]]):
    if  index == len(nums):
        ds = []
        for i in range(len(nums)):
            ds.append(nums[i])

        return_arr.append(ds)
        return

    for i in range(index , len(nums)) :
        swap(i , index , nums)
        do_per( index + 1 , nums , return_arr)
        swap(i , index , nums)
    


def permutation1(l1):
    # [1,2,3]
    return_arr=[]
    do_per(0,l1,return_arr)
    [print(r) for r in return_arr]
    return return_arr



print(permutation1([1,2,3,4,5,6]))