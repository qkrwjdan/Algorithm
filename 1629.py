import sys
import time

A,B,C = map(int, sys.stdin.readline().split())

# A를 10번 곱한 것 -> A를 5번 곱한 것 * A를 5번 곱한 것
# A를 5번 곱한 것 -> A를 2번 곱한 것 * A를 2번 곱한 것 * A
# 곱하는 횟수를 줄이는 것이 좋다. 

def p(a,b): # a = 곱하는 수, b = 곱하는 횟수
    if b > 2:
        if b % 2 == 0:
            tmp = p(a,b // 2)
            return (tmp * tmp) % C
        else :
            tmp = p(a,b // 2)
            return (tmp * tmp * a) % C
    elif b == 2:
        return (a * a) % C
    else:
        return a % C

ans = p(A,B)
print(ans)
