#while loops
temp = int(input("Enter temperature: "))

while temp > 35:
    print("The temperature is {}°c, this is critical!".format(temp))
    print("...normalizing...")
    temp -=1

#break
    if temp == 37:
        print("normalized at {}°c! You're good!".format(temp))
        break



#continue
for number in range(0,11):
    if number == 6:
        print("skipping 6")
        continue
    print("number {}".format(number))

#pass
for number in range(0,11):
    if number == 8:
        pass
    else:
        print("number {}".format(number))

