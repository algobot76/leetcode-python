class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0

        h = len(haystack)
        n = len(needle)

        i = 0
        while i < h - n + 1:
            while i < h - n + 1 and haystack[i] != needle[0]:
                i += 1

            j = 0
            curr_len = 0
            while i < h and j < n and haystack[i] == needle[j]:
                i += 1
                j += 1
                curr_len += 1
            if curr_len == n:
                return i - n
            i = i - curr_len + 1

        return -1
