
MOD = int(1e9)+7


def main():
    n, K = map(int, input().split())
    a = list(map(int, input().split()))

    # dp[i][j] is the number of ways to distribute j candies to first i people
    dp = [[0]*(K+1) for i in range(n+1)]
    prefix = [[0]*(K+1) for i in range(n+1)]
    prefix[0] = [1]*(K+1)
    for i in range(1, n+1):
        for j in range(K+1):
            start = j - min(a[i-1], j)-1
            end = j
            dp[i][j] = (prefix[i-1][end] - \
                (prefix[i-1][start] if start >= 0 else 0))%MOD
            prefix[i][j] = (prefix[i][j-1] + dp[i][j]) % MOD

    print(dp[n][K]%MOD)


if __name__ == "__main__":
    main()
