# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 13:38
# @Author  : zhoujun

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # # 逆序遍历
        # res = 0
        # n = len(height)
        # stack = []
        # i = 0
        # while i < n:
        #     if stack and height[i] > height[stack[-1]]:
        #         # 栈不为空且当前高度比栈顶高，满足构成凹槽条件
        #         mid = stack.pop()  # 弹出凹槽中间
        #         if len(stack) == 0:
        #             continue
        #         h = min(height[i], height[stack[-1]]) - height[mid]
        #         w = i - stack[-1] - 1
        #         res += h * w
        #     else:
        #         stack.append(i)
        #         i += 1

        # 暴力解法
        # res = 0
        # n = len(height)
        # for i in range(n):
        #     l_max = 0
        #     r_max = 0
        #     for j in range(i, n):
        #         r_max = max(r_max, height[j])
        #     for j in range(i, -1, -1):
        #         l_max = max(l_max, height[j])
        #     res += min(l_max, r_max) - height[i]

        # 备忘录
        # res = 0
        # n = len(height)
        # if n == 0:
        #     return res
        # l_max = [0] * n
        # r_max = [0] * n
        # l_max[0] = height[0]
        # r_max[n - 1] = height[n - 1]
        # for i in range(1, n):
        #     l_max[i] = max(height[i], l_max[i - 1])
        # for i in range(n - 2, -1, -1):
        #     r_max[i] = max(height[i], r_max[i + 1])
        # for i in range(n):
        #     res += min(l_max[i], r_max[i]) - height[i]

        # 双指针
        res = 0
        n = len(height)
        if n == 0:
            return res
        l_max = height[0]
        r_max = height[n - 1]
        left, right = 0, n - 1
        while left <= right:
            l_max = max(height[left], l_max)
            r_max = max(height[right], r_max)
            if l_max < r_max:
                res += l_max - height[left]
                left += 1
            else:
                res += r_max - height[right]
                right -= 1
        return res


s = Solution()
r = s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
print(r)
