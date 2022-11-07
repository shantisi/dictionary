# Q29.Write a Python program to sort a list alphabetically in a dictionary.

num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
for i in num:
    for j in num:
        if num[i]<=num[j]:
            num[i],num[j]=num[j],num[i]
print(num)