arr = [input() for _ in range(10)]
char = input()

cnt = 0

for a in arr:
    if a[-1] == char:
        print(a)
        cnt += 1

if cnt == 0:
    print("None")