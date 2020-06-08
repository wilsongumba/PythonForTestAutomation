class Person:
    def __init__(self, firstname, lastname, health, status):

        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        print("hello, my name is {} {}".format(self.firstname, self.lastname))

    def emote(self):
        emotion = random.randrange(1,3)
        if emotion == 1:
            print("{} is happy today".format(self.firstname))
        elif emotion == 2:
            print("{} is sad today".format(self.firstname))

    def status_change(self):
        if ((self.health >= 76) and (self.health <= 100)):
            print("{} is healthy".format(self.firstname))
        elif ((self.health >= 51) and (self.health <= 75)):
            print("{} is unwell".format(self.firstname))
        elif ((self.health >= 26) and (self.health <= 50)):
            print("{} is critical".format(self.firstname))
        elif ((self.health >= 0) and (self.health <= 25)):
            print("{} is unconsious".format(self.firstname))
        else:
            print("out of range")

Jack = Person("Jack", "Wilson", 8, status=True)
Elvis = Person("Elvis", "John", 88, status=False)
Jane = Person("Jane", "Williams", 45, status=False)
Emily = Person("Emily", "Will", 66, status=True)

print("{} is my friend? {}".format(Jack.firstname, Jack.status))
print("{} is my friend? {}".format(Elvis.firstname, Elvis.status))

Jack.introduce()
Jane.introduce()
Elvis.introduce()
Emily.introduce()

Jack.status_change()
Jane.status_change()
Elvis.status_change()
Emily.status_change()

