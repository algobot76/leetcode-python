class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0

        l1 = len(haystack)
        l2 = len(needle)

        i = 0
        while i < l1 - l2 + 1:
            while i < l1 - l2 + 1 and haystack[i] != needle[0]:
                i += 1

            j = 0
            curr_len = 0
            while i < l1 and j < l2 and haystack[i] == needle[j]:
                i += 1
                j += 1
                curr_len += 1
            if curr_len == l2:
                return i - l2
            i = i - curr_len + 1

        return -1
