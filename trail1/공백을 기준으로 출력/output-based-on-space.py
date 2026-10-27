str1 = input()
str2 = input()

arr1 = list(map(str, str1.split()))
arr2 = list(map(str, str2.split()))

for a in arr1:
    print(a, end = "")
for a in arr2:
    print(a, end = "")