"""
720. 词典中最长的单词
给出一个字符串数组words组成的一本英语词典。从中找出最长的一个单词，该单词是由words词典中其他单词逐步添加一个字母组成。若其中有多个可行的答案，则返回答案中字典序最小的单词。

若无答案，则返回空字符串。

 

示例 1：

输入：
words = ["w","wo","wor","worl", "world"]
输出："world"
解释： 
单词"world"可由"w", "wo", "wor", 和 "worl"添加一个字母组成。
示例 2：

输入：
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
输出："apple"
解释：
"apply"和"apple"都能由词典中的单词组成。但是"apple"的字典序小于"apply"。
 

提示：

所有输入的字符串都只包含小写字母。
words数组长度范围为[1,1000]。
words[i]的长度范围为[1,30]。

"""

class Solution:
    def longestWord(self, words: List[str]):
        """
        :type words: List[str]
        :rtype: str
        """
        temp = ""
        words_set = set(words)
        for i in range(len(words)):
            j = 0
            while j < len(words[i]):
                if words[i][0:j+1] not in words_set:
                    break
                else:
                    j += 1
            if j == len(words[i]):
                if len(words[i]) > len(temp):
                    temp = words[i]
                elif len(words[i]) == len(temp):
                    if words[i] < temp:
                        temp = words[i]                    
        return temp

class Solution:
    def longestWord(self, words: List[str]):
        """
        :type words: List[str]
        :rtype: str
        
        """
        res=''
        trie=Trie()
        for word in words:
            trie.insert(word)
        for word in words:
            if trie.search(word):
                if len(word) > len(res):
                    res=word
                elif len(word)==len(res) and word < res:
                    res=word
        return res

class TrieNode:
    def __init__(self):
        self.end=False
        self.children=collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        node=self.root
        for s in word:
            node=node.children[s]
        node.end=True

    def search(self, word: str) -> bool:
        node=self.root
        for s in word:
            node=node.children.get(s)
            if node is None or not node.end:
                return False
        return True

作者：moffysto
链接：https://leetcode-cn.com/problems/longest-word-in-dictionary/solution/python3-qian-zhui-shu-shi-xian-by-moffysto/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。