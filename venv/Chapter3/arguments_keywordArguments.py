#positional argument
def user(name,age,town):
    '''This functoin prints name, age, and city from an argument provided to the function.'''

    print("{} is {} years old, from {}".format(name, age, town))

user("wilson",400,"nairobi")

#keyword argument
def user(name,age=0,town="default"):
    '''This functoin prints name, age, and city from an argument provided to the function.'''

    print("{} is {} years old, from {}".format(name, age, town))

user("wilson")
user("wilson", 30, "kisumu")
user("wilson", town="mombasa")

# *args and **kwargs
def user(name,age,town, *args, **kwargs):

    print("{} is {} years old, from {}".format(name, age, town))

user("wilson", 30, "kisumu")
user("wilson", 30, "kisumu", 3000, gender="male")

# *args and **kwargs
def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. Her email is {}.".format(fname, lname, company, email))


application("Jess", "Ingrass", "mail @ mail.com", "Teach Code", 75000, hire_date = "September 2010")