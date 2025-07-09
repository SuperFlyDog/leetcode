class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        num = 0
        countStack = []
        strStack = []

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                # 进入下一层前，先保存本层的状态
                countStack.append(num)
                strStack.append(res)
                num = 0
                res = ''       # 准备收集括号内的子串
            elif c == ']':
                k = countStack.pop()
                prev = strStack.pop()
                # 展开后接回上一层
                res = prev + res * k
            else:  # 普通字母
                res += c

        # 循环结束，res 就是最终结果
        return res