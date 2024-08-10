# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        if head.next==None:
            return head
        # cur,head=head,head.next
        # head.next=cur
        # cur=cur.next
        # 1->2->3->4->5->6->7
        cur=head
        prev=head
        cur=cur.next
        k=ListNode(cur.val)
        k.next=ListNode(prev.val)
        h=k
        while cur.next:
            if cur.next.next:
                k=k.next
                prev=cur.next
                cur=prev.next
                k.next=ListNode(cur.val)
                k=k.next
                k.next=ListNode(prev.val)
            else:
                k=k.next
                cur=cur.next
                k.next=cur
        # if not cur.next.next:
        return h
#--------------------
head=ListNode()
# head.next=ListNode(2)
all=head
# head=head.next
# head.next=ListNode(3)
# head=head.next
# head.next=ListNode(4)
# head=head.next
# head.next=ListNode(5)
# head=head.next
# head.next=ListNode(6)
#-----------------------
solution=Solution()
a=solution.swapPairs(all)
while a:
    print(a.val)
    a=a.next
# while all:
#     print(all.val)
#     all=all.next
