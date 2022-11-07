# Q24.
# Write a Python program to combine values in python list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1',
# 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300}}

a=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, 
{'item': 'item1','amount': 750}]
g={}
for i in a:
    key=i["item"]
    value=i["amount"]
    if  key not in g:
        b= {key:value}
        g.update(b)  
    else:
       g[key]+=value
print(g)




 