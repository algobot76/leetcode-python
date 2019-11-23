import collections
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        punctuations = ".,?!;'"
        for p in punctuations:
            paragraph = paragraph.replace(p, ' ')
        counter = collections.Counter(
            word for word in paragraph.lower().split())

        ans = ''
        for word in counter:
            if (not ans or counter[word] > counter[ans]) and (
                    word not in banned):
                ans = word
        return ans
