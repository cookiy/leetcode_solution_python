"""
336. 回文对
给定一组唯一的单词， 找出所有不同 的索引对(i, j)，使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。

示例 1:

输入: ["abcd","dcba","lls","s","sssll"]
输出: [[0,1],[1,0],[3,2],[2,4]] 
解释: 可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
示例 2:

输入: ["bat","tab","cat"]
输出: [[0,1],[1,0]] 
解释: 可拼接成的回文串为 ["battab","tabbat"]

"""


class Solution:
    def get_palindrome_parts(self,str):
        pre,suf = [],[]
        lenstr = len(str)
        for i in range(0,lenstr + 1):
            #前缀是回文,包括单词本身
            if str[:i] == str[:i][::-1]:
                pre.append(str[i:][::-1])
            #后缀是回文,包括单词本身
            if str[i:] == str[i:][::-1]:
                suf.append(str[:i][::-1])
        return pre,suf
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        dataset = {w: i for i, w in enumerate(words)}
        res = []
        for index,word in enumerate(words):
            pre,suf = self.get_palindrome_parts(word)
            for p in pre:
                #p[::-1] != word 前缀判断中过滤掉单词本身与其他单词形成回文的情况，避免在后缀判断中重复
                #index != dataset[p] 如果是单词本身则不处理
                if p in dataset and index != dataset[p] and p[::-1] != word:
                    res.append([dataset[p],index])
            for s in suf:
                if s in dataset and index != dataset[s]:
                    res.append([index,dataset[s]])
        return res