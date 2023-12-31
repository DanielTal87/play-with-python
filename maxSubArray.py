# LeetCode: 53

from typing import List


class MaxSubArray:
    id = 53

    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        sum = 0

        for n in nums:
            if sum < 0:
                sum = 0
            sum += n
            max_sum = max(max_sum, sum)

        return max_sum


test_cases_53 = [([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6), ([1], 1), ([5, 4, -1, 7, 8], 23)]
