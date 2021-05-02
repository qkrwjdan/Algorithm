import sys

w_list = []
h_list = []
biggerThanMe = 0

n = int(input())
for _ in range(n):
    w,h = map(int,sys.stdin.readline().split())
    w_list.append(w)
    h_list.append(h)

for i in range(len(w_list)):
    for j in range(len(w_list)):
        if w_list[i] < w_list[j] and h_list[i] < h_list[j]:
            biggerThanMe += 1
        else :
            pass
    print(biggerThanMe+1)
    biggerThanMe = 0
            

'''
5
55 185
58 183
88 186
60 175
46 155
'''
