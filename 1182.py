import sys
from itertools import combinations
N, S = map(int,sys.stdin.readline().split())
integers = list(map(int, sys.stdin.readline().split()))

ans = 0
for i in range(1,N+1):
    comb = combinations(integers,i)
    for c in comb:
        sum = 0
        for num in c:
            sum += num
        if sum == S:
            ans += 1
print(ans)

'''
5 0
-7 -3 -2 5 8
'''
