class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        chDict = {}
        for ch in s:
            if ch not in chDict:
                chDict[ch] = 1
            else:
                chDict[ch] += 1
        for cha in t:
            if cha not in chDict or chDict[cha] < 1:
                return False
            else:
                chDict[cha] -= 1
        if sum(chDict.values()) == 0:
            return True
        else:
            return False