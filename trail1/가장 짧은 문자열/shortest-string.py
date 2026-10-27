str1 = input()
str2 = input()
str3 = input()

max = max([len(str1), len(str2), len(str3)])
min = min([len(str1), len(str2), len(str3)])

print(max-min)