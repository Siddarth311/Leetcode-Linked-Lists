# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        cur=head
        prev=head
        while cur:
            if not cur.next:
                return head
            if cur.val==cur.next.val:
                cur.next=cur.next.next
                # cur=cur.next
            else:
                cur=cur.next
        return head
head=ListNode(1)
# head.next=ListNode(1)
# head=head.next
head.next=ListNode(1)
all=head
head=head.next
head.next=ListNode(1)
# head=head.next
# head.next=ListNode(4)
# head=head.next
# head.next=ListNode(4)
# head=head.next
# head.next=ListNode(6)
#-----------------------
solution=Solution()
a=solution.deleteDuplicates(all)
while a:
    print(a.val,end="->")
    a=a.next
# while all:
#     print(all.val)
#     all=all.next
