"""
93. 复原IP地址
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。

 

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
"""

# 暴力法
class Solution:
    def validInt(self, s: str):
        """
        :rtype: Boolean
        """
        if not s or (s[0] == "0" and len(s) > 1) or int(s) > 255:
            return False
        return True

    def restoreIpAddresses(self, s: str):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        res = []
        for i in range(3):
            for j in range(i + 1, i + 4):
                for k in range(j + 1, j + 4):
                    if i < n and j < n and k < n:
                        tmp1 = s[:i + 1]
                        tmp2 = s[i + 1:j + 1]
                        tmp3 = s[j + 1:k + 1]
                        tmp4 = s[k + 1:]
                        # print(tmp1, tmp2, tmp3, tmp4)

                        if all(map(self.validInt, [tmp1, tmp2, tmp3, tmp4])):
                            res.append(tmp1 + "." + tmp2 + "." + tmp3 + "." + tmp4)
        return res


作者：powcai
链接：https://leetcode-cn.com/problems/restore-ip-addresses/solution/bao-li-he-hui-su-by-powcai/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 回溯法

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        r = []
        def restore(count=0, ip='', s=''): # count record split times, ip record ip, s record remaining string
            if count == 4:
                if s == '':
                    r.append(ip[:-1])
                return
            if len(s) > 0:
                restore(count+1, ip+s[0]+'.', s[1:])
            if len(s) > 1 and s[0] != '0':
                restore(count+1, ip+s[:2]+'.', s[2:])
            if len(s) > 2 and s[0] != '0' and int(s[0:3]) < 256:
                restore(count+1, ip+s[:3]+'.', s[3:])
        restore(0, '', s)
        return r

作者：su-zi-2
链接：https://leetcode-cn.com/problems/restore-ip-addresses/solution/97-100-jian-ji-hui-su-by-su-zi-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。