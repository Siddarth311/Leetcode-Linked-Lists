# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n==0:
            return head
        i=1
        cur=head
        while cur.next:
            i+=1
            cur=cur.next
        a=i-n
        if i==n:
            return head.next
        if n==1:
            cur=head
            for i in range(a-1):
                cur=cur.next
            # while cur.next:
            #     cur=cur.next
            cur.next=None
            return head
        cur=head
        for i in range(a-1):
            cur=cur.next
        cur.next=cur.next.next
        return head
#--------------------
head=ListNode(1)
# head.next=ListNode(1)
# head=head.next
head.next=ListNode(2)
all=head
head=head.next
head.next=ListNode(3)
head=head.next
head.next=ListNode(4)
head=head.next
head.next=ListNode(5)
head=head.next
head.next=ListNode(6)
#-----------------------
solution=Solution()
a=solution.removeNthFromEnd(all,1)
while a:
    print(a.val,end="->")
    a=a.next
# while all:
#     print(all.val)
#     all=all.next
