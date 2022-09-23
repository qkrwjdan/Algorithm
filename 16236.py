import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
_map = []

baby_shark_position = []
X = 0
Y = 1
D = 2
S = 3
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
baby_shark_size = 2
exp = 2
sum_dist = 0

for i in range(N):
    row = list(map(int, input().split()))
    for r in range(len(row)):
        if row[r] == 9:
            baby_shark_position = [r, i]

    _map.append(row)


def search_feed(m, x, y):
    que = deque()
    feeds = []
    distance = 0
    visited = [[False for _ in range(N)] for _ in range(N)]

    que.append([x, y, distance])
    visited[y][x] = True

    while que:
        [new_x, new_y, dist] = que.popleft()

        for i in range(4):
            dif_x = new_x + dx[i]
            dif_y = new_y + dy[i]

            if dif_x < 0 or dif_x >= N or dif_y < 0 or dif_y >= N:
                continue
            if visited[dif_y][dif_x]:
                continue
            if m[dif_y][dif_x] > baby_shark_size:
                continue
            if m[dif_y][dif_x] > 0 and m[dif_y][dif_x] != 9 and m[dif_y][dif_x] < baby_shark_size:
                feeds.append([dif_x, dif_y, dist, m[dif_y][dif_x]])

            visited[dif_y][dif_x] = True
            que.append([dif_x, dif_y, dist + 1])

    return feeds


while True:
    feeds = search_feed(_map, baby_shark_position[X], baby_shark_position[Y])
    if not feeds:
        break

    feeds.sort(key=lambda x: (x[D], x[Y], x[X]))

    feed_x, feed_y, feed_dist, feed_size = feeds[0]

    _map[baby_shark_position[Y]][baby_shark_position[X]] = 0
    baby_shark_position = [feed_x, feed_y]
    _map[feed_y][feed_x] = 9

    exp -= 1
    if exp == 0:
        baby_shark_size += 1
        exp = baby_shark_size

    sum_dist += (feed_dist + 1)

print(sum_dist)
