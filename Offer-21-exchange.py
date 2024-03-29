"""
剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。



示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。


提示：

0 <= nums.length <= 50000
0 <= nums[i] <= 10000
"""
class Solution:
    def exchange(self, nums: list) -> list:
        n = len(nums)
        if n <= 1:
            return nums

        left, right = 0, n-1
        while left < right:
            if nums[left] % 2 == 1:
                left += 1
            elif nums[right] % 2 == 0:
                right -= 1
            else:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
                right -= 1
        return nums