import sys
input = sys.stdin.readline

N = int(input())
max_P = 0
t_list = []
p_list = []

for i in range(N):
    T, P = list(map(int, input().split()))
    t_list.append(T-1)
    p_list.append(P)


def is_available(n, now_T, remain_T):
    if remain_T > 0:
        return False

    if n + now_T >= N:
        return False

    return True


def dfs(n, remain_T, sum_P):
    global max_P
    if n == N:
        max_P = max(max_P, sum_P)
        return

    now_T = t_list[n]
    now_P = p_list[n]

    can_consult = is_available(n, now_T, remain_T)

    if not can_consult:
        dfs(n+1, remain_T-1, sum_P)
    else:
        # 상담할 때
        dfs(n+1, now_T, sum_P + now_P)
        # 상담하지 않을 때
        dfs(n+1, 0, sum_P)


dfs(0, 0, 0)
print(max_P)

"""
15
15 150
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
"""

"""
15
16 150
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
2 11
1 12
"""
