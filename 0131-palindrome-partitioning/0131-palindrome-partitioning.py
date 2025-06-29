class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []

        def is_palindrome(s, start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True


        def backtrack(start, path):
            if start == len(s):
                res.append(list(path))
                return
            for end in range(start, len(s)):
                if is_palindrome(s, start, end):
                    # 做选择
                    path.append(s[start:end+1])
                    backtrack(end+1, path)
                    # 撤销选择
                    path.pop()
        backtrack(0,[])
        return res
