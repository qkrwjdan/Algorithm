import sys
input = sys.stdin.readline

N,M,H = map(int,input().split())
board = [[0] * N for _ in range(H) ]
for i in range(M):
    a,b = map(int,input().split())
    board[a-1][b-1] = 1
ans = 100

def is_answer():
    global board

    for start in range(N):
        index = start

        for horizon in range(H):
            try :
                if board[horizon][index] == 1:
                    index += 1
                    continue
                
                if board[horizon][index-1] == 1:
                    index -= 1
                    continue
            except :
                continue
        end = index  
        if start != end:
            return False
    return True
    

def dfs(index, x):
    global board
    global ans

    if is_answer():
        ans = min(ans,index)
        return

    if index == 3:
        return

    for a in range(x, H):
        for b in range(N-1):
            if board[a][b] == 1:
                continue
            
            try:
                if board[a][b-1] == 1:
                    continue
                if board[a][b+1] == 1:
                    continue
            except :
                continue

            board[a][b] = 1
            dfs(index+1,a)
            board[a][b] = 0

dfs(0,0)
if ans == 100: print(-1)
else: print(ans)
