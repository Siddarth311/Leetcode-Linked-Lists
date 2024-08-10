class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        # Handle edge cases where one of the lists is empty
        # if not list1:
        #     return list2
        # if not list2:
        #     return list1
        # Determine the head of the merged list
        #l=[[1,2,6,8],[2,3,9],[1,2,6,9],[0,1,4]]
        #cur=l[0][0]
        #res=cur
        #res
        head=lists[0]
        for i in range(1,len(lists)):
            list1=head
            list2=lists[i]
            if not list1:
                head = list2
                continue
            if not list2:
                continue
            if list1.val <= list2.val:
                head = list1
                list1 = list1.next
            else:
                head = list2
                list2 = list2.next
            
            # Pointer to build the merged list
            current = head
            # Merge the lists

            while list1 and list2:
                if list1.val <= list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next
            
            # Attach the remaining nodes from list1 or list2
            if list1:
                current.next = list1
            else:
                current.next = list2
        return head
# #--------------------
head=ListNode(1)
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
#-----
head=ListNode(1)
head.next=ListNode(4)
all1=head
head=head.next
head.next=ListNode(5)
head=head.next
head.next=ListNode(8)
head=head.next
head.next=ListNode(9)
head=head.next
head.next=ListNode(9)
#----------
head=ListNode(0)
head.next=ListNode(2)
all2=head
head=head.next
head.next=ListNode(5)
head=head.next
head.next=ListNode(5)
head=ListNode()
k=[all,head,all1,all2]
# #-----------------------
solution=Solution()
a=solution.mergeKLists(k)
while a:
    print(a.val,end="-->")
    a=a.next
# # while all:
# #     print(all.val)
# #     all=all.next
# for i in k:
#     while i:
#         print(i.val,end="-->")
#         i=i.next
    