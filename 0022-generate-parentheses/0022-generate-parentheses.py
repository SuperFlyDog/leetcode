class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        
        def BT(cur,openN,closeN):
            if len(cur) == n*2:
                res.append(cur)
                return
            if openN < n:
                BT(cur+'(',openN+1, closeN)
            if openN > closeN:
                BT(cur+')',openN, closeN+1)
        BT('',0,0)
        return res
            