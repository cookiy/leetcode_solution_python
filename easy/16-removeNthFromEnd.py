"""
19. 删除链表的倒数第N个节点
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

"""
# 方法二：栈

class Solution:
    def removeNthFromEnd(self, head, n: int):
        dummy = ListNode(0, head)
        stack = list()
        cur = dummy

        while cur:
            stack.append(cur)
            cur = cur.next
        
        for i in range(n):
            stack.pop()

        prev = stack[-1]
        prev.next = prev.next.next
        
        return dummy.next


# 方法三：一次遍历
# 快慢节点，n为超出的节点，同时走，到达尾部，正好是要删除的节点，删除后重新连接
class Solution:
    def removeNthFromEnd(self, head, n: int):
        dummy = ListNode(0, head)
        first = head
        second = dummy

        #step1: 快指针先走n步
        for i in range(n):
            first = first.next
        
        #step2: 快慢指针同时走，直到fast指针到达尾部节点，此时slow到达倒数第N个节点的前一个节点
        while first and first.next:
            first  = first.next
            second = second.next

        #step3: 删除节点，并重新连接
        second.next = second.next.next

        return dummy.next