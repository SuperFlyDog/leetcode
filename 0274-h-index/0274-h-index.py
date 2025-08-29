class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        h_index = 0
        # 枚举所有可能的 h
        for h in range(n+1):
            count = 0
            for paper in citations:
                if paper >= h:
                    count += 1
            if count >= h:
                h_index = max(h_index, h)
        return h_index
