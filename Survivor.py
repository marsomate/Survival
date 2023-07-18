"""With this import we can clear the console"""
import os


class Caracter:
    """This class simulate our player with all his attributes (Health)"""
    def __init__(self) -> None:
        self.health = 10

    def choice(self, result):
        """This function gets the users choice and calculates its health"""
        if ((self.health + result) < 100):
            self.health += result
        elif ((self.health + result) >= 100):
            self.health = 100


class Location:
    """This class represents the location/enviroment of the game"""
    def __init__(self) -> None: # This constructor load all the tasks and qouestions
        file = open("C:/Users/MMarso/Documents/GitHub/Survival/tasks.txt", "r")
        self.tasks = file.read()
        self.tasks = self.tasks.split('\n') #  This function splits the string to a list (Enter)
        self.choice = 0 # We need this variable for the consequences function

    def task_printer(self):
        """This function prints the task for the user and get's the choice and returns the score"""
        print(self.tasks[0], "\n",
              self.tasks[1], "\n", self.tasks[2], "\n", self.tasks[3])
        del self.tasks[0:5]
        self.choice = checked_input()
        return (int(self.tasks[self.choice][6:9]))

    def consequences(self):
        """This function prints the consequences"""
        print(self.tasks[self.choice][10:])
        del self.tasks[0:3]
        input("If You are ready for the next task please hit any key")


def print_logo():
    """This is the logo of the game"""
    print(""" _     _                 _ 
(_)   | |               | |
 _ ___| | __ _ _ __   __| |
| / __| |/ _` | '_ \ / _` |
| \__ \ | (_| | | | | (_| |
|_|___/_|\__,_|_| |_|\__,_|
                           """)


def intro():
    """Intro"""
    print_logo()
    print("In this role-playing game, you find yourself on an exciting adventure.")
    print("One day, you are traveling on a plane when suddenly, a massive storm breaks out.")
    print("The plane crashes, and miraculously, you survive, ending up on a deserted island.")
    print("Your goal now is to survive, explore the island,")
    print("and find a way to get back to civilization.")
    input("If you are ready press any key")


def checked_input():
    """This function gets a checked input from the console"""
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


def outro(caracter_outro):
    """Outro"""
    print("Ending: You are successfully rescued and returned to civilization.")
    print("Despite the challenges and hardships you faced, your survival skills and resourcefulness allowed you to make it through.")
    print("The experience has left you with a newfound appreciation for the simple things in life and a resilient spirit that will stay with you forever.")
    print("You reflect on your time on the island as a transformative journey that tested your limits and taught you the importance of adaptability and perseverance.")
    print("Your survival rate is ", caracter_outro.health, "%")


try: #This section is the main program
    os.system('cls')
    caracter = Caracter() # Creating instances of the classes
    location = Location()
    GOOD = True
    i = 0
    intro()
    while GOOD and location.tasks:
        try:
            os.system('cls')
            print_logo()
            print("Survive percentage: ", caracter.health, "%")
            caracter.choice(location.task_printer()) # Question > answers > userInput > calculateTheHealt
            location.consequences() # Printing the consequencies
            i += 1
            if caracter.health <= 0:
                GOOD = False
                input("Unfortunatelly you didn't make it")
        except KeyboardInterrupt:
            print("Exiting...")
            GOOD = False
    if i >= 10:
        outro(caracter)

except KeyboardInterrupt: # Exception handling
    print("Exiting...")

# Make sure to the program can handle dinamic pieces of answer
# Generate a 200 pieces of task
# Make multiple location and scenarios
# Dynamic question
# Random events random effect
# Make it harder
