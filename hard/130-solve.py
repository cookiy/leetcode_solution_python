"""
130. 被围绕的区域
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:

X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：

X X X X
X X X X
X X X X
X O X X
解释:

被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 如果数组长或宽小于等于2，则不需要替换
        if len(board) <= 2 or len(board[0]) <= 2:
            return
        
        row, col = len(board), len(board[0])
        
        def dfs(i, j):
            """
            深度优先算法，如果符合条件，替换为A并进一步测试，否则停止
            """
            if i < 0 or j < 0 or i >= row or j >= col or board[i][j] != 'O':
                return
            board[i][j] = 'A'
            
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
        
        # 从外围开始
        for i in range(row):
            dfs(i, 0)
            dfs(i, col-1)
        
        for j in range(col):
            dfs(0, j)
            dfs(row-1, j)
        
        # 最后完成替换
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'

作者：fe-lucifer
链接：https://leetcode-cn.com/problems/surrounded-regions/solution/yuan-di-xiu-gai-de-dfs-python130-bei-wei-rao-de-qu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。