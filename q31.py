# Q31.. Write a Python program to get the top three items in shop. Go to
# the editor
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55,
# 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3

list={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
b={}
top1=0
top2=0
top3=0
for i in (list):
    for j in list:
        if list[j]>top1:
            top1=list[j]
            n=j
        elif list[j]>top2 and top1 !=list[j]:
            top2=list[j]
            m=j
        elif list[j]>top3 and top1!=list[j] and top2!=list[j]:
            top3=list[j]
            p=j
print(top1,n)
print(top2,m)
print(top3,p)

