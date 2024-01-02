"""
Determine if the sum of two integers is equal to a given value

Problem Statement: Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the given value. Return true if the sum exists, and false if it does not.
"""


class HasPairWithSum:
    source = "Internet"
    id = "2"

    def hasPairWithSum(self, nums: list[int], target_sum: int) -> bool:
        seen = set()

        for num in nums:
            complement = target_sum - num

            if complement in seen:
                return True

            seen.add(num)

        return False


test_cases_HPWS = [([1, 2, 3, 4, 5], 9, True), ([1, 2, 3, 4, 5], 10, False)]
