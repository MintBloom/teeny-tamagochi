
import random
import time

class Colours:
    # ANSI colour codes
    RED = '\033[0;31m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Robot:

    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour
    
    def Eating(self):
        # prints a set of messages to do with feeding the robot 
        print(f"{self.name} is {Colours.RED}hungry{Colours.EndC} and wants to eat!")
        input(f"press {Colours.BOLD}enter{Colours.ENDC} to feed {self.name}")
        print("nom nom")
        input("")
        print("nom nom")
        input("")
        print(f"{self.name} has a wonderful meal!")
        print(f"{self.name} is {Colours.GREEN}happy{Colours.RED}.")

    def Sleeping(self):
        # prints string with given robot name
        print(f"{self.name} has a nap. It was alright.")

    def Exercising(self):
        # prints string with given robot name
        print(f"{self.name} did not enjoy exercising. He or she feels much older than {self.age}")

    def interactWithRobot(self):
        # returns an activity for the robot to do as a string
        print(f"Would you like {self.name} to eat, sleep or exercise?")
        return input("-->")

def createRobot():
    # creates a robot from the Robot class which takes a given name, age and colour
    print("Give your robot a name.")
    c1 = input("-->")
    print("How old is your Robot?")
    c2 = input("-->")
    print("What colour is your robot?")
    c3 = input("-->")
    return Robot(c1,c2,c3)

def numberGen():
    return random.randint[1,3]

def robotNeeds():
    robot_wants = numberGen()
    match robot_wants:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass

def main():
    r1 = createRobot()
    r1_choice = r1.interactWithRobot()
    print('complete')

main()

print(f"Warning: No active frommets remain.{Colours.RED} Continue?{Colours.ENDC}")