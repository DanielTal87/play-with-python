"""
Find the missing number in a given array

Problem Statement: Given an array of positive numbers ranging from 1 to n, such that all numbers from 1 to n are present except one number x, find x. Assume the input array is unsorted.
"""


class FindMissingNumber:
    source = "Internet"
    id = "1"

    def findTheMissingNumber(self, nums: list[int]) -> int:
        n = len(nums) + 1
        except_sum = n * (n + 1) // 2
        actual_sum = sum(nums)

        return except_sum - actual_sum


test_cases_FMN = [([3, 7, 1, 2, 8, 4, 5], 6)]
