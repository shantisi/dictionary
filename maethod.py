# Dictionary methods

# clear() – Remove all the elements from the dictionary
# copy() – Returns a copy of the dictionary
# get() – Returns the value of specified key
# items() – Returns a list containing a tuple for each key value pair
# keys() – Returns a list containing dictionary’s keys
# pop() – Remove the element with specified key
# popitem() – Removes the last inserted key-value pair
# update() – Updates dictionary with specified key-value pairs
# values() – Returns a list of all the values of dictionar


# dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}
  
# copy() method

# dict1={"brand":"suzuki","model":"dizire","year":2020}
# dict2 = dict1.copy()
# print(dict2)

# clear() method
# dict={"brand":"suzuki","model":"dizire","year":2020}
# dict.clear()
# print(dict)
  
# get() method
# dict={"brand":"suzuki","model":"dizire","year":2020}
# print(dict.get("brand"))
  
# items() method
# dict={"brand":"suzuki","model":"dizire","year":2020}
# print(dict.items())
  
# values() method
# dict={"brand":"suzuki","model":"dizire","year":2020}
# print(dict.values())
  
# pop() method
# dict={"brand":"suzuki","model":"dizire","year":2020}
# dict.pop("model")
# print(dict)
  
# popitem() method
# dict={"brand":"suzuki","model":"dizire","year":2020}
# dict.popitem()
# print(dict)
  
# update() method
# dict={"brand":"suzuki","model":"dizire","year":2020}
# dict.update({3: "Scala"})
# print(dict)
  

# values() method

# dict={"brand":"suzuki","model":"dizire","year":2020}
# for x in dict.values():
#     print(x)

# items()

# dict={"brand":"suzuki","model":"dizire","year":2020}
# for k,v in dict.items():
#     print(k,v)

        # setdefault()
# dict={"brand":"suzuki","model":"dizire","year":2020}
# x=dict.setdefault("place","new delhi")
# print(x)
# print(dict)

        # del()
# dict={"brand":"suzuki","model":"dizire","year":2020}
# del dict["model"]
# print(dict)


# key()
# dict={"brand":"suzuki","model":"dizire","year":2020}
# d=dict.keys()
# print(d)

# details={'Name': 'RAM','Age': 17, 'student': {'id': 22,'place': 'dharamsala'}} 
# details['student']['id']=35
# print(details);

# d1 = {"john":40, "peter":45}
# d2 = {"john":466, "peter":45}
# d1==d2
# print(d1==d2)
        

        # len()
# meal ={"monday":  "Chole chawal","sunday":  "Fried rice","wednesday":  "dosa"}
# print(len(meal))


# meal ={"monday":  "Chole chawal","sunday":  "Fried rice","wednesday":  "dosa"}
# h={}
# for i in meal:
#         # h.update({i:meal[i]})
#         h[i]=meal[i]
# print(h)



# meal ={"monday":  "Chole chawal","sunday":  "Fried rice","wednesday":  "dosa"}
# for i in meal:
#         print(meal[i])

meal ={"monday":  "Chole chawal","sunday":  "Fried rice","wednesday":  "dosa"}
for i in meal:
        print(meal[i])

