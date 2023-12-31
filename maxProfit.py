# LeetCode: 121

from typing import List


class MaxProfit:
    id = 121

    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxVal = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxVal = max(maxVal, profit)

            else:
                left = right

            right += 1

        return maxVal


test_cases_121 = [([7, 1, 5, 3, 6, 4], 5), ([7, 6, 4, 3, 1], 0), ([5, 4, -1, 7, 8], 9)]
