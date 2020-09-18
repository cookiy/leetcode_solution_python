"""

示例:

输入:
[1,2,3]

输出:
3

解释:
只需要3次移动（注意每次移动会增加两个元素的值）：

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

"""


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums)-min(nums)*len(nums)