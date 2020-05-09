
def main():
    n = int(input())
    a = list(map(int, input().split()))

    dp = [[0 for i in range(n+2)]for i in range(n+2)]
    # dp [start][end] is the diffence between X and Y
    # such for range start to end
    for start in range(n, 0, -1):
        for end in range(start, n+1):
            if start == end:
                dp[start][end] = a[start-1]
            else:
                dp[start][end] = max(a[start-1]-dp[start+1]
                                     [end], a[end-1]-dp[start][end-1])
    print(dp[1][n])


if __name__ == "__main__":
    main()
