import sys 
sys.setrecursionlimit((10**4) +10)
n = int(input())

route = {0:5,1:3,2:4,3:1,4:2,5:0}
dices = []
sums = []

for _ in range(n):
    dices.append(list(map(int,sys.stdin.readline().split())))

def solve(i,val,s):
    if i >= n:
        sums.append(s)
        return

    idx = dices[i].index(val)
    up = route[idx]
    nextVal = dices[i][up]

    maxNum = 0
    for a,num in enumerate(dices[i]):
        if a in [idx,up]:
            continue
        maxNum = max(maxNum,num)
    
    solve(i+1,nextVal,s+maxNum)

for j in range(6):
    solve(0,dices[0][j],0)
ans = max(sums)
print(ans)


'''
5
2 3 1 6 5 4
3 1 2 4 6 5
5 6 4 1 3 2
1 3 6 2 4 5
4 1 6 5 2 3
'''
