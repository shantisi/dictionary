# Q4. Write a Python script to print a dictionary where the keys are numbers between 1 and
# 15 (both included) and the values are square of keys.
# Simple Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12:
# 144, 13: 169, 14: 196, 15: 225}.

# d={}
# n=int(input("enter no"))
# for i in range(n):
#     num=int(input("enter the number"))
#     d.update({num:num*num})
# print(d)

# c={}
# n=int(input("enter no"))
# for i in range(1,n):
#     if i%2==0:
#         d="true"
#     else:
#         d="false"
#     c.update({i:d})
# print(c)

# a={1:"one",4:{5:"five",6:"six"}}
# for i in a:
#     if type(a[i])==dict:
#         for j in a[i]:
#             print(a[i][j],end=" ")
#         print(a[1])
