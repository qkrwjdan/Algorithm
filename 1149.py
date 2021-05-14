import sys

input = sys.stdin.readline

n = int(input())

lst = []

for _ in range(n):
    r,g,b = map(int,input().split())
    lst.append([r,g,b])

dp = [[[],[],[]] for _ in lst]

dp[0][0] = lst[0][0]
dp[0][1] = lst[0][1]
dp[0][2] = lst[0][2]

for i in range(1,len(lst)):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + lst[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + lst[i][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + lst[i][2]

print(min(dp[n-1]))
