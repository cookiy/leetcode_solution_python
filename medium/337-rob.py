"""
337. 打家劫舍 III
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:

输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

输出: 7 
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
示例 2:

输入: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode):
        a = self.helper(root) # a 是一个二维数组, 为root的[偷值, 不偷值]
        return max(a[0], a[1])  # 返回两个值的最大值, 此值为小偷最终获得的总值

    # 参数为root节点, helper方法输出一个二维数组：root节点的[偷值, 不偷值]
    def helper(self, root): # 递归结束条件：root为空, 输出 [0, 0]
        if not root:
            return [0,0]
        left = self.helper(root.left) # left是一个二维数组, 为 root 左侧子节点的[偷值, 不偷值]
        right = self.helper(root.right) # right也是一个二维数组, 为root右侧子节点的[偷值, 不偷值]
        robValue = left[1] + right[1] + root.val # root 的偷值
        skipValue =  max(left[0], left[1]) + max(right[0], right[1]) # root 的不偷值
        return [robValue, skipValue]    # 输出小偷可获得的最大金额
        
