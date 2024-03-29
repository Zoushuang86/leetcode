"""
1748. 唯一元素的和
给你一个整数数组 nums 。数组中唯一元素是那些只出现 恰好一次 的元素。

请你返回 nums 中唯一元素的 和 。



示例 1：

输入：nums = [1,2,3,2]
输出：4
解释：唯一元素为 [1,3] ，和为 4 。
示例 2：

输入：nums = [1,1,1,1,1]
输出：0
解释：没有唯一元素，和为 0 。
示例 3 ：

输入：nums = [1,2,3,4,5]
输出：15
解释：唯一元素为 [1,2,3,4,5] ，和为 15 。


提示：

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""
from collections import Counter
"""
执行用时：36 ms, 在所有 Python3 提交中击败了65.56%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了73.60%的用户
"""
class Solution:
    def sumOfUnique(self, nums) -> int:
        mapping = Counter(nums)

        res = 0
        for k, v in mapping.items():
            if v == 1:
                res += k
        return res


if __name__ == "__main__":
    nums = [1,1,1,1,1]
    s = Solution()
    print(s.sumOfUnique(nums))
