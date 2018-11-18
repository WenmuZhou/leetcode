# -*- coding: utf-8 -*-
# @Time    : 2018/11/18 10:56
# @Author  : zhoujun

class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        l = len(temperatures)
        if l == 1:
            return [0]
        result = [0] * l
        stack = []
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                index = stack.pop()[1]
                result[index] = i - index
                print("执行出站操作之后：{}  {}".format(result,stack))
            stack.append((t,i))
            print("执行入站操作：{}".format(stack))
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))