# LeetCode: 152

from typing import List


class MaxProduct:
    id = 152

    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue

            a, b = n * curMax, n * curMin
            curMax, curMin = max(a, b, n), min(a, b, n)
            res = max(res, curMax)
        return res


test_cases_152 = [
    ([2, 3, -2, 4], 6),
    ([1], 1),
    ([-2, 0, -1], 0),
]
