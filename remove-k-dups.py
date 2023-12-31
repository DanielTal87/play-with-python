# LeetCode: 1209

class Solution:
  def removeDuplicates(self, s: str, k: int) -> str:
    stack = []
    for char in s:
      if stack and stack[-1][0] == char:
        stack[-1][1] += 1
      else:
        stack.append([char, 1])
      if stack[-1][1] == k:
        stack.pop()
    res = ""
    for char, count in stack:
      res += char * count
    return res


def run_test(index, test_input, k, expected_output):
    solution = Solution()
    output = solution.removeDuplicates(test_input, k)

    if output == expected_output:
        print(f"\033[92mTest {index} Passed!\033[0m")  # Green color for passed
    else:
        print(f"\033[91mTest {index} Failed.\033[0m", f"Expected: {expected_output}, Got: {output}")  # Red color for failed

test_cases = [
   ('abcd', 2, 'abcd'),
   ("deeedbbcccbdaa", 3, "aa"),
   ('pbbcggttciiippooaais', 2, 'ps')
]

for index, test_case in enumerate(test_cases, start=1):
    run_test(index, *test_case)