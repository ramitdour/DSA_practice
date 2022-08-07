import itertools as it
from typing import List

from sqlalchemy import false, true

# -> List[List[int]]

# recursion function
def do_per(nums:List[int],ds:List[int] ,return_arr: List[List[int]] , map_space:List[bool]):
    # print("ra",return_arr ,ds)
    if(len(ds) == len(nums)):
        return_arr.append(ds[:]) # ds ponter ho raha tha
        # print("\t raa",return_arr ,ds)
        return
    for i in range(len(nums) ):
        if not(map_space[i]):
            map_space[i] = True
            ds.append(nums[i])
            do_per(nums,ds,return_arr,map_space)
            ds.pop(-1)
            map_space[i] = False



def permutation1(l1):
    # [1,2,3]
    return_arr=[]
    do_per(l1,ds = [] , return_arr = return_arr,map_space=[False]*len(l1))
    [print(r) for r in return_arr]
    return return_arr



print(permutation1([1,2,3]))