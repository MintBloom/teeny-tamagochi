
class Robot():
    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour
    
    def Eating(self):
        print(f"{self.name} has a wonderful meal!")

    def Sleeping(self):
        print(f"{self.name} has a nap. It was alright.")

    def Execising(self):
        print(f"{self.name} did not enjoy exercising. He or she feels much older than {self.age}")

def main():
    print("Give your robot a name.")
    c1 = input("-->")
    print("How old is your Robot?")
    c2 = input("-->")
    print("What colour is your robot?")
    c3 = input("-->")
    R1 = Robot(c1, c2, c3)
    print(f"Would you like {c1} to eat, sleep or exercise?")
    c4 = input("-->")
    if c4 == "eat":
        Robot.Eating(R1)
    elif c4 == "sleep":
        Robot.Sleeping(R1)
    elif c4 == "exercise":
        Robot.Execising(R1)
    input("")
    print(f"{c1} toodles off now.")

main()