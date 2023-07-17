import os


class Caracter:
    def __init__(self) -> None:
        self.health = 10

    def choice(self, result):
        if ((self.health + result) < 100):
            self.health += result
        elif ((self.health + result) >= 100):
            self.health = 100


class Location:
    def __init__(self) -> None:
        f = open("tasks.txt", "r")
        self.tasks = f.read()
        self.tasks = self.tasks.split('\n')
        self.choice = 0

    def task_printer(self):
        print(self.tasks[0], "\n",
              self.tasks[1], "\n", self.tasks[2], "\n", self.tasks[3])
        del self.tasks[0:5]
        self.choice = checked_input()
        return (int(self.tasks[self.choice][6:9]))

    def consequences(self):
        print(self.tasks[self.choice][10:])
        del self.tasks[0:3]
        input("If You are ready for the next task please hit any key")


def print_logo():
    print(""" _     _                 _ 
(_)   | |               | |
 _ ___| | __ _ _ __   __| |
| / __| |/ _` | '_ \ / _` |
| \__ \ | (_| | | | | (_| |
|_|___/_|\__,_|_| |_|\__,_|
                           """)


def intro():
    print_logo()
    print("In this role-playing game, you find yourself on an exciting adventure.One day, you are traveling on a plane when suddenly, a massive storm breaks out. The plane crashes, and miraculously, you survive, ending up on a deserted island. Your goal now is to survive, explore the island, and find a way to get back to civilization.")
    input("If you are ready press any key")


def checked_input():
    while True:
        choice = input()
        if choice == "a" or choice == "1":
            return (0)
        elif choice == "b" or choice == "2":
            return (1)
        elif choice == "c" or choice == "3":
            return (2)
        else:
            print("Input is not valid.")


def outro(caracter):
    print("Ending: You are successfully rescued and returned to civilization. Despite the challenges and hardships you faced, your survival skills and resourcefulness allowed you to make it through. The experience has left you with a newfound appreciation for the simple things in life and a resilient spirit that will stay with you forever. You reflect on your time on the island as a transformative journey that tested your limits and taught you the importance of adaptability and perseverance.")
    print("Your survival rate is ", caracter.health, "%")


try:
    os.system('cls')
    caracter = Caracter()
    location = Location()
    good = True
    i = 0
    while good and location.tasks:
        try:
            os.system('cls')
            print_logo()
            print("Survive percentage: ", caracter.health, "%")
            caracter.choice(location.task_printer())
            location.consequences()
            i += 1
            if caracter.health <= 0:
                good = False
                input("Unfortunatelly you didn't make it")
        except KeyboardInterrupt:
            print("Exiting...")
            good = False
    if i >= 10:
        outro(caracter)

except KeyboardInterrupt:
    print("Exiting...")

# Make sure to the program can handle dinamic pieces of answer
# Generate a 200 pieces of task
# Make multiple location and scenarios
# Dynamic question
# Random events random effect
# Make it harder
