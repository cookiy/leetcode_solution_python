"""
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

 

示例 1：

输入: n = 5, m = 3
输出: 3
示例 2：

输入: n = 10, m = 17
输出: 2
 

限制：

1 <= n <= 10^5
1 <= m <= 10^6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

"""
这个游戏里叫击鼓传花，约瑟夫环，西方也有叫热土豆。
https://blog.csdn.net/u011500062/article/details/72855826
通过严格的数学推导可以。
用程序来全真模拟也可以。
"""
"""
数学方法
f(n,m) = (f(n-1,m)+m) % n
我们把数字看做人，报到 m 的人，直接干掉
n 代表的是当前人数，m 代表的是报数
假设一共有 11 人,最后那个胜利的人下标是 6
在下一轮 10 人的时候，胜利者的编号往前移动三格(假设m=3)
那假设我们有 10 人，胜利者下标为3，到 11 人的时候胜利者下标是 6
所以公式为 fn = (fn-1 + m) % n
执行用时 :80 ms, 在所有 Python3 提交中击败了90.79%的用户
内存消耗 :13.7 MB, 在所有 Python3 提交中击败了100.00%的用户
"""
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        x = 0
        for i in range(2, n+1):
            x = (m + x) % i
        return x
            
"""
模拟破解

1.生成一个0——n-1的列表，初始索引i=0
2.传递m次，意味着从i开始偏移m得到新索引i=i+m-1，考虑m可能大于当前列表长度，所以要对列表长度求模余
3.从列表中pop出一个值后，实际上下一个值的索引位置未改变（因为后边的值都前移了一位），所以仍然是用i=i+m-1计算新的索引，当然也要用新的列表长度求模
4.直至列表长度为1，返回最后剩下的数字。

当然，因为列表中pop(i)是平均O(n)复杂度，所以总的时间复杂度是O(n2)。
"""

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        i, a = 0, list(range(n))
        while len(a)>1:
            i = (i+m-1)%len(a)
            a.pop(i)
        return a[0]