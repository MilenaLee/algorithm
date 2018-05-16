n, k = map(int, input().split())

coin = []

for _ in range(n):
    coin.append(int(input()))
    
dp = [1] + [0] * k

for c in coin:
    for money in range(1,k+1): 
        if money - c >= 0:
            dp[money] += dp[money-c]
        
print(dp[k])
