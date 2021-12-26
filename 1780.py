import sys

N = int(sys.stdin.readline())
all_paper = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
NOT_UNIFIED = 2
ans = [0,0,0]

def check_unified(r_start, c_start, num):
    first = all_paper[r_start][c_start]
    if num == 1:
        return first

    for r in range(r_start,r_start + num):
        for c in range(c_start,c_start + num):
            if all_paper[r][c] is not first:
                return NOT_UNIFIED

    return first

def is_unified_paper(r_start, c_start, num):
    check = check_unified(r_start, c_start, num)

    if check is NOT_UNIFIED:
        num = num // 3
        for i in range(3):
            for j in range(3):
                row_start = r_start + i * num
                col_start = c_start + j * num
                is_unified_paper(row_start, col_start,num)
    else:
        ans[check+1] += 1

is_unified_paper(0,0,N)
for a in ans:
    print(a)
