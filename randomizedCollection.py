# LeetCode: 381

import collections
import random


class RandomizedCollection:
    id = 381

    def __init__(self):
        self.arr = []
        self.dict = collections.defaultdict(set)

    def insert(self, val: int) -> bool:
        self.dict[val].add(len(self.arr))
        self.arr.append(val)

        return len(self.dict[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.dict[val]:
            return False

        else:
            last = self.arr[-1]
            index = self.dict[val].pop()
            self.arr[index] = last
            self.dict[last].add(index)
            self.dict[last].discard(len(self.arr) - 1)
            self.arr.pop()
            return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


test_cases_381 = [
    ("insert", 1, True),
    ("insert", 1, False),
    ("insert", 2, True),
    ("getRandom", None, 2),
    ("remove", 1, True),
    ("getRandom", None, 1),
]
