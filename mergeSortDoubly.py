# User function Template for python3

'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None
'''


class Solution():
    # Function to sort the given doubly linked list using Merge Sort.
    def sortDoubly(self, head):
        # Your code here
        # Si la liste est vide ou n'a qu'un seul élément, elle est déjà triée
        if not head or not head.next:
            return head

        # Trouver le milieu de la liste
        middle = self.getMiddle(head)
        next_to_middle = middle.next

        # Séparer les deux moitiés
        middle.next = None
        if next_to_middle:
            next_to_middle.prev = None

        # Appliquer récursivement le tri fusion sur les deux moitiés
        left = self.sortDoubly(head)
        right = self.sortDoubly(next_to_middle)

        # Fusionner les deux moitiés triées
        sorted_list = self.merge(left, right)

        return sorted_list

    def getMiddle(self, head):
        if not head:
            return head

        slow = head
        fast = head.next

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        if left.data < right.data:
            left.next = self.merge(left.next, right)
            if left.next:
                left.next.prev = left
            left.prev = None
            return left
        else:
            right.next = self.merge(left, right.next)
            if right.next:
                right.next.prev = right
            right.prev = None
            return right


# {
# Driver Code Starts
# Initial Template for Python 3

import sys

sys.setrecursionlimit(1000000)


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def printList(self, node):
        while (node.next is not None):
            node = node.next
        while node.prev is not None:
            node = node.prev
        while (node is not None):
            print(node.data, end=" ")
            node = node.next
        print()


def printList(node):
    temp = node

    while (node is not None):
        print(node.data, end=" ")
        temp = node
        node = node.next
    print()
    while (temp):
        print(temp.data, end=" ")
        temp = temp.prev


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        llist = DoublyLinkedList()
        for e in arr:
            llist.append(e)
        ob = Solution()
        llist.head = ob.sortDoubly(llist.head)
        printList(llist.head)
        print()

# } Driver Code Ends