class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0

        l1 = len(haystack)
        l2 = len(needle)

        for i in range(l1 - l2 + 1):
            if haystack[i:i + l2] == needle:
                return i
        return -1
