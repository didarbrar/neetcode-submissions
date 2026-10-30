# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head

        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        
        l1 = head
        l2 = slow.next
        slow.next = None
        prev_l2=None
        curr=l2

        while curr is not None:
            next_node=curr.next
            curr.next=prev_l2
            prev_l2=curr
            curr=next_node
        list1=l1
        list2=prev_l2

        while list2:
            next1=list1.next
            next2=list2.next

            list1.next=list2
            list2.next=next1

            list1=next1
            list2=next2
        
        