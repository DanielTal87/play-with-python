# LeetCode: 208


class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    id = 208

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.isEnd = True
        return None

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


test_cases_208 = [
    ("insert", "apple", None),
    ("search", "apple", True),
    ("search", "app", False),
    ("startsWith", "app", True),
    ("insert", "app", None),
    ("search", "app", True),
]
