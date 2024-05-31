# User function Template for python3

from typing import List


class Solution:
    def reverse(self, St):
        # code here
        if len(St) == 0:
            return

        # Step 1: Remove the top element
        top = St.pop()

        # Step 2: Recursively reverse the remaining stack
        self.reverse(St)

        # Step 3: Insert the top element at the bottom of the reversed stack
        self.insert_at_bottom(St, top)

    def insert_at_bottom(self, St, item):
        if len(St) == 0:
            St.append(item)
        else:
            top = St.pop()
            self.insert_at_bottom(St, item)
            St.append(top)


# {
# Driver Code Starts

# Initial Template for Python 3


for _ in range(int(input())):
    N = int(input())
    St = list(map(int, input().split()))
    ob = Solution()
    ob.reverse(St)
    print(*St)
# } Driver Code Ends