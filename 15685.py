import sys
input = sys.stdin.readline

N = int(input())
X = 0
Y = 1
board = [[0] * 101 for i in range(101)]
dx = [1,0,-1,0]
dy = [0,-1,0,1]
answer = 0

def rotate90(rotation_point_x, rotation_point_y, x, y):
    return [rotation_point_y-y+rotation_point_x, x-rotation_point_x+rotation_point_y]

def check_dragon_curve(x,y,d,g):
    dragon_curve = [
        [x, y], 
        [x+dx[d], y+dy[d]]
        ]

    for i in range(g):
        length = len(dragon_curve)
        for j in range(length - 2,-1,-1):
            
            rotation_point_x = dragon_curve[length-1][X]
            rotation_point_y = dragon_curve[length-1][Y]
            x = dragon_curve[j][X]
            y = dragon_curve[j][Y]

            rotated_dot = rotate90(rotation_point_x, rotation_point_y, x, y)
            dragon_curve.append(rotated_dot)
    
    return dragon_curve

for i in range(N):
    x,y,d,g = map(int,input().split())

    dragon_curve = check_dragon_curve(x,y,d,g)
    for [x,y] in dragon_curve:
        board[y][x] = 1
    
for y in range(100):
    for x in range(100):
        if board[y][x] == 1 and board[y][x+1] == 1 and board[y+1][x] == 1 and board[y+1][x+1] == 1:
            answer += 1
print(answer)
