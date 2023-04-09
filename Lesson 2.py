import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 45
        self.alive = True


    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5


    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3


    def to_chill(self):
        print("Rest time")
        self.gladness += 9
        self.progress -= 0.1
        self.money -= 4

    def to_work(self):
        print("Time to work!")
        self.gladness -= 5
        self.money += 6

    def hard_work(self):
        print("Not enough money... I'll work a little harder!")
        self.gladness -= 20
        self.money += 45

    def additional_courses(self):
        print("I study badly... Worth attending additional courses!")
        self.progress += 1.3
        self.money -= 30
        self.gladness -= 10


    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally…")
            self.alive = False
        elif self.money <= 0:
            print("Bankrupt…")
            self.alive = False


    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money = {self.money}")


    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")

        live_cube = random.randint(1, 4)

        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_work()

        if -0.49 <= self.progress <= -0.15 and self.money >= 45:
            self.additional_courses()

        if self.gladness >= 100 and self.money <= 50:
            self.hard_work()

        self.end_of_day()
        self.is_alive()


nick = Student(name="Nick")

for day in range(366):
    if nick.alive:
        nick.live(day)