n = int(input())
arr = [input() for _ in range(n)]
char = input()

cnt = 0 
sum = 0
for a in arr:
    if a[0] == char:
        cnt += 1
        sum += len(a)

print(cnt, f"{(sum/cnt):.2f}")