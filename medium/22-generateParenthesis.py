"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例：

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

"""
DFS
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(cur, l_num, r_num):
            # 如果可以放置的左右括号数为0，说明已经已经完成一个有效组合，直接将字串加入结果集
            if l_num ==0 and r_num ==0:
                res.append(cur)
                return
            if r_num > 0 and r_num > l_num:
                dfs(cur+')', l_num, r_num-1)
            # 如果可以放置的左括号数大于零，则放置左括号，然后继续dfs
            # 这里可以不添加 and l_num <= r_num，因为上一步r_num > l_num已经保证了这点
            if l_num > 0:
                dfs(cur+'(', l_num-1, r_num)
        res = []
        dfs('', n, n)
        return res