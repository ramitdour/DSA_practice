from typing import List
from largeDs import lx


def merge_sorted_arr(nums: List[int], left, mid, right):

    # print("m",nums, left, mid, right)
    # print("m",nums[left : mid], nums[mid : right + 1])
    # print(" ")

    if (right - left == 0) : return 0

    total = 0

    # [low,mid) [mid ,right]
    i = left
    j = mid

    for i in range(left , mid):
        while j <= right and nums[i] > 2*nums[j]:
            j += 1
        total += (j - mid)

    # resuse var for store data
    i = left
    j = right


    while (mid <= right):
        if nums[left] >= nums[mid]:
            nums.insert(left , nums.pop(mid))
            left  += 1
            mid += 1
        else:    
            # nums[left] < nums[mid]
            left  += 1
            
            
    

    # n1 = mid - left
    # n2 = (right + 1) - mid

    # orinal_left = left

    # counter_i_gt_2j = 0 

    # i = left
    # j = mid  

    # # while j <= right :
    # #     if nums[i] > 2*nums[j]

    # # for i in range(n1 + n2 + 1):
    # # while n1 > 0 and n2 > 0:
    # while mid <= right:

    #     # print(nums, left, mid, right)

    #     # print(nums[left:mid], nums[mid:left + 1])
       
    #     # if (arr_l[0] < arr_r[0]):
        
    #     if (nums[left] < nums[mid]):
    #         left += 1

    #         # arr_merge.append(arr_l.pop(0))
    #         # arr_merge.append(arr_l.pop(0))
    #     else:
    #         # nums[left] > nums[mid]
    #         # arr_merge.append(arr_r.pop(0))
    #         nums.insert(left, nums.pop(mid))
    #         left += 1
    #         mid += 1

    #     if left == mid:
    #         mid += 1
    #         left  = orinal_left 

    # print("==",nums)

    return total


def merg_sort(nums , left , right):

    # print("aa", nums[left:right + 1])
    # print(nums , left , right , nums[left:right + 1] )

    n =  right - left + 1   # len(nums)

    if n < 2:

        return 0

    # if n == 2:

    #     return merge_sorted_arr(nums, 0, mid, 0)

    else:

        left    = left
        right   = right #n - 1
        mid     = (left + right) // 2  + 1  # very importand , yaad kar lena acche se 

        invs = merg_sort(nums , left,  mid - 1 )

        invs += merg_sort(nums , mid,  right )

        invs += merge_sorted_arr(nums, left, mid, right)

        return  invs


def merg_sortM(nums):
    print(merg_sort(nums , 0, len(nums) - 1))
    # print("ans= ",nums)

# print(merg_sortM([1]))

# print(merg_sortM([1,2]))
# print(merg_sortM([3,1]))

# print(merg_sortM([1,2,3]))

# print(merg_sortM([1,3,2]))

# print(merg_sortM([1,2,3,4]))

# print(merg_sortM([4,5,1,3,2]))

# print(merg_sortM([38,27,43,3,9,82,10]))

print(merg_sortM([38,99,45,52,1,9,2,4,5,88,45,658,27,43,3,9,82,10])) #60

# print(merg_sortM(lx)) #312836170
 
# print(merge_sorted_arr([1, 4, 7, 2, 5, 8, 9, 10], 0, 3, 7))

# print(merge_sorted_arr([1, 4, 7, 2, 4, 8, 9, 10], 0, 3, 7))