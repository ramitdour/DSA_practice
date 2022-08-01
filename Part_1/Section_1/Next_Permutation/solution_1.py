import itertools as it

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        print(nums)
        # [print(i) for i in it.permutations(nums)]
        

        def npr(n,r):
            # n! / n-r !
            pass
        
        def swap(a,b):
            print("ab",a,b)
            t = nums[a]
            nums[a] = nums[b]
            nums[b] = t
        
        ind1 = n - 1
        ind2 = n - 1

        for i in range(n-2,-1,-1):
            print("tt" ,i,nums[i] ,nums[ind1] )
            if(nums[i] <  nums[i+1]): 
                ind1 = i
                print("ind121",ind1,ind2)
                break

        if ind1 != n - 1 :

            for i in range(n-1,-1,-1):
                print("ss" ,i,nums[i] ,nums[ind1] )
                if (nums[i] > nums[ind1]): 
                    ind2 = i
                    print("ind122",ind1,ind2)
                    break

        if not(ind1 == n-1  and  ind2 == n - 1):

            swap(ind1,ind2)

        else:
            ind1 = -1
        print(nums)
        for i in range( ind1 + 1 ,n - 1):
            
            print('dsadas', i , n - 1 - (i -(ind1 + 1) ))

            if(n - 1 - (i -(ind1 + 1) ) < i):
                break

            swap(i,n - 1 - (i -(ind1 + 1) ))
        
        return nums
            






s1 = Solution()

# print(s1.nextPermutation([1, 2, 3]))
# print(s1.nextPermutation([3, 2, 1]))
# print(s1.nextPermutation([1,3,2]))
# print(s1.nextPermutation([1, 1, 5]))
# print(s1.nextPermutation([1,3,5,4,2]))

# print(s1.nextPermutation([1,2,3,4,5]))
print(s1.nextPermutation([5,4,7,5,3,2])) #[5,5,2,3,4,7] 


# Definition of lexicography
# 1 : the editing or making of a dictionary. 