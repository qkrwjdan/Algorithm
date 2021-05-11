input = sys.stdin.readline
REMAIN = pow(2,64)

m, n = map(int,input().split())
candies = sorted([int(input()) for _ in range(n)])

rest = sum(candies) - m

ans = 0

for i in range(n):
    x = min(candies[i], rest // (n-i))
    ans += x * x
    rest -= x

print( ans % REMAIN )
