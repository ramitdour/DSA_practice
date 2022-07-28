from marshmallow import missing


class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, nums):
        print("nums=",nums)
        repeting = nums[0]
        missing = nums[0]
        # for i in range(len(nums)):
        #     if nums[abs(nums[i])] < 0 :
        #         repeting = abs(nums[i])
        #         break
        #     nums[abs(nums[i])] *= -1

        l  = len(nums)

        for i in range(l):
            # for j in range( l - i -1):
            for j in range( l - 1):
                if nums[j] > nums[j + 1] :
                    temp =   nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp

                if nums[j] == nums[j + 1]:
                    repeting = nums[j]

        print("sort=",nums)
        
        if nums[0] != 1:
            missing = 1
        elif nums[-1] != len(nums):
            missing = len(nums)
        else:
            for j in range( l ):
                if (nums[j] -  nums[j - 1]) == 2 :
                    # print(nums)
                    missing = nums[j] - 1

            

        
        return [missing , repeting]


s1 = Solution()

# print(s1.repeatedNumber(nums = [3 ,1, 2 ,5 ,3])) #4 3

# print(s1.repeatedNumber(nums = [6,4,3,5,5,1])) #2 5

# print(s1.repeatedNumber(nums = [1,3,5,4,4])) #2 4

# print(s1.repeatedNumber(nums = [4,5,2,9,8,1,1,7,10,3])) #6 1

# print(s1.repeatedNumber(nums = [7,5,3,2,1,6,6])) #4 6

print(s1.repeatedNumber(nums = [3,4,5,2,2 ]))  # 1 2
#  8,1,4,5,3,7,7,6 #2 7

"""
3 4 5 2 2 

1 1 4 5 2

6 6 5 3 4 1

8 1 4 5 3 7 7 6 

4 5 6 7 8 1 2 9 3 10 10 11 13 14 16 12 15 19 18 17

4 5 6 7 1 2 3 9 9 

2 2 1 

1 2 3 3 4 5 6 8

9 10 11 12 12 1 2 3 4 5 6 7

4 3 2 5 6 7 8 8 9 10 11 14 13 15 12

1 1 

2 2 

1 1 2 4 

1 5 8 1 2 3 4 10 7 6



1 2
3 1
2 6
2 7
20 10
8 9 
3 2
7 3
8 12
1 8
1 1
2 2
3 1
9 1

"""