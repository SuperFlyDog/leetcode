class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)-1,-1,-1):
            print(s[i])
            if s[i] != " ":
                count += 1
            elif count > 0 and s[i] == " ":
                return count
        return count    
