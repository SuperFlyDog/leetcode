class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        letterDict = {}
        for letter in magazine:
            if letter in letterDict:
                letterDict[letter] += 1
            else:
                letterDict[letter] = 1
        for ch in ransomNote:
            if ch in letterDict and letterDict[ch] > 0:
                letterDict[ch] -= 1
            else:
                return False
        return True

