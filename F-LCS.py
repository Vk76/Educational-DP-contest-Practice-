

def main():
    s = input()
    t = input()
    n, m = len(s), len(t)
    LCS = [[0]*(m+1) for i in range(n+1)]
    # LCS[i][j] is the longest common subsequence of strings s[0...i] and t[0...j]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == t[j-1]:
                LCS[i][j] = LCS[i-1][j-1] + 1
            else:
                LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
    ans = ""
    i, j = n, m
    while i > 0 and j > 0:
        if s[i-1] == t[j-1]:
            ans += s[i-1]
            i -= 1
            j -= 1
        elif LCS[i][j-1] > LCS[i-1][j]:
            j -= 1
        else:
            i -= 1
    print(ans[::-1])


if __name__ == "__main__":
    main()
