import sys

input = sys.stdin.readline

n,k = map(int,input().split())

P = list(map(int,input().split()))

s_list = [0 for _ in range(k)]

for i in range(0,n):
    for j in range(k):
        if P[i] > s_list[j]:
            s_list[j] = P[i]
            break
        if j == k-1:
            print("NO")
            quit()
print("YES")



'''
3 2
3 2 1

10 3
4 1 3 2 5 6 8 9 7 10
'''
