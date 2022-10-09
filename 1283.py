import sys

input = sys.stdin.readline
N = int(input())
assigned = []
result = []

for _ in range(N):
    words = input().split()
    done = False

    for i in range(len(words)):
        if not words[i][0].lower() in assigned:
            assigned.append(words[i][0].lower())
            words[i] = '[' + words[i][0] + ']' + words[i][1:]
            done = True
            break

    if done:
        result.append(words)
        continue

    for i in range(len(words)):
        for j in range(len(words[i])):

            if not words[i][j].lower() in assigned:
                assigned.append(words[i][j].lower())
                words[i] = words[i][:j] + \
                    '[' + words[i][j] + ']' + words[i][j+1:]
                done = True
                break

        if done:
            break
    result.append(words)
    continue

for r in result:
    print(' '.join(r))
