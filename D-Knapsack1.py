



def main():
    N,W = map(int, input().split())
    dp = [[0]*(W+1) for i in range(N+1)]
    weight = [0]
    value = [0]
    for i in range(N):
        w,v=map(int, input().split())
        weight.append(w)
        value.append(v)

    # dp[i][w] is the maximum value got with first i items stored in w weight of knapsack
    for i in range(1,N+1):
        for w in range(1,W+1):
            if w>=weight[i]:
                dp[i][w] = max(dp[i-1][w],dp[i-1][w-weight[i]]+value[i])
            else:
                dp[i][w] = dp[i-1][w]
    print(dp[N][W])





if __name__ == "__main__":
    main()