import sys 
from collections import deque
input = sys.stdin.readline

N,M,K = map(int,input().split())
A = []
trees = []

R = 0
C = 1
AGE = 2

dr = [-1,-1,-1,0,0,1,1,1]
dc = [-1,0,+1,-1,+1,-1,0,1]

trees = [[deque()for _ in range(N)] for __ in range(N)]

for _ in range(N):
    A.append(list(map(int,input().split())))

for _ in range(M):
    r,c,age = map(int,input().split())
    trees[r-1][c-1].appendleft(age)

board = [[5] * N for _ in range(N)]

for year in range(K):
    for r in range(N):
        for c in range(N):
            tree_num = len(trees[r][c])

            for idx in range(tree_num):
                if board[r][c] >= trees[r][c][idx] :
                    board[r][c] -= trees[r][c][idx]
                    trees[r][c][idx] += 1
                else:
                    for _ in range(idx, tree_num):
                        board[r][c] += trees[r][c].pop() // 2
                    break

    for r in range(N):
        for c in range(N):
            for t in trees[r][c]:
                if t % 5 == 0:
                    for i in range(8):
                        nr = r + dr[i]
                        nc = c + dc[i]

                        if nr >= 0 and nr < N and nc >= 0 and nc < N:
                            trees[nr][nc].appendleft(1)
            board[r][c] += A[r][c]

sum = 0
for r in range(N):
    for c in range(N):
        sum += len(trees[r][c])

print(sum)
