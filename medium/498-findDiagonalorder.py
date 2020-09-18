
"""
498. 对角线遍历
给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。

 

示例:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

输出:  [1,2,4,7,5,3,6,8,9]

解释:

 

说明:

给定矩阵中的元素总数不会超过 100000 。
"""

class Solution:
	def findDiagonalOrder(self, matrix):
		if not matrix or not matrix[0]:
			return []
		M, N = len(matrix), len(matrix[0])
		matrix_num = M * N
		count = 0
		x, y = 0, 0
		result = []
		direction = "up"
		while (count < matrix_num):
			count += 1
			result.append(matrix[x][y])
			# 向右上方向走
			if direction == "up":
				# 无需调换方向的条件（1.x>0 碰到上壁前, 2.y<n-1碰到右壁前）
				if x > 0 and y < N - 1:
					x -= 1
					y += 1
					continue
				else:
					direction = "down"
					# 碰到上壁:1 --> 2
					if x == 0 and y < N - 1:
						y += 1
					# 碰到右壁:3 --> 6
					elif y == N - 1:
						x += 1
			# 向左下方向走
			else:
				# 无需调换方向的条件（1.x < M 碰到下壁前, 2.y > 0 碰到右壁前）
				if x < M - 1 and y > 0:
					x += 1
					y -= 1
					continue
				else:
					direction = "up"
					# 碰左壁:4 --> 7
					if  y == 0 and x < M - 1:
						x += 1
					# 碰下壁:8 --> 9
					elif x == M - 1 :
						y += 1
		return result
