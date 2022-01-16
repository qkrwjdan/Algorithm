import sys
input = sys.stdin.readline
import copy

N,M = map(int,input().split())
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
board = []
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]
ans = 100
cctv_list = []

for _ in range(N):
    board.append(list(map(int,input().split())))

class CCTV():
    def __init__(self,x,y,type):
        self.x = x
        self.y = y
        self.type = type

def find_cctv(board):
    for i in range(N):
        for j in range(M):
            if board[i][j] != 6 and board[i][j] != 0:
                cctv_list.append(CCTV(j,i,board[i][j]))

def get_blindspot(board):
    spot = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                spot += 1
    return spot

def fill(board,x,y,directions):
    for d in directions:
        nx = x
        ny = y
        while True:
            nx = nx + dx[d]
            ny = ny + dy[d]
            
            if nx < 0 or ny < 0 or nx >= M or ny >=N:
                break
            if board[ny][nx] == 6:
                break
            
            if board[ny][nx] == 0:
                board[ny][nx] = 7    
    return board

def dfs(cnt, board):
    global ans

    if cnt == len(cctv_list):
        num = get_blindspot(board)
        ans = min(ans,num)
        return
    
    cctv = cctv_list[cnt]
    for directions in mode[cctv.type]:
        temp_board = copy.deepcopy(board)
        temp_board = fill(temp_board,cctv.x,cctv.y,directions)
        dfs(cnt+1,temp_board)
        
find_cctv(board)
dfs(0,board)
print(ans)
