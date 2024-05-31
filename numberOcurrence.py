class Solution:
    def count(self, arr, n, x):
        i = 0
        for number in arr:
            if number == x:
                i += 1
            return i

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1
