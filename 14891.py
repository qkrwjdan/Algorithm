import sys
input = sys.stdin.readline

N = 0
S = 1
left = 0
right = 1
clockwise = 1
counterclockwise = -1
wheels = [] 

for i in range(4):
    wheels.append(input().strip())

attached_tooth = [[6,2],[6,2],[6,2],[6,2]]

K = int(input())
simulation = []
for i in range(K):
    simulation.append(list(map(int,input().split())))

def rotate(target, direction):
    global attached_tooth

    if direction is clockwise:
        attached_tooth[target][left] = (attached_tooth[target][left] - 1) % 8 
        attached_tooth[target][right] = (attached_tooth[target][right] - 1) % 8 

    elif direction is counterclockwise:
        attached_tooth[target][left] = (attached_tooth[target][left] + 1) % 8
        attached_tooth[target][right] = (attached_tooth[target][right] + 1) % 8

for inst in simulation:
    target = inst[0] - 1
    direction = inst[1]

    if target == 0 : # 1st wheel
        if wheels[target][attached_tooth[target][right]] != wheels[target+1][attached_tooth[target+1][left]]:
            if wheels[target+1][attached_tooth[target+1][right]] != wheels[target+2][attached_tooth[target+2][left]]:
                if wheels[target+2][attached_tooth[target+2][right]] != wheels[target+3][attached_tooth[target+3][left]]:
                    rotate(target+3, direction * -1)
                rotate(target+2, direction)
            rotate(target+1, direction * -1)

    elif target == 1: # 2st wheel
        if wheels[target][attached_tooth[target][right]] != wheels[target+1][attached_tooth[target+1][left]]:
            if wheels[target+1][attached_tooth[target+1][right]] != wheels[target+2][attached_tooth[target+2][left]]:
                rotate(target+2, direction)
            rotate(target+1, direction * -1)
        
        if wheels[target][attached_tooth[target][left]] != wheels[target-1][attached_tooth[target-1][right]]:
            rotate(target-1, direction * -1)

    elif target == 2: # 3st wheel
        if wheels[target][attached_tooth[target][left]] != wheels[target-1][attached_tooth[target-1][right]]:
            if wheels[target-1][attached_tooth[target-1][left]] != wheels[target-2][attached_tooth[target-2][right]]:
                rotate(target-2, direction)
            rotate(target-1, direction * -1)
        
        if wheels[target][attached_tooth[target][right]] != wheels[target+1][attached_tooth[target+1][left]]:
            rotate(target+1, direction * -1)

    elif target == 3: # 4st wheel
        if wheels[target][attached_tooth[target][left]] != wheels[target-1][attached_tooth[target-1][right]]:
            if wheels[target-1][attached_tooth[target-1][left]] != wheels[target-2][attached_tooth[target-2][right]]:
                if wheels[target-2][attached_tooth[target-2][left]] != wheels[target-3][attached_tooth[target-3][right]]:
                    rotate(target-3, direction * -1)
                rotate(target-2, direction)
            rotate(target-1, direction * -1)

    rotate(target, direction)

ans = 0
for i in range(4):
    top = ( attached_tooth[i][left] + 2 ) % 8
    if int(wheels[i][top]) == S:
        ans = ans + pow(2,i)

print(ans)
