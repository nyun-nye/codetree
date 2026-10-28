A = input()

# Please write your code here.

cnt = 0
char = A[0]
result = []

for a in A:
    if char == a:
        cnt += 1
    else:
        result.append(char)
        result.append(cnt)
        char = a
        cnt = 1

result.append(char)
result.append(cnt)

result = ''.join(map(str, result))

print(len(result))
print(result)