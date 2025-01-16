# mid solution
class Solution(object):
    def romanToInt(self, s):
        roman_to_int = {'I':1, 'V':5, 'X':10, 'L':50, 'C': 100, 'D': 500, 'M': 1000, 'IV':4, 'IX':9, 'XL':40,'XC':90,'CD':400, 'CM':900}

        intt = 0
        y = 0 

        while y < len(s):
            added = 0

            if s[y:y+2] == 'IV' or s[y:y+2] == 'IX' or s[y:y+2] == 'XL' or s[y:y+2] == 'XC' or s[y:y+2] == 'CD' or s[y:y+2] == 'CM':
                added = roman_to_int[s[y:y+2]]
                y+=2
            else:
                added = roman_to_int[s[y]] 
                y+=1

            intt+=added

        return intt