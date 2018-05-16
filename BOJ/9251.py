X = input()
Y = input()

dp = [[0 for _ in range(len(Y)+1)] for _ in range(len(X)+1)]

for ix, valx in enumerate(X,1):
    for iy, valy in enumerate(Y,1):
        if valx == valy:
            dp[ix][iy] = dp[ix-1][iy-1] + 1
        else:
            dp[ix][iy] = max(dp[ix-1][iy],dp[ix][iy-1])

print(dp[len(X)][len(Y)])
