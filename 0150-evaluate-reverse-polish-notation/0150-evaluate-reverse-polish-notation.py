import math

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = {"+", "-", "*", "/"}
        for token in tokens:
            if token not in operators: 
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == "+":
                    stack.append(int(num2+num1))
                elif token == "-":
                    stack.append(int(num2-num1))
                elif token == "*":
                    stack.append(int(num2*num1))
                elif token == "/":
                    stack.append(int(float(num2) / num1))  # 显式转 float，再转 int

        return stack.pop()