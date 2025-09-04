class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(needle)
        m = len(haystack)
        i = 0
        j = 0

        for j in range(m-n+1):
            if haystack[j] == needle[0]:
                cut = haystack[j:j+n]
                if cut == needle:
                    return j
        return -1
