from typing import Optional

from randomizedSet import RandomizedSet, test_cases_380
from removeDuplicatesK import RemoveDuplicatesK, test_cases_1029
from spiralMatrix import SpiralMatrix, test_cases_54


def run_tests(tests):
    for solution_class, test_cases in tests:
        print(
            f"\033[33m\nRunning tests for {solution_class.__name__}, LeetCode {solution_class.id}:\033[0m"
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
            randomized_set = solution_class()
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

        # Test LeetCode: 54
        if solution_class is SpiralMatrix:
            for index, test_case in enumerate(test_cases, start=1):
                matrix, expected_output = test_case
                solution = solution_class()
                output = solution.spiralOrder(matrix)
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
        (SpiralMatrix, test_cases_54),
    ]
)
