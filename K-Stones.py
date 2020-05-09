

def main():
    n, K = map(int, input().split())
    a = list(map(int, input().split()))

    # dp[i] is true if First player wins with i tiles left
    dp = [False]*(K+1)
    for k in range(1, K+1):
        for i in a:
            if k >= i and not dp[k-i]:
                dp[k] = True
    print(['Second', 'First'][dp[K]])


if __name__ == "__main__":
    main()
