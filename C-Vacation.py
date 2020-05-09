import sys
sys.setrecursionlimit(1000000)

dp = [[-1 for j in range(3)]for i in range(99999999)]


def solve(l, n, i, col):

    if i >= n:
        return 0
    if dp[i][col] != -1:
        return dp[i][col]

    mx = -1
    for j in range(3):
        if j != col:
            mx = max(mx, l[i][col]+solve(l, n, i+1, j))
    dp[i][col] = mx
    return mx


def main():
    n = int(input())
    l = [[0 for i in range(3)]for j in range(n)]
    for i in range(n):
        l[i][0], l[i][1], l[i][2] = map(int, input().split())
    print(max(solve(l, n, 0, 0), solve(l, n, 0, 1), solve(l, n, 0, 2)))


if __name__ == "__main__":
    main()
