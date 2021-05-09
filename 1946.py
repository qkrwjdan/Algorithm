import sys
input = sys.stdin.readline

testCase = int(input())

for _ in range(testCase):

    n = int(input())
    scoreList = []

    for _ in range(n):
        s0, s1 = map(int, input().split())
        scoreList.append([s0,s1])
    
    scoreList.sort(key = lambda x : x[0])
    
    criterion = n + 1
    ans = 0

    for [ _,s1 ] in scoreList:
        if s1 < criterion:
            criterion = s1
            ans += 1
    
    print(ans)
