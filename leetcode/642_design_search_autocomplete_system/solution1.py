import collections
from typing import List


class TrieNode:
    def __init__(self):
        self.__TOP_COUNT = 3
        self.hot = []
        self.children = {}

    def add_hot(self, s: str, times: int) -> None:
        for entry in self.hot:
            if entry[1] == s:
                entry[0] = -times
                break
        else:
            self.hot.append([-times, s])
        self.hot.sort()
        if len(self.hot) > self.__TOP_COUNT:
            self.hot.pop()


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.curr = self.root
        self.search = []
        self.sentence_to_count = collections.defaultdict(int)
        for sentence, count in zip(sentences, times):
            self.sentence_to_count[sentence] = count
            self._insert(sentence, count)

    def _insert(self, s: str, times: int) -> None:
        curr = self.root
        curr.add_hot(s, times)
        for ch in s:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
            curr.add_hot(s, times)

    def input(self, c: str) -> List[str]:
        ans = []
        if c == '#':
            self.sentence_to_count[''.join(self.search)] += 1
            self._insert(''.join(self.search),
                         self.sentence_to_count[''.join(self.search)])
            self.curr = self.root
            self.search = []
        else:
            self.search.append(c)
            if self.curr:
                if c not in self.curr.children:
                    self.curr = None
                    return []
                self.curr = self.curr.children[c]
                ans = [entry[1] for entry in self.curr.hot]
        return ans

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
