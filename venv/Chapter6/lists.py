fruits = ["apples", "peaches", "apples", "pears", "apples"]
years = [3, "1998", 2.5, 987, "1994"]


#check membership
print("apples" in fruits)
print("apple" in fruits)

#check membership and number of item
print(fruits.count("apples"))

#check membership and index
print(fruits.index("peaches"))


print(fruits, years)

#append
fruits.append("oranges")
print(fruits)

#extend
fruits.extend(years)
print(fruits)

#remove
fruits.remove("pears")
print(fruits)

#remove with pop
fruits.pop(0)
print(fruits)

#remove last item one with pop
fruits.pop(-1)
print(fruits)


#sorting
numbers = [2,33,4,65,785,43,46,56,5555555,683,46,34,764,76]
numbers.sort()
print(numbers)
