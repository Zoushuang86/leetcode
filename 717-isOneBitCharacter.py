"""
717. 1比特与2比特字符
有两种特殊字符：

第一种字符可以用一个比特 0 来表示
第二种字符可以用两个比特(10 或 11)来表示、
给定一个以 0 结尾的二进制数组 bits ，如果最后一个字符必须是一位字符，则返回 true 。



示例 1:

输入: bits = [1, 0, 0]
输出: true
解释: 唯一的编码方式是一个两比特字符和一个一比特字符。
所以最后一个字符是一比特字符。
示例 2:

输入: bits = [1, 1, 1, 0]
输出: false
解释: 唯一的编码方式是两比特字符和两比特字符。
所以最后一个字符不是一比特字符。


提示:

1 <= bits.length <= 1000
bits[i] == 0 or 1
"""
class Solution:
    """
    方法一：正序遍历
    根据题意，第一种字符一定以 0 开头，第二种字符一定以 1 开头。

    我们可以对 bits 数组从左到右遍历。当遍历到 bits[i] 时，如果 bits[i]=0，说明遇到了第一种字符，将 i 的值增加 1；
    如果 bits[i]=1，说明遇到了第二种字符，可以跳过 bits[i+1]
    （注意题目保证 bits 一定以 0 结尾，所以 bits[i] 一定不是末尾比特，因此 bits[i+1] 必然存在），将 i 的值增加 2。
    上述流程也说明 bits 的编码方式是唯一确定的，因此若遍历到 i=n−1，那么说明最后一个字符一定是第一种字符。

    def isOneBitCharacter(self, bits: list) -> bool:
        i, n = 0, len(bits)
        while i < n - 1:
            i += bits[i] + 1
        return i == n - 1
    """

    """
    方法二：倒序遍历
    根据题意，0 一定是一个字符的结尾。
    我们可以找到 bits 的倒数第二个 0 的位置，记作 i（不存在时定义为 −1），
    那么 bits[i+1] 一定是一个字符的开头，且从 bits[i+1] 到 bits[n−2] 的这 n−2−i 个比特均为 1。
    
    如果 n−2−i 为偶数，则这些比特 1 组成了 (n-2-i)/2个第二种字符，所以 bits 的最后一个比特 0 一定组成了第一种字符。
    如果 n−2−i 为奇数，则这些比特 1 的前 n−3−i 个比特组成了 (n-3-i)/2个第二种字符，多出的一个比特 1 和 bits 的最后一个比特 0 组成第二种字符。
    
    由于 n−i 和 n−2−i 的奇偶性相同，我们可以通过判断 n−i 是否为偶数来判断最后一个字符是否为第一种字符，若为偶数则返回 true，否则返回 false。
    """
    def isOneBitCharacter(self, bits: list) -> bool:
        n = len(bits)
        i = n - 2
        while i >= 0 and bits[i]:
            i -= 1
        return (n - i) % 2 == 0


if __name__ == "__main__":
    bits = [1, 0, 0]
    s = Solution()
    print(s.isOneBitCharacter(bits))
