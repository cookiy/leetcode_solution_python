"""
n 名士兵站成一排。每个士兵都有一个 独一无二 的评分 rating 。

每 3 个士兵可以组成一个作战单位，分组规则如下：

从队伍中选出下标分别为 i、j、k 的 3 名士兵，他们的评分分别为 rating[i]、rating[j]、rating[k]
作战单位需满足： rating[i] < rating[j] < rating[k] 或者 rating[i] > rating[j] > rating[k] ，其中  0 <= i < j < k < n
请你返回按上述条件可以组建的作战单位数量。每个士兵都可以是多个作战单位的一部分。

 

示例 1：

输入：rating = [2,5,3,4,1]
输出：3
解释：我们可以组建三个作战单位 (2,3,4)、(5,4,1)、(5,3,1) 。
示例 2：

输入：rating = [2,1,3]
输出：0
解释：根据题目条件，我们无法组建作战单位。
示例 3：

输入：rating = [1,2,3,4]
输出：4
 

提示：

n == rating.length
1 <= n <= 200
1 <= rating[i] <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-number-of-teams
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
穷举法
执行用时 :1536 ms, 在所有 Python3 提交中击败了100.00%的用户
内存消耗 :13.6 MB, 在所有 Python3 提交中击败了100.00%的用户
"""
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if rating[i] < rating[j]:
                        if rating[j] < rating[k]:
                            count += 1
                    elif rating[i] > rating[j]:
                        if rating[j] > rating[k]:
                            count += 1
        return count

"""
动态规划
更新dp的同时，更新res；
dp[i]记录的是第i个数之前比其值小的数的个数；
两层判断，如果nums[i] > nums[idx], 更新dp[i]，其次，如果dp[idx]>0则再更新res。因为此时，num[i]已经大于nums[idx]，再算上一个比nums[idx]小的数，就构成了一个3个数的升序，这样的组合有dp[idx]；
另外的一种情况，将数组逆序即可。
"""
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        def func(nums):
            dp = [0] * len_
            res = 0
            for i in range(1, len_):
                idx = i - 1
                while idx >= 0:
                    if nums[i] > nums[idx]:
                        dp[i] += 1
                        if dp[idx] > 0:
                            res += dp[idx]
                    idx -= 1
            return res
            
        len_ = len(rating)
        return func(rating[::-1]) + func(rating)

"""
DFS深度优先搜索
"""

class Solution:###比赛时没有考虑len(path)==3的情况加break导致超时
    def numTeams(self, rating):
        self.res=0
        self.dfs(rating,[])
        return self.res
    
    def dfs(self,rating,path):
        if self.is_valid(path):
            self.res += 1
            return
        for i in range(len(rating)):
            if len(path)<3:
                path.append(rating[i])
                self.dfs(rating[i+1:],path)
                path.pop()
            else:###len(path)==3 那么就可以回到上一层了 而不需要继续遍历 
                break
            
    def is_valid(self,p):
        if len(p)==3:
            return p[0]>p[1]>p[2] or p[0]<p[1]<p[2]
