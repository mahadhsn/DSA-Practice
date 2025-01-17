# best
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        words = s.split(" ")
        i = len(words)
        while True:
            i = i - 1
            
            if words[i] == " " or words[i] == "":
                continue
            else:
                return len(words[i])
                break