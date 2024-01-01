# LeetCode: 70


class ClimbingStairs:
    id = 70

    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one += two
            two = temp

        return one


test_cases_70 = [(2, 2), (3, 3)]
