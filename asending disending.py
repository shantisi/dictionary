# Q5.
# Write a Python program to sort (ascending and descending) a dictionary by value.
# Original dictionary : {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Dictionary in ascending order by value : [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# Dictionary in descending order by value : {3: 4, 4: 3, 1: 2, 2: 1, 0:0}


n={1: 2, 3: 4, 4: 3, 2: 1, 0:0,9:7}
li=[]
b={}
for i in n:
    li.append(i)
for h in range (len(li)):
    for j in range (len(li)):
        if li[h]>li[j]:
            li[h],li[j]=li[j],li[h]
for v in li:
    for m in n:
        if m==v:
            b.update({m:n[m]})
print(b)

        # Ascending order value
# n={1: 2, 3: 4, 4: 3, 2: 1, 0:0,9:2}
# for i in n:
#     for j in n:
#         if n[i]<=n[j]:
#             n[i],n[j]=n[j],n[i]
# print(n)

            # discending order

# n={1: 2, 3: 4, 4: 3, 2: 1, 0:0,9:2}
# for i in n:
#     for j in n:
#         if n[i]>=n[j]:
#             n[i],n[j]=n[j],n[i]
# print(n)