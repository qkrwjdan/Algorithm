import sys
from termios import VEOL
input = sys.stdin.readline

dx = [0, 0, 0, 1, -1]
dy = [0, -1, 1, 0, 0]
sharks = []
king = -1
result = 0

ROW = 0
COL = 1
VELOCITY = 2
DIRECTION = 3
SIZE = 4

R, C, M = list(map(int, input().split()))
R = R - 1
C = C - 1


def move(r, c, s, d):

    if d == 3 or d == 4:  # 오른 왼
        T = C*2  # 주기 : 자기자리로 & 같은방향

        if d == 3:
            real_s = s % T  # 실제 이동
            if real_s <= C-c:
                nr, nc = r, c+real_s
                if nc == C:
                    d = 4

            elif C-c < real_s <= T-c:
                nr, nc = r, C - (real_s - (C-c))
                d = 4
                if nc == 0:
                    d = 3
            else:
                nr, nc = r, real_s - (T-c)

        elif d == 4:
            real_s = s % T  # 실제 이동
            if real_s <= c:
                nr, nc = r, c-real_s
                if nc == 0:
                    d = 3

            elif c < real_s <= T-(C-c):
                nr, nc = r, real_s - c
                d = 3
                if nc == C:
                    d = 4
            else:
                nr, nc = r, c + T - real_s  # 원래 위치 + 주기 - 이동거리

    if d == 1 or d == 2:  # 위 아래
        T = R*2  # 주기 : 자기자리로 & 같은방향

        if d == 2:
            real_s = s % T  # 실제 이동
            if real_s <= R-r:
                nr, nc = r+real_s, c
                if nr == R:  # 방향전환 왼쪽
                    d = 1

            elif R-r < real_s <= T-r:
                nr, nc = R - (real_s - (R-r)), c
                d = 1
                if nr == 0:  # 방향전환 오른쪽
                    d = 2
            else:
                nr, nc = real_s - (T-r), c

        elif d == 1:
            real_s = s % T  # 실제 이동
            if real_s <= r:
                nr, nc = r-real_s, c
                if nr == 0:
                    d = 2

            elif r < real_s <= T-(R-r):
                nr, nc = (real_s - r), c
                d = 2
                if nr == R:
                    d = 1
            else:
                nr, nc = r + T - real_s, c  # 원래 위치 + 주기 - 이동거리

    return (nr, nc, s, d)


def reverse_direction(d):
    if d == 1:
        return 2
    elif d == 2:
        return 1
    elif d == 3:
        return 4
    elif d == 4:
        return 3


for _ in range(M):
    r, c, s, d, z = list(map(int, input().split()))
    sharks.append([r-1, c-1, s, d, z])

sharks.sort(key=lambda x: x[ROW])

for _ in range(C+1):
    sharks.sort(key=lambda x: x[ROW])

    king += 1
    map_dict = {}

    for i in range(len(sharks)):
        shark = sharks[i]
        if shark[COL] == king:
            result += shark[SIZE]
            del sharks[i]
            break

    # move shark
    for i in range(len(sharks)):
        shark = sharks[i]

        br = shark[ROW]
        bc = shark[COL]
        bv = shark[VELOCITY]
        bd = shark[DIRECTION]

        nr, nc, nv, nd = move(br, bc, bv, bd)
        sharks[i][ROW] = nr
        sharks[i][COL] = nc
        sharks[i][VELOCITY] = nv
        sharks[i][DIRECTION] = nd

        # for _ in range(shark[VELOCITY]):
        #     shark_dx = dx[shark[DIRECTION]]
        #     shark_dy = dy[shark[DIRECTION]]

        #     moved_x = shark[COL] + shark_dx
        #     moved_y = shark[ROW] + shark_dy

        #     if moved_x < 0 or moved_x >= C or moved_y < 0 or moved_y >= R:
        #         new_direction = reverse_direction(shark[DIRECTION])
        #         sharks[i][DIRECTION] = new_direction

        #         shark_dx = dx[new_direction]
        #         shark_dy = dy[new_direction]

        #         moved_x = shark[COL] + shark_dx
        #         moved_y = shark[ROW] + shark_dy

        #     sharks[i][COL] = moved_x
        #     sharks[i][ROW] = moved_y

        shark = sharks[i]

        r = sharks[i][ROW]
        c = sharks[i][COL]

        try:
            if map_dict[(r, c)]:
                s = map_dict[(r, c)]
                if s[SIZE] < sharks[i][SIZE]:
                    map_dict[(r, c)] = sharks[i]
        except:
            map_dict[(r, c)] = sharks[i]

    new_sharks = []
    keys = list(map_dict.keys())
    keys.sort(key=lambda x: x[0])

    for k in keys:
        new_sharks.append(map_dict[k])

    sharks = new_sharks

print(result)
