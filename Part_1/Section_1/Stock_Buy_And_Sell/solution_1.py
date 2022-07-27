from ctypes.wintypes import HHOOK
from sqlalchemy import false, true


class Solution:
    def maxProfit(self, prices) :
        print (prices)
        # low_i = 0 
        # low_p = prices[low_i]

        # high_i = 0
        # high_p = prices[high_i]

        # for i in len(prices):
        #     if (prices[i] < low_p):
        #         low_i = i
        #         low_p = prices[low_i]

        #         if low_i > high_i:

        #     if (prices[i] > high_p):
        #         high_i = i
        #         high_p = prices[high_i]

        #         if high_i < low_i:
        #             pass

        #  #[ (gain ,buy , sell ) , ]

        gain_list = []

        i_higher_high = 0
        i_higher_low = 0

        i_lower_low = 0
        i_lower_high = 0

        higher_high = prices[i_higher_high]
        higher_low = prices[i_higher_low]

        lower_low = prices[i_lower_low]
        lower_high = prices[i_lower_high]

        is_up_trend = True

        # i > HH up trend
        # i < LL down trend

        for i in range(len(prices)):
            # print(higher_high , higher_low ,lower_high ,lower_low ,  "up"  if is_up_trend else "down")

            if (prices[i] > higher_high):
                is_up_trend = True

                i_higher_high = i
                higher_high = prices[i_higher_high]

            if (is_up_trend and prices[i] < higher_high):

                i_higher_low = i
                higher_low = prices[i_higher_low]

            if (prices[i] < lower_high):

                is_up_trend = False  # down trend

                i_lower_high = i
                lower_high = prices[i_lower_high]

            if (not(is_up_trend) and prices[i] < lower_low):

                i_lower_low = i
                lower_low = prices[i_lower_low]


s1 = Solution()

# print(s1.maxProfit([7, 1, 5, 3, 6, 4]))
# print(s1.maxProfit([7, 6, 4, 3, 1]))
# print(s1.maxProfit([1, 1, 5]))
l12 = [0, 1, 3, 2, 4, 6, 5, 6, 7, 8]
print(s1.maxProfit(prices = l12[::-1]))

# Definition of lexicography
# 1 : the editing or making of a dictionary.
