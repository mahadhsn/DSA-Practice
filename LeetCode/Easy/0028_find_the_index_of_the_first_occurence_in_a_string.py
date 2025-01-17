# best
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        hay = len(haystack)
        nee = len(needle)

        ans = -1

        if needle == haystack:
            return 0

        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i:i+nee] == needle:
                return i
        
        return ans