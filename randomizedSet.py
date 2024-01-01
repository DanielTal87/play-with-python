# LeetCode: 380

import random


class RandomizedSet:
    id = 380

    def __init__(self):
        self.arr = []
        self.dict = {}

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False

        self.dict[val] = len(self.arr)
        self.arr.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False

        index = self.dict.get(val, None)
        if index is None:
            return False

        length = len(self.arr)
        last = self.arr[length - 1]
        self.arr[index], self.arr[length - 1] = self.arr[length - 1], self.arr[index]

        del self.arr[-1]
        del self.dict[val]

        if last != val:
            self.dict[last] = index

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


test_cases_380 = [
    ("insert", 1, True),
    ("remove", 2, False),
    ("insert", 2, True),
    ("getRandom", None, 2),
    ("remove", 1, True),
    ("insert", 2, False),
    ("getRandom", None, 2),
]
