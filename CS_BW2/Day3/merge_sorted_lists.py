# https://leetcode.com/problems/merge-two-sorted-lists/

# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.

# Example:
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head1 = l1
        head2 = l2
        pointer = None

        if not head1:
            return head2
        if not head2:
            return head1

        # establish which of the two heads is bigger
        if head1.val <= head2.val:
            pointer = head1
            head1 = pointer.next
        else:
            pointer = head2
            head2 = pointer.next

        new_head = pointer

        while head1 and head2:
            if head1.val <= head2.val:
                pointer.next = head1
                pointer = head1
                head1 = pointer.next
            else:
                pointer.next = head2
                pointer = head2
                head2 = pointer.next

        if not head1:
            pointer.next = head2
        if not head2:
            pointer.next = head1

        return new_head
