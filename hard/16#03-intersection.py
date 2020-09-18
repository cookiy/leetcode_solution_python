"""
给定两条线段（表示为起点start = {X1, Y1}和终点end = {X2, Y2}），如果它们有交点，请计算其交点，没有交点则返回空值。

要求浮点型误差不超过10^-6。若有多个交点（线段重叠）则返回 X 值最小的点，X 坐标相同则返回 Y 值最小的点。

 

示例 1：

输入：
line1 = {0, 0}, {1, 0}
line2 = {1, 1}, {0, -1}
输出： {0.5, 0}
示例 2：

输入：
line1 = {0, 0}, {3, 3}
line2 = {1, 1}, {2, 2}
输出： {1, 1}
示例 3：

输入：
line1 = {0, 0}, {1, 1}
line2 = {1, 0}, {2, 1}
输出： {}，两条线段没有交点

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
两条都是垂线，即与y轴平行
直线1是垂线，直线2不是
直线2是垂线，直线1不是
两条都不是垂线
斜率相同，且截距相同并有交点
斜率不同，先算出交点，再看交点是否均在两条线段之间
"""

class Solution:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        k1 = (end1[1]-start1[1])/(end1[0]-start1[0]) if (end1[0]-start1[0]) else None
        b1 = start1[1] - k1*start1[0] if k1 is not None else None
        k2 = (end2[1]-start2[1])/(end2[0]-start2[0])if (end2[0]-start2[0]) else None
        b2 = start2[1] - k2*start2[0] if k2 is not None else None
        
        if k1 is None and k2 is None: #两条都是垂线
            if start1[0] == start2[0] and min(start1[1], end1[1])<=max(start2[1], end2[1]) and min(start2[1], end2[1])<=max(start1[1], end1[1]):
                #仅当X相同、第一条直线的底端小于第二直线顶端、第二条直线的底端小于第一条直线的顶端时，才有交点
                return [start1[0], max(min(start1[1], end1[1]), min(start2[1], end2[1]))]
        elif k1 is None:#直线1是垂线，直线2不是
            y = k2*start1[0] + b2
            if (start2[1]-y)*(end2[1]-y)<=0:
                return [start1[0], y]
        elif k2 is None:#直线2是垂线，直线1不是
            y = k1*start2[0] + b1
            if (start1[1]-y)*(end1[1]-y)<=0:
                return [start2[0], y]
        else:#都不是垂线
            if k1 == k2 and b1 == b2 and min(start1[1], end1[1])<=max(start2[1], end2[1]) and min(start2[1], end2[1])<=max(start1[1], end1[1]):#两线斜率相同、截距相同，类似两条垂线时的判断
                return [max(min(start1[0], end1[0]), min(start2[0], end2[0])), max(min(start1[1], end1[1]), min(start2[1], end2[1]))]
            elif k1 != k2:#两线斜率不同
                x = (b2-b1)/(k1-k2)
                y = k1*x+b1
                if (start2[1]-y)*(end2[1]-y)<=0 and (start1[1]-y)*(end1[1]-y)<=0:
                    return [x, y]
        return []

