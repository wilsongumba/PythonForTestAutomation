#if statements
name = input("enter name: ")
if name == "wilson":
    print("hi {}".format(name))

print ("havea nice day {}".format(name))

# elif statements
number = int(input("enter number: "))
if number > 0:
    print("hi, {} is a positive number".format(number))

elif number < 0:
    print("hi, {} is a negative number".format(number))

elif number == 0:
    print("hi, is {} this positive or negative?".format(number))

print("have a mathed day {}!".format(name))


#else
name = input("What's your name? ")
if name == "Jessica":
    print("Hello, nice to see you {}".format(name))
elif name == "Danielle":
    print("Hello, you are a great person!")
elif name != "Mariah":
    print("You're not Mariah!")
elif name == "Kingston":
    print("Hi, {}, let's have lunch soon!".format(name))
else:
    print("Have a nice day!")

    