# LeetCode: 10

"""
Regular expression matching

Problem Statement: Given a text and a pattern, determine if the pattern matches the text completely or not at all using regular expression matching. Assume the pattern contains only two operators: . and *. Operator * in the pattern means that the character preceding * may not appear or may appear any number of times in the text. Operator . matches with any character in the text exactly once.
"""


class RegularExpressionMatching:
    id = 10

    def isMatch(self, text: str, pattern: str) -> bool:
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
        dp[0][0] = True

        for j in range(1, len(pattern) + 1):
            if pattern[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        for i in range(1, len(text) + 1):
            for j in range(1, len(pattern) + 1):
                if pattern[j - 1] == text[i - 1] or pattern[j - 1] == ".":
                    dp[i][j] = dp[i - 1][j - 1]
                elif pattern[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2] or (
                        dp[i - 1][j]
                        if text[i - 1] == pattern[j - 2] or pattern[j - 2] == "."
                        else False
                    )

        return dp[len(text)][len(pattern)]


test_cases_10 = [("aa", "a", False), ("aa", "a*", True), ("ab", ".*", True)]
