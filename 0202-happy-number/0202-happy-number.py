class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = set()
        
        while n != 1:
            s = str(n)
            n = 0
            for i in s:
                n += int(i)*int(i)
            if n in num:
                return False
            print(n) 
            num.add(n)
        return True
