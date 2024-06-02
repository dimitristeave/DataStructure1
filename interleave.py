from typing import List
from collections import deque


class Solution:
    def rearrangeQueue(self, N: int, q: List[int]) -> List[int]:
        # code here
        # Convert the list into a deque for efficient pops from the left
        queue = deque(q)

        # Create two deques to hold the two halves
        first_half = deque()
        second_half = deque()

        # Fill the first half
        for _ in range(N // 2):
            first_half.append(queue.popleft())

        # Fill the second half
        for _ in range(N // 2):
            second_half.append(queue.popleft())

        # Interleave the elements from the two halves
        interleaved_queue = deque()
        while first_half and second_half:
            interleaved_queue.append(first_half.popleft())
            interleaved_queue.append(second_half.popleft())

        # Convert back to list and return the result
        return list(interleaved_queue)


# {
# Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())

        q = IntArray().Input(N)

        obj = Solution()
        res = obj.rearrangeQueue(N, q)

        IntArray().Print(res)

# } Driver Code Ends