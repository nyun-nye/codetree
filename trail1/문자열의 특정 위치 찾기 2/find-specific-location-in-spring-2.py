str1 = "apple"
str2 = "banana"
str3 = "grape"
str4 = "blueberry"
str5 = "orange"

char = input()
arr = [str1, str2, str3, str4, str5]

cnt = 0

for i in range(5):
    if arr[i][2] == char or arr[i][3] == char:
        cnt += 1
        print(arr[i])

print(cnt)