class LinkedNode:
    def __init__(self, value):
        self.value = value
        self.next = None


# ----TEST FUNCTION-----
def create_linked_list(arr):
    head = LinkedNode(arr[0])
    node = head
    for index in range(1, len(arr)):
        node.next = LinkedNode(arr[index])
        node = node.next

    return head


# need to refactor to remove Kth item from end
def remove_node(head, k):
    temp = []
    node = head

    while node is not None:
        temp.append(node.value)
        node = node.next

    if k > len(temp):
        return head
    else:
        temp.pop(len(temp) - k)
        new_head = LinkedNode(temp[0])
        node = new_head

        for index in range(1, len(temp)):
            print(node.value)
            node.next = LinkedNode(temp[index])
            node = node.next

        return new_head


# Test Case
head1 = create_linked_list([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, None])
print(remove_node(head1, 5))
