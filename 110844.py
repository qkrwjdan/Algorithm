import sys
REMAIN = 1000000000
input = sys.stdin.readline

n = int(input())

if n == 1:
    print(9)
    quit()

dp = [[[] for _ in range(10)] for _ in range(n+1)]

dp[0][0] = 0
for i in range(9):
    dp[0][i+1] = 1

for i in range(1,n):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1] % REMAIN
        elif j == 9:
            dp[i][j] = dp[i-1][j-1] % REMAIN
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % REMAIN

# print(dp)
print(dp)
print(sum(dp[n-1]) % REMAIN)
