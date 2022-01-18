import sys
input = sys.stdin.readline

N, M = map(int,input().split())
board = []

for i in range(N):
    board.append(list(map(int, input().split())))

# tetrises = [[dx0,dy0],[dx1,dy1],[dx2,dy2],[dx3,dy3]]
tetrises = [
    [[1,0],[0,1],[1,1]], # 네모 1
    [[0,1],[0,2],[0,3]], # 세로 막대 2
    [[1,0],[2,0],[3,0]], # 가로 막대 3
    [[0,1],[0,2],[1,2]], # ㄴ 4 
    [[0,1],[1,0],[2,0]], # 뒤집은 ㄱ 5
    [[1,0],[1,1],[1,2]], # ㄱ 6
    [[1,0],[2,0],[2,-1]], # 뒤집은 ㄴ 7
    [[1,0],[1,-1],[1,-2]], # 8
    [[1,0],[2,0],[2,1]], # 9
    [[1,0],[0,1],[0,2]], # 10
    [[0,1],[1,1],[2,1]], # 11
    [[0,1],[1,1],[1,2]],# 번개 12 
    [[1,0],[1,-1],[2,-1]], # 누운 번개 13
    [[0,-1],[1,-1],[1,-2]], # 14
    [[1,0],[1,1],[2,1]], # 15
    [[-1,0],[1,0],[0,-1]], # ㅗ  16
    [[0,-1],[1,0],[0,1]], # ㅏ  17
    [[-1,0],[0,1],[1,0]], # ㅜ 18
    [[-1,0],[0,1],[0,-1]], # ㅓ 19
]

ans = 0
for y in range(N):
    for x in range(M):
        for tetrise in tetrises:
            sum = board[y][x]
            count = 0
            for dx, dy in tetrise:
                if x + dx < 0 or x + dx >= M or y + dy < 0 or y + dy >= N:
                    break
                count += 1
                sum += board[y+dy][x+dx]
            
            if count == 3:
                ans = max(ans,sum)
            
print(ans)
