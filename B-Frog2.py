#This might give TLE 
#Use same logic in C++14 to avoid TLE

def main():
    
    n,k=map(int,input().split())
    h=list(map(int,input().split()))

    dp=[9999999999]*n
    dp[0]=0
    dp[1]=abs(h[1]-h[0])

    for i in range(2,n):
        for j in range(1,k+1):
            if i-j>=0:
                dp[i]=min(dp[i],dp[i-j]+abs(h[i]-h[i-j]))
            else:
                break

    print(dp[n-1])

if __name__ == "__main__":
    main()