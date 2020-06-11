# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 16:02
# @Author  : zhoujun

class Solution:
    def myPow(self, x: float, n: int) -> float:
        self.d = {}
        self.d[0] = 1
        self.d[1] = x
        if n < 0:
            return 1 / self.pow(x, -n)
        else:
            return self.pow(x, n)

    def pow(self, x, n):
        if n in self.d:
            return self.d[n]
        half = self.pow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x


s = Solution()
print(s.myPow(2, 3))
