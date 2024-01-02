# LeetCode: 10
# Second Solution

"""
Regular expression matching

Problem Statement: Given a text and a pattern, determine if the pattern matches the text completely or not at all using regular expression matching. Assume the pattern contains only two operators: . and *. Operator * in the pattern means that the character preceding * may not appear or may appear any number of times in the text. Operator . matches with any character in the text exactly once.
"""


class RegularExpressionMatching2:
    id = "10 #2"

    def isMatch(self, text: str, pattern: str) -> bool:
        def dfs(i: int, j: int):
            if i >= len(text) and j >= len(pattern):
                return True
            elif j >= len(pattern):
                return False

            match = i < len(text) and (text[i] == pattern[j] or pattern[j] == ".")
            # Handle '*' case
            if (j + 1) < len(pattern) and pattern[j + 1] == "*":
                # if match and use '*' or don't use '*'
                return match and dfs(i + 1, j) or dfs(i, j + 2)

            if match:
                return dfs(i + 1, j + 1)

            return False

        return dfs(0, 0)


test_cases_10_2 = [
    ("aa", "a", False),
    ("aa", "a*", True),
    ("ab", ".*", True),
    ("aaaaaaaaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*", False),
]
