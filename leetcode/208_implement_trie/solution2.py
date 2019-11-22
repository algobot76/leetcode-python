from typing import Optional


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        curr['#'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        result = self._find(word)
        return result is not None and '#' in result

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self._find(prefix) is not None

    def _find(self, prefix: str) -> Optional[dict]:
        curr = self.root
        for ch in prefix:
            if ch not in curr:
                return None
            curr = curr[ch]
        return curr

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
