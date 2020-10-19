class Node():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution():
    def reverseLinkedList(self, root):
        head = root
        newHead = root.next
        head.next = None

        while newHead:
            tmp = newHead.next
            newHead.next = head
            head = newHead
            newHead = tmp




n4 = Node(4)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)


# iterate before
node = n1
while node:
    print(node.val)
    node = node.next

Solution().reverseLinkedList(n1)
# iterate after
node = n4
while node:
    print(node.val)
    node = node.next


