# Q33.Python: Print a dictionary line by line
# students = {'Aex':{'class':'V',
# 'rolld_id':2},
# 'Puja':{'class':'V',
# 'roll_id':3}}
# Sample Output:
# Aex
# class : V
# rolld_id : 2
# Puja
# class : V
# roll_id : 3

s = {'Aex':{'class':'V','rolld_id':2},
'Puja':{'class':'V',
'roll_id':3}}
for i in s:
    print(i)
    for j in s[i]:
        print(j,s[i][j])
        







