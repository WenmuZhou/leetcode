# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 17:28:06 2018

@author: new
"""
import math
#完全平方定理： 任何一个正整数都可以表示成不超过四个整数的平方之和。满足四数平方和定理的数n（这里要满足由四个数构成，小于四个不行），必定满足n = 4^a(8b + 7)
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n % 4 == 0:
            n /= 4
        
        if n % 8 == 7: 
            return 4

        a = 0
        while a**2 <= n:
            b = int((n - a**2)**0.5)
            if a**2 + b**2 == n:
                return (not not a) + (not not b)

            a += 1
        return 3

tt=Solution()
tt.numSquares(4)
#动态规划解决
#查找动态转移公式：
#dp[i + j**2] = min(dp[i + j**2], dp[i] + 1)
#

class Solution1:
    _dp = list()
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = self._dp
        dp = [float('inf') for i in range(n + 1)]
        dp[0] = 0
        for i in range(n):
            j = 1
            while i + j**2 <= n:
                dp[i + j**2] = min(dp[i + j**2], dp[i] + 1)
                j += 1       
        return dp[n]
ff=Solution1()
dp=ff.numSquares(500)
