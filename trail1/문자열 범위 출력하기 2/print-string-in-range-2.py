str = input()
n = int(input())

if n > len(str):
    for s in str[::-1]:
        print(s, end ="")
else:
    for i in range(n):
        print(str[-(i+1)], end="")