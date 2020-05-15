# https://leetcode.com/problems/add-two-numbers/
# <----Problem Statement----->
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.

# ~~~Specifications~~~
# Add the two numbers and return it as a linked list.

# Assumptions:
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Pseudo Code
# reverse the linked lists
# convert the linked list values into one integer
# sum the integers together
# convert sum into a reverse linked list


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return '(Value: %s, Next: %s)' % (self.val, self.next)


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    reversed_l1 = reversal(l1)
    reversed_l2 = reversal(l2)
    sum = make_integer(reversed_l1) + make_integer(reversed_l2)

    sum_list = [int(d) for d in str(sum)]

    index = len(sum_list) - 1
    head = ListNode(sum_list[index])
    current_node = head
    while index > 0:
        index -= 1
        current_node.next = ListNode(sum_list[index])
        current_node = current_node.next

    print(head.__repr__())
    return head


# reverse a linked list helper function
def reversal(linked_list):
    previous_node = None
    current_head = linked_list

    while current_head is not None:
        next_node = current_head.next
        current_head.next = previous_node
        previous_node = current_head
        current_head = next_node

    return previous_node


# helper function to cram all the linked list values together into a single integer value
def make_integer(linked_list):
    string = ""
    current = linked_list

    while current.next is not None:
        string += str(current.val)
        current = current.next
    string += str(current.val)
    return int(string)


# <---------TEST--------->
def make_linked_list(data_list):
    head = ListNode(data_list[0])
    current = head
    for index in range(1, len(data_list)):
        current.next = ListNode(data_list[index])
        current = current.next

    return head


l1 = make_linked_list([2, 4, 3])
l2 = make_linked_list([5, 6, 4])

addTwoNumbers(l1, l2)
