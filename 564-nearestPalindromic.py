"""
564. 寻找最近的回文数
给定一个表示整数的字符串 n ，返回与它最近的回文整数（不包括自身）。如果不止一个，返回较小的那个。

“最近的”定义为两个整数差的绝对值最小。



示例 1:

输入: n = "123"
输出: "121"
示例 2:

输入: n = "1"
输出: "0"
解释: 0 和 2是最近的回文，但我们返回最小的，也就是 0。


提示:

1 <= n.length <= 18
n 只由数字组成
n 不含前导 0
n 代表在 [1, 10^18 - 1] 范围内的整数
"""
"""
方法：模拟
1. 用原数的前半部分替换后半部分得到的回文整数。
2. 用原数的前半部分加一后的结果替换后半部分得到的回文整数。
3. 用原数的前半部分减一后的结果替换后半部分得到的回文整数。
4. 为防止位数变化导致构造的回文整数错误，因此直接构造 999…999 和 100…001 作为备选答案。
"""
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        m = len(n)
        # 需要注意少一位和多一位情况
        candidates = [10**(m-1)-1, 10**m+1]
        selfPrefix = int(n[:(m+1)//2])

        for x in range(selfPrefix - 1, selfPrefix + 2):
            y = x if m % 2 == 0 else x // 10
            while y:
                x = x * 10 + y % 10
                y //= 10
            candidates.append(x)

        ans = -1
        selfNumber = int(n)
        for candidate in candidates:
            if candidate != selfNumber:
                if ans == -1 or (abs(candidate-selfNumber) < abs(ans-selfNumber)) or ((abs(candidate-selfNumber) == abs(ans-selfNumber)) and (candidate < ans)):
                    ans = candidate
        return str(ans)


if __name__ == "__main__":
    string = "11"
    s = Solution()
    print(s.nearestPalindromic(string))
