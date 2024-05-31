# User function Template for python3
class Solution:

    def matchPairs(self, nuts, bolts, n):

        # code here
        # Définir l'ordre de priorité pour les éléments
        order = ['!', '#', '$', '%', '&', '*', '?', '@', '^', '~']
        priority = {char: i for i, char in enumerate(order)}

        # Trier les écrous et les boulons selon l'ordre défini
        nuts.sort(key=lambda x: priority[x])
        bolts.sort(key=lambda x: priority[x])


# {
# Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        nuts = list(map(str, input().strip().split()))
        bolts = list(map(str, input().strip().split()))
        ob = Solution()
        ob.matchPairs(nuts, bolts, n)
        for x in nuts:
            print(x, end=" ")
        print()
        for x in bolts:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends