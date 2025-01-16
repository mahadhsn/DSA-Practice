# copied the best solution lol
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]  # Start with the first string as the prefix
        for string in strs[1:]:  # Compare with the rest of the strings
            while not string.startswith(prefix):  # Shorten prefix until it matches
                prefix = prefix[:-1]
                if not prefix:  # If prefix becomes empty, return ""
                    return ""
        return prefix