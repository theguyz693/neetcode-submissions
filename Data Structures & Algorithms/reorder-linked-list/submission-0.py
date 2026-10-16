# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        second=slow.next #prepping the next to exisit,after making it null for firsthalf
        slow.next=None
        prev=None #reversing LL with second as curr/head

        while second:
            tmp= second.next
            second.next=prev
            prev=second
            second=tmp

        #merge two halves
        first,second=head,prev
        while second:
            first_next,second_next=first.next,second.next
            first.next=second
            second.next=first_next
            first=first_next
            second=second_next
