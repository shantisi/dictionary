# Q2. Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

# a="w3resource"
# b={}
# for i in range (len(a)):
#     c=0
#     for j in range (len(a)):
#         if a[i]==a[j]:
#             c=c+1
#         b.update({a[i]:c})
# print(b)

a="w3resource"
d={}
for i in a:
    if i not in d:
        d[i]=0
    d[i]=d[i]+1
print(d)


