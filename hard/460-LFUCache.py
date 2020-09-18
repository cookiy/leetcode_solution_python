"""
设计并实现最不经常使用（LFU）缓存的数据结构。它应该支持以下操作：get 和 put。

get(key) - 如果键存在于缓存中，则获取键的值（总是正数），否则返回 -1。
put(key, value) - 如果键不存在，请设置或插入值。当缓存达到其容量时，它应该在插入新项目之前，使最不经常使用的项目无效。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，最近最少使用的键将被去除。

一个项目的使用次数就是该项目被插入后对其调用 get 和 put 函数的次数之和。使用次数会在对应项目被移除后置为 0。

进阶：
你是否可以在 O(1) 时间复杂度内执行两项操作？

示例：

LFUCache cache = new LFUCache( 2 /* capacity (缓存容量) */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回 1
cache.put(3, 3);    // 去除 key 2
cache.get(2);       // 返回 -1 (未找到key 2)
cache.get(3);       // 返回 3
cache.put(4, 4);    // 去除 key 1
cache.get(1);       // 返回 -1 (未找到 key 1)
cache.get(3);       // 返回 3
cache.get(4);       // 返回 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lfu-cache
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class dlNode:
    def __init__(self, key, val, cnt=0):
        self.val = [key, val, cnt]#键、值、访问次数
        self.pre = None
        self.nxt = None


class LFUCache:
    def __init__(self, capacity: int):
        self.cache = {}#通过key保存链表节点，key:node
        self.c = capacity#字典容量
        self.head = dlNode(1, 1, float('inf'))#头节点，定义访问次数正无穷
        self.tail = dlNode(-1, -1, float('-inf'))#尾节点，定义访问次数负无穷
        self.head.nxt = self.tail 
        self.tail.pre = self.head

    def _refresh(self, node, cnt):##辅助函数，对节点node，以访问次数cnt重新定义其位置
        pNode, nNode = node.pre, node.nxt #当前节点的前后节点
        if cnt < pNode.val[2]:#如果访问次数小于前节点的访问次数，无需更新位置
            return
        pNode.nxt, nNode.pre = nNode, pNode#将前后连起来，跳过node位置
        while cnt >= pNode.val[2]:#前移到尽可能靠前的位置后插入
            pNode = pNode.pre
        nNode = pNode.nxt
        pNode.nxt = nNode.pre = node
        node.pre, node.nxt = pNode, nNode

    def get(self, key: int) -> int:
        if self.c <= 0 or key not in self.cache:#如果容量<=0或者key不在字典中，直接返回-1
            return -1
        node = self.cache[key]#通过字典找到节点
        _, value, cnt = node.val#通过节点得到key，value和cnt
        node.val[2] = cnt+1#访问次数+1
        self._refresh(node, cnt+1)#刷新位置
        return value

    def put(self, key: int, value: int) -> None:
        if self.c <= 0:#缓存容量<=0
            return
        if key in self.cache:#已在字典中，则要更新其value，同时访问次数+1刷新位置
            node = self.cache[key]
            _, _, cnt = node.val
            node.val = [key, value, cnt+1]#更新其值
            self._refresh(node, cnt+1)
        else:
            if len(self.cache) >= self.c: #容量已满，先清除掉尾部元素
                tp, tpp = self.tail.pre, self.tail.pre.pre
                self.cache.pop(tp.val[0]) #从字典剔除尾节点
                tpp.nxt, self.tail.pre = self.tail, tpp #首尾相连，跳过原尾节点
            #新建节点，并插入到队尾，再刷新其位置
            node = dlNode(key, value)
            node.pre, node.nxt = self.tail.pre, self.tail
            self.tail.pre.nxt, self.tail.pre = node, node
            self.cache[key] = node
            self._refresh(node, 0)
