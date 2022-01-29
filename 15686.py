from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

homes = []
chicken_homes = []
alive = []

answer = 100000

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            homes.append([j,i])
        if board[i][j] == 2:
            chicken_homes.append([j,i])

check = [0] * len(chicken_homes)

def distance(home1, home2):
    return abs(home1[0] - home2[0]) + abs(home1[1] - home2[1])

def get_chicken_distance(alive_chicken_homes):
    city_chicken_distance = 0

    for home in homes:
        min_distance = 100000
        for chicken_home in alive_chicken_homes:
            min_distance = min(min_distance,distance(home, chicken_home)) 
        
        city_chicken_distance += min_distance
    return city_chicken_distance

comb = list(combinations(chicken_homes, M))
for c in comb:
    answer = min(answer, get_chicken_distance(c))
print(answer)
