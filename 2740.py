import sys

N, M = map(int,sys.stdin.readline().split())

A = []
for i in range(N):
    es = list(map(int, sys.stdin.readline().split()))
    A.append(es)

M, K = map(int,sys.stdin.readline().split())
B = []
for i in range(M):
    es = list(map(int, sys.stdin.readline().split()))
    B.append(es)

C = [[0 for _ in range(K)] for _ in range(N)]
for i in range(N):
    for j in range(K):
        for k in range(M):
            C[i][j] += A[i][k] * B[k][j]

for i in C:
    print(*i)
