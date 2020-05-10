
MOD = int(1e9)+7
def main():
    H, W = map(int, input().split())
    mat = []
    for i in range(H):
        mat.append(input())

    ways = [[0]*(W+1) for i in range(H+1)]
    ways[0][1] = 1
    for i in range(1, H+1):
        for j in range(1, W+1):
            if mat[i-1][j-1] != '#':
                ways[i][j] = (ways[i-1][j]+ways[i][j-1])%MOD
    print(ways[H][W])


if __name__ == "__main__":
    main()
