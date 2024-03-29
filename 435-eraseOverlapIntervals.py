"""
435. 无重叠区间
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意:

可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
示例 1:

输入: [ [1,2], [2,3], [3,4], [1,3] ]

输出: 1

解释: 移除 [1,3] 后，剩下的区间没有重叠。
示例 2:

输入: [ [1,2], [1,2], [1,2] ]

输出: 2

解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
示例 3:

输入: [ [1,2], [2,3] ]

输出: 0

解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
"""
"""
动态规划：超时

class Solution:
    def eraseOverlapIntervals(self, intervals: list) -> int:
        n = len(intervals)
        if n == 0:
            return 0

        intervals.sort()
        dp = [1] * n
        res = 1
        for i in range(1, n):
            for j in range(i):
                if intervals[i][0] >= intervals[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return n-res
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: list) -> int:
        n = len(intervals)
        if n == 0:
            return 0

        def compare(elem):
            return elem[1], elem[0]

        intervals.sort(key=compare)
        res = 1
        pre = 0
        for i in range(1, n):
            if intervals[i][0] >= intervals[pre][1]:
                res += 1
                pre = i
        return n - res


if __name__ == "__main__":
    intervals = [ [1,2], [2,3], [3,4], [1,3] ]
    solution = Solution()
    print(solution.eraseOverlapIntervals(intervals))
