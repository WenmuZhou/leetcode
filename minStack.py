# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 11:01:22 2018

@author: new
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        try:
            int(x)
            if x is None:
                pass
            else:
                self.stack.append(x)
        except Exception as e:
            print(e)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack is None:
            return 'error'
        else:
            self.stack.pop(-1)        

    def top(self):
        """
        :rtype: int
        """
        if self.stack is None:
            return 'error'
        else:
            return self.stack[-1]        

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack is None:
            return 'error'
        else:
            return min(self.stack)
     


# Your MinStack object will be instantiated and called as such:
 obj = MinStack()
 obj.push([1,2,3])
 print(obj.stack)
 obj.pop()
 print(obj.stack)
 param_3 = obj.top()
  print(obj.stack)
 param_4 = obj.getMin()
  print(obj.stack)