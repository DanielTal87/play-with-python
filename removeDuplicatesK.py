# LeetCode: 1209


class RemoveDuplicatesK:
    id = 1029

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


test_cases_1029 = [
    ("abcd", 2, "abcd"),
    ("deeedbbcccbdaa", 3, "aa"),
    ("pbbcggttciiippooaais", 2, "ps"),
]
