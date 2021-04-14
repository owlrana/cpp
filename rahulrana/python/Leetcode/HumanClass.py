# Check file

# to check how the fuck 'is' is working in python


class Human():
    def __init__(self, name, age, height, weight, score):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.score = score
    
    def __str__(self):
        string = str(self.name) + " is a man."
        return string

choice = True
lst = []
i = 0

while i < 2:
    mrbean = Human
    name = input("Enter the name: ")
    print("Enter the age of ", name, ": ")
    age = input()
    print("Enter the height of ", name, ": ")
    height = input()
    print("Enter the weight of ", name, ": ")
    weight = input()
    print("Enter the score of ", name, ": ")
    score = input()
    choice = False
    man = mrbean(name, age, height, weight, score)
    lst.append(man)
    i += 1

for humans in lst:
    print(humans)