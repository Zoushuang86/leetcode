"""
64. 最小路径和
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。



示例 1：


输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
示例 2：

输入：grid = [[1,2,3],[4,5,6]]
输出：12


提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100

class Solution:
    def minPathSum(self, grid: list) -> int:
        row = len(grid)
        col = len(grid[0])

        def check(x, y):
            return 0 <= x < row and 0 <= y < col

        # 确保依次对对角线的元素进行计算
        for dia in range(1, row+col-1):
            for i in range(row):
                j = dia - i
                if check(i, j):
                    if not check(i, j-1):
                        grid[i][j] = grid[i-1][j] + grid[i][j]
                    elif not check(i-1, j):
                        grid[i][j] = grid[i][j-1] + grid[i][j]
                    else:
                        grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[row-1][col-1]
"""
class Solution:
    def minPathSum(self, grid: list) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                elif j == 0:
                    grid[i][j] = grid[i-1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[-1][-1]


if __name__ == "__main__":
    triangle = [[1,2,3],[4,5,6]]
    print(Solution().minPathSum(triangle))
