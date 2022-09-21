import sys
from itertools import combinations
from collections import deque
from copy import deepcopy

input = sys.stdin.readline
N, M = list(map(int, input().split()))
_map = []
viruses = []
X = 0
Y = 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(N):
    row = list(map(int, input().split()))
    _map.append(row)

max_idx = N * M
idx_list = list(range(max_idx))
max_safe_area_num = 0

choices = combinations(idx_list, 3)


def find_virus(m):
    global viruses
    for i in range(N):
        for j in range(M):
            area = m[i][j]
            if area == 2:
                viruses.append([j, i])


find_virus(_map)


def print_map(m):
    for i in m:
        for j in i:
            print("%3d" % j, end="")
        print()


# def break_wall(m, choice):
#     for idx in choice:
#         x = idx % M
#         y = idx // M
#         m[y][x] = 0

#     return m


def put_wall(m, choice):
    for idx in choice:
        x = idx % M
        y = idx // M

        if m[y][x] != 0:
            return False

        m[y][x] = 1

    return m


def spread_virus(m):
    visited = [[0 for i in range(M)] for j in range(N)]
    que = deque()

    for virus in viruses:
        que.append([virus[X], virus[Y]])

    while que:
        [x, y] = que.popleft()

        if m[y][x] == 0:
            m[y][x] = 2
        visited[y][x] = 1

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if new_x < 0 or new_x >= M or new_y < 0 or new_y >= N:
                continue

            if visited[new_y][new_x] == 0 and m[new_y][new_x] == 0:
                que.append([new_x, new_y])

    return m


def count_safe_area(m):
    num = 0
    for i in m:
        for j in i:
            if j == 0:
                num += 1

    return num


for choice in list(choices):
    new_map = deepcopy(_map)
    new_map = put_wall(new_map, choice)
    if not new_map:
        continue

    spreaded_map = spread_virus(new_map)
    safe_area_num = count_safe_area(spreaded_map)
    max_safe_area_num = max(max_safe_area_num, safe_area_num)

print(max_safe_area_num)
