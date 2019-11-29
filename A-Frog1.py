def main():
    
    n=int(input())
    h=list(map(int,input().split()))

    dp=[9999999999]*n
    dp[0]=0
    dp[1]=abs(h[1]-h[0])

    for i in range(2,n):
        dp[i]=min(dp[i-1]+abs(h[i]-h[i-1]),dp[i-2]+abs(h[i]-h[i-2]))
        print(dp)

    print(dp[n-1])


if __name__ == "__main__":
    main()