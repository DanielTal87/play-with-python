# Run tests cases for all solutions

from typing import Optional

from climbingStairs import ClimbingStairs, test_cases_70
from constructStringFromBinaryTree import Tree2string, test_cases_606
from findMissingNumber import FindMissingNumber, test_cases_FMN
from hasPairWithSum import HasPairWithSum, test_cases_HPWS
from maxProfit import MaxProfit, test_cases_121
from maxSubArray import MaxSubArray, test_cases_53
from randomizedCollection import RandomizedCollection, test_cases_381
from randomizedSet import RandomizedSet, test_cases_380
from regularExpressionMatching import RegularExpressionMatching, test_cases_10
from removeDuplicatesK import RemoveDuplicatesK, test_cases_1029
from spiralMatrix import SpiralMatrix, test_cases_54
from trie import Trie, test_cases_208
from utils.BinaryTree import array_to_binary_tree


def run_tests(tests):
    for solution_class, test_cases in tests:
        source_name = getattr(solution_class, "source", "LeetCode")
        source_id = getattr(solution_class, "id", "")
        print(
            f"\033[33m\nRunning tests for {solution_class.__name__} | {source_name} {source_id}:\033[0m"
        )

        # Test LeetCode: 1029
        if solution_class is RemoveDuplicatesK:
            for index, test_case in enumerate(test_cases, start=1):
                test_input, k, expected_output = test_case
                solution = solution_class()
                output = solution.removeDuplicates(test_input, k)
                compare_expected_and_output(expected_output, output, index)

        # Test LeetCode: 380
        if solution_class is RandomizedSet:
            randomized_set = RandomizedSet()
            outputs = []
            for index, test_case in enumerate(test_cases, start=1):
                operation, value, expected = test_case

                if operation == "insert":
                    result = randomized_set.insert(value)
                elif operation == "remove":
                    result = randomized_set.remove(value)
                elif operation == "getRandom":
                    result = randomized_set.getRandom()

                outputs.append((result, expected))

            for index, (output, expected) in enumerate(outputs, start=1):
                compare_expected_and_output(expected, output, index)

        # Test LeetCode: 381
        if solution_class is RandomizedCollection:
            outputs = []
            randomized_collection = RandomizedCollection()
            for index, test_case in enumerate(test_cases, start=1):
                operation, value, expected = test_case

                if operation == "insert":
                    result = randomized_collection.insert(value)
                elif operation == "remove":
                    result = randomized_collection.remove(value)
                elif operation == "getRandom":
                    result = randomized_collection.getRandom()

                outputs.append((result, expected))

            for index, (output, expected) in enumerate(outputs, start=1):
                compare_expected_and_output(expected, output, index)

        # Test LeetCode: 54
        if solution_class is SpiralMatrix:
            for index, test_case in enumerate(test_cases, start=1):
                matrix, expected_output = test_case
                solution = SpiralMatrix()
                output = solution.spiralOrder(matrix)
                compare_expected_and_output(expected_output, output, index)

        # Test LeetCode: 53
        if solution_class is MaxSubArray:
            for index, test_case in enumerate(test_cases, start=1):
                nums, expected_output = test_case
                solution = MaxSubArray()
                output = solution.maxSubArray(nums)
                compare_expected_and_output(expected_output, output, index)

        # Test LeetCode: 121
        if solution_class is MaxProfit:
            for index, test_case in enumerate(test_cases, start=1):
                prices, expected_output = test_case
                solution = MaxProfit()
                output = solution.maxProfit(prices)
                compare_expected_and_output(expected_output, output, index)

        # Test LeetCode: 606
        if solution_class is Tree2string:
            for index, test_case in enumerate(test_cases, start=1):
                input, expected_output = test_case
                root = array_to_binary_tree(input)
                solution = Tree2string()
                output = solution.tree2str(root)
                compare_expected_and_output(expected_output, output, index)

        # Test LeetCode: 70
        if solution_class is ClimbingStairs:
            for index, test_case in enumerate(test_cases, start=1):
                input, expected_output = test_case
                solution = ClimbingStairs()
                output = solution.climbStairs(input)
                compare_expected_and_output(expected_output, output, index)

        # Test LeetCode: 208
        if solution_class is Trie:
            trie = Trie()
            outputs = []
            for index, test_case in enumerate(test_cases, start=1):
                operation, value, expected = test_case

                if operation == "insert":
                    result = trie.insert(value)
                elif operation == "search":
                    result = trie.search(value)
                elif operation == "startsWith":
                    result = trie.startsWith(value)
                outputs.append((result, expected))

            for index, (output, expected) in enumerate(outputs, start=1):
                compare_expected_and_output(expected, output, index)

        # Test FindMissingNumber
        if solution_class is FindMissingNumber:
            for index, test_case in enumerate(test_cases, start=1):
                input, expected_output = test_case
                solution = FindMissingNumber()
                output = solution.findTheMissingNumber(input)
                compare_expected_and_output(expected_output, output, index)

        # Test HasPairWithSum
        if solution_class is HasPairWithSum:
            for index, test_case in enumerate(test_cases, start=1):
                nums, target_sum, expected_output = test_case
                hasPairWithSum = HasPairWithSum()
                output = hasPairWithSum.hasPairWithSum(nums, target_sum)
                compare_expected_and_output(expected_output, output, index)

        # Test LeetCode: 10
        if solution_class is RegularExpressionMatching:
            for index, test_case in enumerate(test_cases, start=1):
                text, pattern, expected_output = test_case
                solution = RegularExpressionMatching()
                output = solution.isMatch(text, pattern)
                compare_expected_and_output(expected_output, output, index)


##### Analyze test results functions #####


def compare_expected_and_output(expected, output, index: Optional[int] = None):
    if output == expected:
        print(f"\033[92mTest #{index} Passed!\033[0m")
    else:
        print(
            f"\033[91mTest #{index} Failed.\033[0m",
            f"Expected: {expected}, Got: {output}",
        )


##### Run Tests #####

run_tests(
    [
        (RemoveDuplicatesK, test_cases_1029),
        (RandomizedSet, test_cases_380),
        (RandomizedCollection, test_cases_381),
        (SpiralMatrix, test_cases_54),
        (MaxSubArray, test_cases_53),
        (MaxProfit, test_cases_121),
        (Tree2string, test_cases_606),
        (ClimbingStairs, test_cases_70),
        (Trie, test_cases_208),
        (FindMissingNumber, test_cases_FMN),
        (HasPairWithSum, test_cases_HPWS),
        (RegularExpressionMatching, test_cases_10),
    ]
)
