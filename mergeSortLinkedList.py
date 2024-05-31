# User function Template for python3

'''
    :param head: head of unsorted linked list
    :return: head of sorted linkd list

    # Node Class
    class Node:
        def __init__(self, data):  # data -> value stored in node
            self.data = data
            self.next = None
'''


class Solution:
    # Function to sort the given linked list using Merge Sort.
    def mergeSort(self, head):
        # Base case: empty list or single element
        if not head or not head.next:
            return head
        # Find the middle of the linked list
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow
        # Split the linked list into two halves
        next_to_middle = middle.next
        middle.next = None
        # Recursively sort the two halves
        left_half = self.mergeSort(head)
        right_half = self.mergeSort(next_to_middle)
        # Merge the sorted halves
        sorted_list = self.merge(left_half, right_half)

        return sorted_list

    # Function to merge two sorted linked lists
    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        if left.data < right.data:
            merged = left
            merged.next = self.merge(left.next, right)
        else:
            merged = right
            merged.next = self.merge(left, right.next)

        return merged


# {
# Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys


# Contributed by : Nagendra Jha

# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node


# prints the elements of linked list starting with head
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data, end=" ")
        curr_node = curr_node.next
    print(' ')


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n = int(input())
        p = LinkedList()  # create a new linked list 'a'.
        nodes_p = list(map(int, input().strip().split()))
        for x in nodes_p:
            p.append(x)  # add to the end of the list

        printList(Solution().mergeSort(p.head))

# } Driver Code Ends