"""
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

示例 1:
输入:

0 0 0
0 1 0
0 0 0
输出:

0 0 0
0 1 0
0 0 0
示例 2:
输入:

0 0 0
0 1 0
1 1 1
输出:

0 0 0
0 1 0
1 2 1
注意:

给定矩阵的元素个数不超过 10000。
给定矩阵中至少有一个元素是 0。
矩阵中的元素只在四个方向上相邻: 上、下、左、右。

"""


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))]  # 设定结果集
        q = collections.deque()  # BFS 经典结果，设定一个 queue 来存储每个层次上的点
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:  # 将题目转换为 0 到其它点的距离
                    res[i][j] = 0  # 0到自身的距离为零
                    q.append([i, j])  # 将找到的 0 放入队列
        while q:  # BFS 经典模板
            x, y = q.popleft()  # 取出某层上的点
            for x_bias, y_bias in [[0, 1], [0, -1], [1, 0], [-1, 0]]:  # 加四个方向的偏置
                new_x = x + x_bias
                new_y = y + y_bias
                if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]) and res[new_x][new_y] == None:  # 判断扩展点有效性
                    res[new_x][new_y] = res[x][y] + 1
                    q.append([new_x, new_y])  # 将新扩展的点加入队列
        return res