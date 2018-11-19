# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 10:31:21 2018
给一个01矩阵，求不同的岛屿的个数。 
0代表海，1代表岛，如果两个1相邻，那么这两个1属于同一个岛。我们只考虑上下左右为相邻。

样例 
在矩阵： 
[ 
[1, 1, 0, 0, 0], 
[0, 1, 0, 0, 1], 
[0, 0, 0, 1, 1], 
[0, 0, 0, 0, 0], 
[0, 0, 0, 0, 1] 
] 
中有3个岛。
深度优先思想。遍历矩阵的每个元素，如果为1则计数加一，同时把自己和周围的元素都置0。
@author: shuping
"""
class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        # Write your code here
        if grid is None:
            return None
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res += 1
                    self.dfs(grid, i, j)
        return res

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return
        if grid[i][j]:
            grid[i][j] = 0
            self.dfs(grid, i + 1, j)
            self.dfs(grid, i - 1, j)
            self.dfs(grid, i, j - 1)
            self.dfs(grid, i, j + 1)
if __name__ == '__main__':
    pass
    solution = Solution()
    grid = [ 
[1, 1, 0, 0, 0], 
[0, 1, 0, 0, 1], 
[0, 0, 0, 1, 1], 
[0, 0, 0, 0, 0], 
[0, 0, 0, 0, 1] 
] 
    step = solution.numIslands(grid)
    print(str(step))
