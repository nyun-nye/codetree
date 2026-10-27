N = int(input())
arr = [input() for _ in range(N)]

sum = 0
for a in arr:
    sum += len(a)

cnt = 0
for a in arr:
    if a[0] == 'a':
        cnt += 1

print(sum, cnt)