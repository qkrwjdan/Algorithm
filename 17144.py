import sys
input = sys.stdin.readline

R, C, T = list(map(int, input().split()))
_map = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

clockwise_dx = [0, 1, 0, -1]
clockwise_dy = [-1, 0, 1, 0]

counterclockwise_dx = [0, 1, 0, -1]
counterclockwise_dy = [1, 0, -1, 0]

upper_air_cleaner = []
lower_air_cleaner = []


def get_tmp_map():
    _tmp_map = []
    for _ in range(R):
        c = [0 for _ in range(C)]
        _tmp_map.append(c)
    return _tmp_map


# def print_map(m):
#     print()
#     for row in m:
#         print(*row)


for i in range(R):
    c = list(map(int, input().split()))
    for x in range(len(c)):
        if c[x] == -1:
            upper_air_cleaner = [x, i-1]
            lower_air_cleaner = [x, i]

    _map.append(c)


def spread():
    global _map
    global dx
    global dy

    tmp_map = get_tmp_map()
    for i in range(R):
        for j in range(C):
            amount_left = _map[i][j]
            if amount_left > 4:  # 퍼질 먼지 잇음.
                enable_direction = []

                for n in range(4):
                    new_coordinate_x = j + dx[n]
                    new_coordinate_y = i + dy[n]

                    if new_coordinate_x < 0 or new_coordinate_x >= C or new_coordinate_y < 0 or new_coordinate_y >= R:
                        continue
                    if _map[new_coordinate_y][new_coordinate_x] != -1:
                        enable_direction.append(n)

                amount_of_diffusion = int(amount_left / 5)
                amount_left_over = amount_left - \
                    int(amount_left / 5) * len(enable_direction)

                tmp_map[i][j] = tmp_map[i][j] + amount_left_over
                for n in enable_direction:
                    new_coordinate_x = j + dx[n]
                    new_coordinate_y = i + dy[n]
                    tmp_map[new_coordinate_y][new_coordinate_x] = tmp_map[new_coordinate_y][new_coordinate_x] + \
                        amount_of_diffusion
            elif amount_left > 0:
                tmp_map[i][j] = tmp_map[i][j] + amount_left

    _map = tmp_map
    _map[upper_air_cleaner[1]][upper_air_cleaner[0]] = -1
    _map[lower_air_cleaner[1]][lower_air_cleaner[0]] = -1


def clean_upper_air():
    d = 0

    x = upper_air_cleaner[0] + clockwise_dx[d]
    y = upper_air_cleaner[1] + clockwise_dy[d]

    _map[y][x] = 0

    while True:
        if upper_air_cleaner[0] == x and upper_air_cleaner[1] == y:
            break

        new_x = x + clockwise_dx[d]
        new_y = y + clockwise_dy[d]

        if new_x < 0 or new_x >= C or new_y < 0 or new_y > upper_air_cleaner[1]:
            d = (d + 1) % 4
            continue

        if _map[new_y][new_x] == -1:
            _map[y][x] = 0
        else:
            _map[y][x] = _map[new_y][new_x]

        x = new_x
        y = new_y

    _map[upper_air_cleaner[1]][upper_air_cleaner[0]] = -1
    _map[lower_air_cleaner[1]][lower_air_cleaner[0]] = -1


def clean_lower_air():
    d = 0

    x = lower_air_cleaner[0] + counterclockwise_dx[d]
    y = lower_air_cleaner[1] + counterclockwise_dy[d]

    _map[y][x] = 0

    while True:
        if lower_air_cleaner[0] == x and lower_air_cleaner[1] == y:
            break

        new_x = x + counterclockwise_dx[d]
        new_y = y + counterclockwise_dy[d]

        if new_x < 0 or new_x >= C or new_y < lower_air_cleaner[1] or new_y >= R:
            d = (d + 1) % 4
            continue

        if _map[new_y][new_x] == -1:
            _map[y][x] = 0
        else:
            _map[y][x] = _map[new_y][new_x]

        x = new_x
        y = new_y

    _map[upper_air_cleaner[1]][upper_air_cleaner[0]] = -1
    _map[lower_air_cleaner[1]][lower_air_cleaner[0]] = -1


for i in range(T):
    spread()
    clean_upper_air()
    clean_lower_air()
    # print_map(_map)


def count_dust(m):
    sum_dust = 0
    for row in m:
        for c in row:
            if c == -1:
                continue
            sum_dust = sum_dust + c

    return sum_dust


print(count_dust(_map))

"""
8 8 2
3 0 0 0 0 0 0 0
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0


7 8 1000
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
0 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
-1 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0

7 6 1
1 2 3 4 5 6
6 5 4 3 2 1
-1 2 3 4 5 6
-1 6 5 4 3 2
1 2 3 4 5 6
6 5 4 3 2 1
1 2 3 4 5 6

"""
