dictionary = {"food": 43, "energy": 645, "friends": 23}

#gets value of specified item
print(dictionary.get("food"))

#gets all keys and values
print(dictionary.items())

#gets keys only
print(dictionary.keys())

#set default
print(dictionary.setdefault("food"))
print(dictionary)
print(dictionary.setdefault("enemies", 126))
print(dictionary)



#removes last item with pop
print(dictionary.popitem())
print(dictionary)

#update
dictionary2 = {"food": 43, "energy": 645, "friends": 23}
dictionary3 = {"planes": 43, "cars": 645, "ship": 23}

dictionary2.update(dictionary3)
print(dictionary2)


#update existing
dictionary4 = {"planes": 324, "cars": 5, "ship": 243}
dictionary3.update(dictionary4)
print(dictionary3)

#update existing addnew
dictionary4 = {"planes": 324, "cars": 5, "jet": 3}
dictionary3.update(dictionary4)
print(dictionary3)

#update directly
dictionary3.update(food = 450, cookies = 6)
print(dictionary3)