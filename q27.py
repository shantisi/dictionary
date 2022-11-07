# Q27.Write a Python program to count the values associated with key in a dictionary.


data= [{'id': 1, 'success': True, 'name': 'Lary'},
{'id': 2, 'success': False, 'name': 'Rabi'},
{'id': 3, 'success': True, 'name': 'Alex'}]
s=0
for i in data:
    d=i["id"]
    s=s+d
print(s)


