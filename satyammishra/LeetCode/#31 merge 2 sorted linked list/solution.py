# # # Merge two sorted linked lists and return it as a sorted list. 
# # # The list should be made by splicing together the nodes of the first two lists.

# # Input: l1 = [1,2,4], l2 = [1,3,4]
# # Output: [1,1,2,3,4,4]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:    
        head = ListNode()
        temp = head
    
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 or l2
        return head.next







        
