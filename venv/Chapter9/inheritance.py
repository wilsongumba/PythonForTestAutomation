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
        if ((self.health >= 101)):
            print("{} is superhuman".format(self.firstname))
        if ((self.health >= 76) and (self.health <= 100)):
            print("{} is healthy".format(self.firstname))
        elif ((self.health >= 51) and (self.health <= 75)):
            print("{} is unwell".format(self.firstname))
        elif ((self.health >= 26) and (self.health <= 50)):
            print("{} is critical".format(self.firstname))
        elif ((self.health >= 0) and (self.health <= 25)):
            print("{} is unconsious".format(self.firstname))
        else:
            print("{} is dead".format(self.firstname))

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



#inheritance
class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)
        self.weapon = weapon

    #overide polymorphism
    def introduce(self):
        print("You are my mortal enemy!!!")

    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'stick':
            other.health -= 5
        print(other.health)

    def insult(self, other):
        if other.health <= 80:
            print("{}, you are weak".format(other.firstname))

    def steal(self, other):
        print("{}, i stole your stuff!".format(other.firstname))
        if other.status ==True:
            other.status == False


Bruce = Enemy('rock', 'Bruce', 'Wayne', 86, status=False)
Bruce.introduce()
Bruce.hurt(Jack)
Bruce.insult(Elvis)
Bruce.insult(Jack)