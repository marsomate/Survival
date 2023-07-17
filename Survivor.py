import os


class Caracter:
    def __init__(self) -> None:
        self.health = 10

    def choice(self, result):
        if ((self.health + result) < 100):
            self.health += result
        elif ((self.health + result) >= 100):
            self.health = 100


class Iland:
    def __init__(self, difficulty) -> None:
        self.difficulty = difficulty
        f = open("tasks.txt", "r")
        self.tasks = f.read()
        self.tasks = self.tasks.split('\n')

    def task_printer(self):
        print(self.tasks[0], "\n",
              self.tasks[1], "\n", self.tasks[2], "\n", self.tasks[3])
        del self.tasks[0:5]

        check = False
        while not check:
            choice = input()
            if choice == "a" or choice == "1":
                choice = int(0)
                check = True
            elif choice == "b" or choice == "2":
                choice = int(1)
                check = True
            elif choice == "c" or choice == "3":
                choice = int(2)
                check = True
            else:
                print("Input is not valid.")

        return (int(self.tasks[choice][6:9]))

    def consequences(self):
        print(self.tasks[0], "\n",
              self.tasks[1], "\n", self.tasks[2])
        del self.tasks[0:3]
        input("If You are ready for the next task please hit any key")


try:
    os.system('cls')
    caracter = Caracter()
    location = Iland(1)
    good = True
    i = 0
    print(""" _     _                 _ 
(_)   | |               | |
 _ ___| | __ _ _ __   __| |
| / __| |/ _` | '_ \ / _` |
| \__ \ | (_| | | | | (_| |
|_|___/_|\__,_|_| |_|\__,_|
                           """)
    print("In this role-playing game, you find yourself on an exciting adventure.One day, you are traveling on a plane when suddenly, a massive storm breaks out. The plane crashes, and miraculously, you survive, ending up on a deserted island. Your goal now is to survive, explore the island, and find a way to get back to civilization.")
    input("If you are ready press any key")
    while good and i < 10:
        try:
            os.system('cls')
            print(""" _     _                 _ 
(_)   | |               | |
 _ ___| | __ _ _ __   __| |
| / __| |/ _` | '_ \ / _` |
| \__ \ | (_| | | | | (_| |
|_|___/_|\__,_|_| |_|\__,_|
                           """)
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
    if i == 10:
        print("Ending: You are successfully rescued and returned to civilization. Despite the challenges and hardships you faced, your survival skills and resourcefulness allowed you to make it through. The experience has left you with a newfound appreciation for the simple things in life and a resilient spirit that will stay with you forever. You reflect on your time on the island as a transformative journey that tested your limits and taught you the importance of adaptability and perseverance.")
        print("Your survival rate is ", caracter.health, "%")
except KeyboardInterrupt:
    print("Exiting...")
