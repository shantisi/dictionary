# Q7.
# Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# for i in dic2:
#     dic1.update(dic2)
#     dic1.update(dic3)
# print(dic1)

date=int(input("enter the date"))
month=int(input("enter the month"))
year=int(input("enter the year"))
if date >=1 and date <=31 and month >1 and month <12:
    print("next day"/"date"/"month"/"year")
else:
    print('next wrong day')
    