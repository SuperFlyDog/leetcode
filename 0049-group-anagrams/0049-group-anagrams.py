class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}

        def createSig(s):
            return ''.join(sorted(s))

        for s in strs:
            sig = createSig(s)
            if not sig in groups:
                groups[sig] = []
            groups[sig].append(s)
        return list(groups.values())