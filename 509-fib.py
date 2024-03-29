"""
509. 斐波那契数
斐波那契数，通常用 F(n) 表示，形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给你 n ，请计算 F(n) 。



示例 1：

输入：2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1
示例 2：

输入：3
输出：2
解释：F(3) = F(2) + F(1) = 1 + 1 = 2
示例 3：

输入：4
输出：3
解释：F(4) = F(3) + F(2) = 2 + 1 = 3


提示：

0 <= n <= 30
"""
"""
class Solution:
    memo = [0, 1]

    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return 1

        if len(self.memo) < n+1:
            self.memo.append(self.fib(n-1)+self.fib(n-2))

        return self.memo[n]
"""
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        memo = [-1 for _ in range(n+1)]
        memo[0] = 0
        memo[1] = 1
        for i in range(2, n+1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]


if __name__ == "__main__":
    n = 100
    s = Solution()
    res = s.fib(n)
    print(res)
