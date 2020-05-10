

def main():
    N, W = map(int, input().split())
    weight = [0]
    value = [0]
    for i in range(N):
        w, v = map(int, input().split())
        weight.append(w)
        value.append(v)
    V = sum(value)
    dp = [[float('inf')]*(V+1) for i in range(N+1)]
    for i in range(N):
        dp[i][0] = 0
    # dp[i][val] is the minimum weight required to achieve value v in i elements
    for i in range(1, N+1):
        for val in range(1, V+1):
            if val >= value[i]:
                dp[i][val] = min(dp[i-1][val], dp[i-1][val-value[i]]+weight[i])
            else:
                dp[i][val] = dp[i-1][val]
    ans = 0
    for v in range(V, -1, -1):
        if dp[N][v] <= W:
            ans = v
            break
    print(ans)


if __name__ == "__main__":
    main()
