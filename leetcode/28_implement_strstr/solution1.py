class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0

        h = len(haystack)
        n = len(needle)

        for i in range(h - n + 1):
            if haystack[i:i + n] == needle:
                return i
        return -1
