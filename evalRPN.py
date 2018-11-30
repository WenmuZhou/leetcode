# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 11:29:25 2018
根据逆波兰表示法，求表达式的值。
有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
说明：
整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
@author: shuping
"""

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for c in tokens:
          if c in '+-*':
            i2 = stack.pop()
            i1 = stack.pop()
            print (i1,c,i2)
            print (eval('%s'*3 % (i1,c,i2)))
            stack.append(eval('%s'*3 % (i1,c,i2)))
          else:
            stack.append(c)
        print (stack[0])
        return stack[0]
    
if __name__ == '__main__':
    pass
    solution = Solution()
    s=['2','1','+','3','*']
    step = solution.evalRPN(s)
    print(step)

