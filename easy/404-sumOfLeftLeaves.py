"""
404. 左叶子之和
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        sum = 0
        if not root:
            return 0
        ans = [ root] 
        while ans:
            r = ans.pop()
            if r.left and not r.left.left and not r.left.right:
                sum += r.left.val
            if r.left:
                ans.append(r.left)
            if r.right:
                ans.append(r.right)
        return sum


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
      self.res = 0
      def dfs(node):
          if not node:
              return None
          if node.left and not node.left.left and not node.left.right:
              self.res += node.left.val
          dfs(node.left)
          dfs(node.right)
      dfs(root)
      return self.res