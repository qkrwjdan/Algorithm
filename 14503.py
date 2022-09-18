import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
_map = []
r, c, d = list(map(int, input().split()))
robot_position = [c, r]
cleaned_sum = 0
north = [0, -1]
east = [1, 0]
south = [0, 1]
west = [-1, 0]
direction = [north, east, south, west]  # 북, 동, 남, 서 순서.
CLEANED = 2
NOT_CLEANED = 0
WALL = 1
X = 0
Y = 1

for _ in range(N):
    row = list(map(int, input().split()))
    _map.append(row)


# def print_map(m):
#     for i in range(len(m)):
#         for j in range(len(m[i])):
#             print("{:^3}".format(m[i][j]), end="")
#         print()

while True:
    # print()
    # print_map(_map)

    if _map[robot_position[Y]][robot_position[X]] == NOT_CLEANED:
        cleaned_sum += 1
        _map[robot_position[Y]][robot_position[X]] = CLEANED

    now_direction = d
    enable = False
    for i in range(4):
        now_direction = (d - (i + 1)) % 4
        now_x = robot_position[X] + direction[now_direction][X]
        now_y = robot_position[Y] + direction[now_direction][Y]

        if _map[now_y][now_x] != WALL and _map[now_y][now_x] != CLEANED:
            enable = True
            robot_position[X] = now_x
            robot_position[Y] = now_y
            d = now_direction
            break

    if enable:
        continue

    backward = (d + 2) % 4
    back_x = robot_position[X] + direction[backward][X]
    back_y = robot_position[Y] + direction[backward][Y]

    if _map[back_y][back_x] != WALL:
        robot_position[X] = back_x
        robot_position[Y] = back_y
        continue

    break

print(cleaned_sum)
