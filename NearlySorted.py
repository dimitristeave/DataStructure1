# User function Template for python3

class Solution:

    # Function to return the sorted array.
    def nearlySorted(self, a, n, k):

        # code here
        heap = a[:k + 1]
        heapq.heapify(heap)

        index = 0
        for i in range(k + 1, len(a)):
            a[index] = heapq.heappop(heap)
            heapq.heappush(heap, a[i])
            index += 1

        while (heap):
            a[index] = heapq.heappop(heap)
            index += 1

        return a

import heapq
from collections import defaultdict

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, k = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(*ob.nearlySorted(a, n, k))

# } Driver Code Ends