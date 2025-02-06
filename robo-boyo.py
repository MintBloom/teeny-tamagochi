
import random
import time

class Colours:
    '''Ansi colour codes
    - when wrapped around text, it will change the text's colour according to the code's colour'''
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
        print(f"{self.name} is {Colours.RED}hungry{Colours.ENDC} and wants to eat!")
        input(f"press {Colours.BOLD}enter{Colours.ENDC} to feed {self.name}.")
        print("nom nom...")
        input("")
        print("munch munch...")
        input("")
        print(f"{self.name} has a wonderful meal!")
        print(f"{self.name} is {Colours.GREEN}happy{Colours.ENDC}.")

    def Sleeping(self):
        # prints a set of messages to do with letting the robot sleep
        print(f"{self.name} is {Colours.RED}tired{Colours.ENDC} and wants to snooze!")
        input(f"press {Colours.BOLD}enter{Colours.ENDC} to let {self.name} sleep.")
        print("zzzzzzz...")
        input("")
        print("zzzzzzzz...")
        input("")
        print(f"{self.name} feels refreshed!")
        print(f"{self.name} is quite {Colours.GREEN}satisfied{Colours.ENDC}.")

    def Exercising(self):
        # prints a set of messages to do with 
        print(f"{self.name} is feeling energetic {Colours.RED}energetic{Colours.ENDC} and wants to try exercising!")
        input(f"press {Colours.BOLD}enter{Colours.ENDC} to help {self.name} deadlift some weights.")
        print("hufff...")
        input("")
        print("hufff...")
        input("")
        print("A new personal best deadlift!")
        print(f"{self.name} is very {Colours.GREEN}happy{Colours.ENDC}.")
        print(f"However {self.name} now feels much older than {self.age}.")

def helping(self):
    # decide whether or not to help the robot
    while True:
        print(f'Would you like to help {self.name} with something?') # this and the line below are turning red for some reason
        choice = input('-->')
        if choice in ('yes' or 'Yes'):
            robotNeeds(self)
            True
        else:
            break

def robotNeeds(chosen_robot):
    # matches the generated number to a specific robot function
    robot_wants = numberGen()
    match robot_wants:
        case 1:
            chosen_robot.Eating()
        case 2:
            chosen_robot.Sleeping()
        case 3:
            chosen_robot.Exercising()

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
    # generates a number
    return random.randint(1,3)

def main():
    r1 = createRobot()
    helping(r1)
    print('All done.')

main()