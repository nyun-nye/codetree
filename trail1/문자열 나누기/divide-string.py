n = int(input())
arr = input().split()

string = ''.join(arr)

cnt = 0
for s in string:
    if cnt == 5:
        print()
        cnt = 0
    print(s, end = "")
    cnt += 1