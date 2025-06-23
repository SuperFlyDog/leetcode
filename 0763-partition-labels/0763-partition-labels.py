class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last = {}
        for idx, char in enumerate(s):
            last[char] = idx
        res = []
        start = 0
        end = 0

        for i, char in enumerate(s):
            # 每遇到一个字符，就更新end为它的最后一次出现
            end = max(end, last[char])

            # 如果i到达了end，说明可以分割了
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res
