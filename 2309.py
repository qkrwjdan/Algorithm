h_list = []
sum = 0;
for _ in range(9):
    n = int(input())
    sum = sum + n
    h_list.append(n)

h_list.sort()

for i in range(9):
    for j in range(1,9-i):
        if h_list[i] + h_list[i+j] == sum - 100:
            for idx,n in enumerate(h_list):
                if idx == i or idx == i+j:
                    continue
                print(n)

            quit()

"""
20
7
23
19
10
15
25
8
13
"""
