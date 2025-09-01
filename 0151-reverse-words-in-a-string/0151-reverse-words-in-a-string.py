class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word = ''
        res = ''
        for z in s:
            if z == ' ':
                s = s[1:]
            else:
                break
        for i in range(len(s)-1,-1,-1):
            if s[i] != ' ':
                word += s[i]
            elif word and s[i] == ' ':
                res += word[::-1]
                word = ''
                res += ' '
        if word != ' ':
            res += word[::-1]
        return res

        
