str = input()
char = input()

cnt = 0

for i in range(len(str)):
    if str[i] == char:
        cnt += 1

print(cnt)