class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []

        # 初始化字典，记录p中每个字符出现的次数
        dic = {}
        for ch in p:
            if ch not in dic:
                dic[ch] = 1
            else:
                dic[ch] += 1

        for i in range(len(s) - len(p) + 1):
            test = s[i: i + len(p)]
            dicTemp = dic.copy()
            valid = True
            for ch in test:
                if ch in dicTemp:
                    dicTemp[ch] -= 1
                else:
                    valid = False
                    break  # 提前跳出，说明不是 anagram

            # 检查字典中是否所有字符频次都为0
            if valid and all(value == 0 for value in dicTemp.values()):
                res.append(i)

        return res
