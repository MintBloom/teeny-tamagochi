
class Robot():
    def __init__(self, name, age,):
        self.name = name
        self.age = age
    
    def Eating(self):
        print(f"{self.name} has a wonderful meal!")

    def Sleeping(self):
        print(f"{self.name} has a nap. It was alright.")

    def Execising(self):
        print(f"{self.name} did not enjoy exercising. It feels much older than {self.age}")

def main():
    print("Give your robot a name.")
    c1 = input("-->")
    print("And how old is your Robot?")
    c2 = input("-->")
    R1 = Robot(c1, c2)
    print(f"Would you like {c1} to eat, sleep or exercise?")
    c3 = input("-->")
    if c3 == "eat":
        Robot.Eating(R1)
    elif c3 == "sleep":
        Robot.Sleeping(R1)
    elif c3 == "execise":
        Robot.Execising(R1)

main()