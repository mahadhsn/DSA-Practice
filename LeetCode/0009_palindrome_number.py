# best possible answer
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        ans = False
        x = str(x)
        if x[::-1] == x:
            ans = True
        
        return ans