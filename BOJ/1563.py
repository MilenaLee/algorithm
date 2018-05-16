n = int(input())
res = 0
dp = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(n+1)]
dp[1][0][0] = dp[1][1][0] = dp[1][0][1] = 1
# O, L, A 각각 한가지 경우씩 존재

for day in range(1,n):
    for late in range(2):
        for absent in range(3):
            if late + absent > day:
                continue
            if late>=2 or absent >= 3:
                continue
            # 내일이 O 일 경우
            dp[day+1][late][0] += dp[day][late][absent]
            # 내일이 L 일 경우
            dp[day+1][late+1][0] += dp[day][late][absent]
            # 내일이 A 일 경우
            dp[day+1][late][absent+1] += dp[day][late][absent]
           
        
for late in range(2):
    for absent in range(3):
        if late + absent > n:
            continue
        res = (res + dp[n][late][absent])%1000000
        

print(res)
        
