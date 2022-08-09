from typing import List
from largeDs import lx

def merge_sorted_arr(arr_l:List[int],arr_r):

    n1 = len(arr_l)
    n2 = len(arr_r)

    arr_merge = []

    for i in range(n1 + n2 + 1):

        if (len(arr_l) > 0 and len(arr_r) > 0):
            if (arr_l[0] < arr_r[0]):
                arr_merge.append(arr_l.pop(0))
            else:
                arr_merge.append(arr_r.pop(0))
        else:
            if len(arr_l) == 0:
                arr_merge.extend(arr_r)
                break
            else:
                arr_merge.extend(arr_l)
                break

    # print(arr_merge)

    return arr_merge

def merg_sort(nums):
    # print(nums)

    n = len(nums)

    if n < 2: 

        return nums
    if n == 2 :
        return merge_sorted_arr(nums[0:1],nums[1:2])

    else:

        right = n - 1
        left = 0
        mid = (left + right) // 2 

        l_arr = merg_sort(nums[:mid])
        r_arr = merg_sort(nums[mid:])

        return merge_sorted_arr(l_arr,r_arr)





# print(merg_sort([1]))

# print(merg_sort([1,2]))
# print(merg_sort([3,1]))

# print(merg_sort([1,2,3]))

# print(merg_sort([1,2,3,4]))

# print(merg_sort([38,27,43,3,9,82,10]))

print(merg_sort(lx))

# print(merge_sorted_arr([1,4,7],[2,5,8,9,10]))
