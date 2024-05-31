class Solution:
    # Function to return k largest elements from an array.
    def kLargest(self, li, n, k):
        # Your code here
        # Sort the array in descending order
        li.sort(reverse=True)
        # Return the first k elements
        return li[:k]


# Driver Code
t = int(input("Enter the number of test cases: "))
for _ in range(t):
    # Input processing
    li = [int(x) for x in input().strip().split()]
    n = li[0]
    k = li[1]
    li = [int(x) for x in input().strip().split()]

    # Create an object of the Solution class
    ob = Solution()

    # Call the kLargest function and get the result
    k_largest_list = ob.kLargest(li, n, k)

    # Output the result
    for element in k_largest_list:
        print(element, end=" ")
    print('')
