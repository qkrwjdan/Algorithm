import sys

p = 1000000007
N,K = map(int,sys.stdin.readline().split())

# nCr = n! % p / ((n-k)! * k!) % p 
# n! % p / ((n-k)! * k!) % p = (n! % p) * ((k! % p * (n-k)! % p) ^ p-2) % p

# factorial 구하기
dp = [ 0 for _ in range(N+1)]
dp[0] = 1
dp[1] = 1
for i in range(2, N+1):
    dp[i] = (dp[i-1] * i) % p 

# pow 구하기
def fast_pow(a,b):
    ans = 1
    while b :
        if( b & 1):
            ans = (ans * a) % p
        b = b // 2
        a = (a * a) % p
    return ans % p

A = dp[N]
B = (dp[N-K] * dp[K]) % p

print((A * fast_pow(B,p-2)) % p) 
