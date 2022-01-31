from collections import deque
import sys
input = sys.stdin.readline

N,L,R = map(int, input().split())
board = []
check = [[0] * N for _ in range(N)]
global_united = []
day = 0

for _ in range(N):
    board.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(x,y):
    global check
    global board
    global global_united

    que = deque()
    united = []
    que.appendleft([x,y])
    united.append([x,y])
    check[y][x] = 1

    while len(que) != 0:
        [x,y] = que.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                if check[ny][nx] == 1:
                    continue
                diff = abs(board[y][x] - board[ny][nx])
                if L <= diff and diff <= R:
                    que.appendleft([nx,ny])
                    united.append([nx,ny])
                    check[ny][nx] = 1
    if len(united) != 1:
        global_united.append(united)

while True:
    for x in range(N):
        for y in range(N):
            if check[y][x] == 1:
                continue

            bfs(x,y)

    if len(global_united) == 0:
        print(day)
        break

    day += 1

    for group in global_united:
        summation = 0

        for [x,y] in group:
            summation += board[y][x]
        
        result = summation // len(group)

        for [x,y] in group:
            board[y][x] = result

    check = [[0] * N for _ in range(N)]
    global_united = []
