class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ori = ''
        for ch in s:
            if ch.isalnum():  # 字母或数字都保留
                ori += ch.lower()
        return ori == ori[::-1]
