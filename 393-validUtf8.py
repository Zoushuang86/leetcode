"""
393. UTF-8 编码验证
给定一个表示数据的整数数组 data ，返回它是否为有效的 UTF-8 编码。

UTF-8 中的一个字符可能的长度为 1 到 4 字节，遵循以下的规则：

对于 1 字节 的字符，字节的第一位设为 0 ，后面 7 位为这个符号的 unicode 码。
对于 n 字节 的字符 (n > 1)，第一个字节的前 n 位都设为1，第 n+1 位设为 0 ，后面字节的前两位一律设为 10 。剩下的没有提及的二进制位，全部为这个符号的 unicode 码。
这是 UTF-8 编码的工作方式：

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
注意：输入是整数数组。只有每个整数的 最低 8 个有效位 用来存储数据。这意味着每个整数只表示 1 字节的数据。



示例 1：

输入：data = [197,130,1]
输出：true
解释：数据表示字节序列:11000101 10000010 00000001。
这是有效的 utf-8 编码，为一个 2 字节字符，跟着一个 1 字节字符。
示例 2：

输入：data = [235,140,4]
输出：false
解释：数据表示 8 位的序列: 11101011 10001100 00000100.
前 3 位都是 1 ，第 4 位为 0 表示它是一个 3 字节字符。
下一个字节是开头为 10 的延续字节，这是正确的。
但第二个延续字节不以 10 开头，所以是不符合规则的。


提示:

1 <= data.length <= 2 * 104
0 <= data[i] <= 255
通过次数20,864提交次数49,783
"""
"""
方法一：遍历 + 位运算
思路

如果给定的数组 ata 是有效的 UTF-8 编码，则可能由一个或多个 UTF-8 字符组成。第一个 UTF-8 字符的长度由 data[0] 的值决定。
对于从 data[index] 开始的 UTF-8 字符，可根据 data[index] 的值得到该字符的长度 n，如果下一个 UTF-8 字符存在，
则下一个 UTF-8 字符从下标 index+n 开始。因此，如果给定的数组 data 是有效的 UTF-8 编码，则其对应的 UTF-8 字符序列是唯一的，且每个 UTF-8 字符的开始下标是确定的。

基于上述分析，可以遍历数组 data 得到每个字符的开始下标和长度，并分别判断每个字符是否符合 UTF-8 编码的规则。

每个 UTF-8 字符由 1 到 4 个字节组成。以下将每个 UTF-8 字符的第 1 个字节称为头字节，除了第 1 个字节以外的字节统称为其余字节。

用 m 表示 data 的长度，用 index 表示 UTF-8 字符的头字节在 data 中的下标，初始时 index=0。对于每个字符，执行如下操作。

头字节包含了当前字符的字节数信息，根据头字节计算当前字符字节数的方法如下。

如果头字节的最高位是 0，则当前字符由 1 个字节组成，只有头字节，没有其余字节。

如果头字节的最高位是 1，则计算头字节从最高位开始的连续 1 的个数。如果连续 1 的个数为 2 个到 4 个，则连续 1 的个数表示当前字符的字节数；
否则头字节不符合 UTF-8 编码的规则，data 不是有效的 UTF-8 编码。

当头字节符合 UTF-8 编码的规则时，根据头字节得到当前字符的字节数为 nn，则当前字符包括头字节和 n−1 个其余字节。
如果 data 在头字节后面的字节数小于 n−1，即 index+n>m，则 data 不是有效的 UTF-8 编码。

当 data 在头字节后面的字节数大于等于 n−1 时，头字节后面的 n−1 个字节为当前字符的其余字节。判断每个其余字节的最高两位是否是 10，
如果存在一个其余字节的最高两位不是 10，则 data 不是有效的 UTF-8 编码。

当前字符遍历结束之后，将 index 的值加 n，则更新后的 index 是下一个字符的头字节在 data 中的下标。

重复上述操作，直到 index=n 时遍历结束，此时 data 是有效的 UTF-8 编码。

实现
判断 data 是否是有效的 UTF-8 编码时，需要对每个字符的头字节和其余字节分别做判断。
判断需要通过位运算实现，为了方便判断，需要设计两个位掩码 MASK_1=2^7，MASK_2=2^7+2^6。

对于头字节，首先判断头字节和 MASK_1 的按位与运算结果是否为 0。如果为 0 则当前字符由 1 个字节组成。
如果不为 0 则创建位掩码 mask 并将初始值设为 MASK_1，每次计算头字节和 mask 的按位与运算结果，
如果结果不为 0 则将 mask 除以 2（可通过右移位运算实现）并重复该过程，直到结果为 0，此时可得到当前字符的字节数。

对于其余字节，判断最高两位是否是 10 的做法为计算其余字节和 MASK_2的按位与运算结果是否等于 MASK_1
"""
class Solution:
    def validUtf8(self, data: list) -> bool:
        MASK1, MASK2 = 1 << 7, (1 << 7) | (1 << 6)

        def getBytes(num: int) -> int:
            if (num & MASK1) == 0:
                return 1
            n, mask = 0, MASK1
            while num & mask:
                n += 1
                if n > 4:
                    return -1
                mask >>= 1
            return n if n >= 2 else -1

        index, m = 0, len(data)
        while index < m:
            n = getBytes(data[index])
            if n < 0 or index + n > m or any((ch & MASK2) != MASK1 for ch in data[index + 1: index + n]):
                return False
            index += n
        return True
