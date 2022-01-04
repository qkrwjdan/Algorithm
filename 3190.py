import sys
input = sys.stdin.readline

N = int(input())
board = []
for i in range(N):
    row = []
    for j in range(N):
        row.append('.')
    board.append(row)

K = int(input())
for _ in range(K):
    y, x = map(int,input().split())
    board[y-1][x-1] = 'A'

L = int(input())
simulation = []
for _ in range(L):
    x, c = input().split()
    simulation.append([int(x),c])

board[0][0] = 'B'
bam = []
bam.append([0,0])
head_x = 0
head_y = 0

timer = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]
direction = 0

def eat(x,y):
    if board[y][x] == 'A':
        board[y][x] = '.'
        return True
    return False

def turn(direction_char):
    """
    direction : D, L
    D : 오른쪽으로 돌기
    L : 왼쪽으로 돌기
    """
    global direction

    if direction_char == 'D':
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4
    

while True:
    timer += 1

    new_head_x = head_x + dx[direction]
    new_head_y = head_y + dy[direction]

    # 벽에 박을 때
    if new_head_x >= N or new_head_y >= N or new_head_x < 0 or new_head_y < 0:
        print(timer)
        exit(0)

    # 자기 몸통에 부딪힐 때
    for body in bam:
        if body[0] == new_head_x and body[1] == new_head_y:
            print(timer)
            exit(0)

    bam.insert(0,[new_head_x, new_head_y])

    if (not eat(new_head_x, new_head_y)):
        bam.pop()

    if simulation:
        if timer == simulation[0][0]:
            turn(simulation[0][1])
            del simulation[0]
    
    head_x = new_head_x
    head_y = new_head_y
