"""
704. 二分查找
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。


示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
示例 2:

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
 

提示：

你可以假设 nums 中的所有元素是不重复的。
n 将在 [1, 10000]之间。
nums 的每个元素都将在 [-9999, 9999]之间。
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) -1  # 确定查找的上下界
        while low <= high: # 当low == high时还剩下最后一个值需要进行检验
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1 # +1是因为mid已经验证过不符合条件，新的区间又mid+1开始
            elif nums[mid] > target:
                high = mid -1 # 这里+1同上面原因相同
            else:
                return mid
        return -1 # 执行结束但是没有找到