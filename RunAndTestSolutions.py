from typing import Optional

from removeDuplicatesK import Solution1029, test_cases_1029


def run_tests(tests):
    for solution_class, test_cases in tests:
        print(f"\033[33m\nRunning tests for {solution_class.__name__}:\033[0m")

        if solution_class is Solution1029:
            for index, test_case in enumerate(test_cases, start=1):
                test_input, k, expected_output = test_case
                solution = solution_class()
                output = solution.removeDuplicates(test_input, k)
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
        (Solution1029, test_cases_1029),
        (Solution1029, test_cases_1029),
    ]
)
