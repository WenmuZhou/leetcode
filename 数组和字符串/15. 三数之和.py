# -*- coding: utf-8 -*-
# @Time    : 2020/6/12 9:33
# @Author  : zhoujun
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        result = []
        for i in range(n - 2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return result


if __name__ == '__main__':
    s = Solution()
    nums = [-1,0,1,2,-1,-4]
    r = s.threeSum(nums)
    print(r)
